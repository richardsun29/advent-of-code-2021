with open('input.txt') as f:
    lines = f.readlines()

h = 0
d = 0

for line in lines:
    direction, amt = line.split(' ')
    amt = int(amt)
    if direction == 'forward':
        h += amt
    elif direction == 'down':
        d += amt
    elif direction == 'up':
        d -= amt

print(h * d)

h = 0
d = 0
aim = 0

for line in lines:
    direction, amt = line.split(' ')
    amt = int(amt)
    if direction == 'forward':
        h += amt
        d += aim * amt
    elif direction == 'down':
        aim += amt
    elif direction == 'up':
        aim -= amt

print(h * d)

