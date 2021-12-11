with open('input.txt') as f:
    crabs = [int(i) for i in f.read().split(',')]

#print(max(crabs))


def calc_fuel(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - pos)
    return fuel


def calc_fuel2(crabs, pos):
    fuel = 0
    for crab in crabs:
        distance = abs(crab - pos)
        fuel += distance * (distance + 1) // 2
    return fuel


min_fuel = 2**30

for i in range(2000):
    #min_fuel = min(min_fuel, calc_fuel(crabs, i))
    min_fuel = min(min_fuel, calc_fuel2(crabs, i))

print(min_fuel)