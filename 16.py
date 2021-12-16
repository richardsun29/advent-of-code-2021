with open('input.txt') as f:
    hex_input = f.read()

hex_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

binary = ''.join(hex_to_binary[h] for h in hex_input)


def btoi(binary):
    return int(binary, 2)


class Stream:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def read(self, num_bits):
        data = self.data[self.pos:self.pos+num_bits]
        self.pos += num_bits
        return data

    def has_more_packets(self):
        return '1' in self.data[self.pos:]


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

    def version_sum(self):
        return self.version

    def value(self):
        raise NotImplementedError


class LiteralPacket(Packet):
    def __init__(self, version, type_id, literal):
        super().__init__(version, type_id)
        self.literal = literal

    def value(self):
        return self.literal


class OperatorPacket(Packet):
    def __init__(self, version, type_id, subpackets):
        super().__init__(version, type_id)
        self.subpackets = subpackets

    def version_sum(self):
        return self.version + sum(sp.version_sum() for sp in self.subpackets)

    def value(self):
        if self.type_id == 0:  # sum
            return sum(sp.value() for sp in self.subpackets)
        elif self.type_id == 1:  # product
            value = 1
            for sp in self.subpackets:
                value *= sp.value()
            return value
        elif self.type_id == 2:  # minimum
            return min(sp.value() for sp in self.subpackets)
        elif self.type_id == 3:  # maximum
            return max(sp.value() for sp in self.subpackets)
        elif self.type_id == 5:  # greater than
            return 1 if self.subpackets[0].value() > self.subpackets[1].value() else 0
        elif self.type_id == 6:  # less than
            return 1 if self.subpackets[0].value() < self.subpackets[1].value() else 0
        elif self.type_id == 7:  # equal to
            return 1 if self.subpackets[0].value() == self.subpackets[1].value() else 0


stream = Stream(binary)


def read_packet(stream):
    version = btoi(stream.read(3))
    type_id = btoi(stream.read(3))

    if type_id == 4:
        has_more_data = True
        literal = ''
        while has_more_data:
            data = stream.read(5)
            has_more_data = data[0] == '1'
            literal += data[1:]
        return LiteralPacket(version, type_id, btoi(literal))
    else:
        length_type_id = stream.read(1)
        subpackets = []
        if length_type_id == '0':
            subpackets_length = btoi(stream.read(15))
            subpackets_data = stream.read(subpackets_length)
            subpackets_stream = Stream(subpackets_data)
            while subpackets_stream.has_more_packets():
                subpackets.append(read_packet(subpackets_stream))
        else:
            num_subpackets = btoi(stream.read(11))
            for _ in range(num_subpackets):
                subpackets.append(read_packet(stream))
        return OperatorPacket(version, type_id, subpackets)







version_sum = 0

while stream.has_more_packets():
    packet = read_packet(stream)
    print(f'value = {packet.value()}')
    version_sum += packet.version_sum()

print(f'version sum = {version_sum}')


