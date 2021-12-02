with open('input.txt') as f:
    lines = f.readlines()

lines = [int(i) for i in lines]

inc = 0
prev = 99999999

for i in lines:
    if i > prev:
        inc += 1
    prev = i

print(inc)

sums = []
for i in range(len(lines) - 2):
    sums.append(lines[i] + lines[i+1] + lines[i+2])

inc = 0
prev = 99999999

for i in sums:
    if i > prev:
        inc += 1
    prev = i

print(inc)
