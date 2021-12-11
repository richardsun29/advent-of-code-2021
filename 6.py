from collections import defaultdict

with open('input.txt') as f:
    initial_fish = [int(i) for i in f.read().split(',')]

# counter -> number of fish
fish = defaultdict(int)

for f in initial_fish:
    fish[f] += 1

print(fish)


def run_day(fish):
    new_fish = defaultdict(int)
    # new fish
    new_fish[8] += fish[0]
    new_fish[6] += fish[0]

    for timer in range(1, 9):
        new_fish[timer - 1] += fish[timer]

    return new_fish


def count_fish(fish):
    return sum(x for _,x in fish.items())


for day in range(256):
    fish = run_day(fish)
    print(f'day {day}: {count_fish(fish)}')