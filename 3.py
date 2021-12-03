from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()


def part1():
    ones = defaultdict(int)

    num_bits = len(lines[0])

    for num in lines:
        for bit in range(num_bits):
            if num[bit] == '1':
                ones[bit] += 1

    print(ones)

    gamma = ''
    epsilon = ''
    for bit in range(num_bits):
        if ones[bit] > len(lines) / 2:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    print(gamma)
    print(int(gamma, 2))
    print(epsilon)
    print(int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))
    print('=============')


def get_majority_bit(nums, bit):
    bits = [num[bit] for num in nums]

    ones = sum([b == '1' for b in bits])
    zeros = sum([b == '0' for b in bits])

    if ones == zeros:
        return '1'
    elif ones > zeros:
        return '1'
    else:
        return '0'


def calc_oxy(nums):
    #while len(nums) > 1:
    for bit in range(len(nums[0])):
        m = get_majority_bit(nums, bit)
        nums = list(filter(lambda num: num[bit] == m, nums))
    return nums[0]


def get_minority_bit(nums, bit):
    bits = [num[bit] for num in nums]

    ones = sum([b == '1' for b in bits])
    zeros = sum([b == '0' for b in bits])

    if ones == zeros:
        return '0'
    elif ones > zeros:
        return '0'
    else:
        return '1'

def calc_co2(nums):
    for bit in range(len(nums[0])):
        m = get_minority_bit(nums, bit)
        nums = list(filter(lambda num: num[bit] == m, nums))
        if len(nums) == 1:
            break
    return nums[0]

oxy = calc_oxy(lines)
co2 = calc_co2(lines)
print(oxy)
print(co2)
print(int(oxy, 2) * int(co2, 2))
