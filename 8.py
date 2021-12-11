import itertools

def parse_line(line):
    tokens = line.split(' ')
    signal_patterns = tokens[:10]
    signal_patterns = [set(x) for x in signal_patterns]
    output_patterns = tokens[-4:]
    output_patterns = [set(x) for x in output_patterns]
    return signal_patterns, output_patterns


with open('input.txt') as f:
    lines = f.read().splitlines()


"""
Segments
0   6
1   2   -
2   5
3   5
4   4   -
5   5
6   6
7   3   -
8   7   -
9   6

seg count
2   1  
3   1
4   1
5   3
6   3
7   1
"""

def part1():
    count1478 = 0
    for line in lines:
        _, output_patterns = parse_line(line)
        for pattern in output_patterns:
            if len(pattern) in [2, 4, 3, 7]:
                count1478 += 1

    print(count1478)


def get_mappings():
    for permutation in itertools.permutations('abcdefg'):
        # displayed -> real
        mapping = {
            permutation[0]: 'a',
            permutation[1]: 'b',
            permutation[2]: 'c',
            permutation[3]: 'd',
            permutation[4]: 'e',
            permutation[5]: 'f',
            permutation[6]: 'g',
        }
        yield mapping


class DecodeDigitError(Exception):
    pass


def decode_digit(mapping, digit):
    decoded_segments = set()
    for segment in digit:
        decoded_segments.add(mapping[segment])

    if decoded_segments == set('abcefg'):
        return '0'
    if decoded_segments == set('cf'):
        return '1'
    if decoded_segments == set('acdeg'):
        return '2'
    if decoded_segments == set('acdfg'):
        return '3'
    if decoded_segments == set('bcdf'):
        return '4'
    if decoded_segments == set('abdfg'):
        return '5'
    if decoded_segments == set('abdefg'):
        return '6'
    if decoded_segments == set('acf'):
        return '7'
    if decoded_segments == set('abcdefg'):
        return '8'
    if decoded_segments == set('abcdfg'):
        return '9'

    raise DecodeDigitError()


sum = 0

for line in lines:
    signal_patterns, output_patterns = parse_line(line)
    for mapping in get_mappings():
        try:
            decoded_signals = [decode_digit(mapping, digit) for digit in signal_patterns]
            decoded_outputs = [decode_digit(mapping, digit) for digit in output_patterns]
        except DecodeDigitError:
            continue

        output_num = int(''.join(decoded_outputs))
        #print(output_num)
        sum += output_num
        break

print(sum)
