import re

with open('input.txt') as f:
    lines = f.read().splitlines()

coords = lines[:lines.index('')]
folds = lines[lines.index('')+1:]


def parse_coord(line):
    x, y = line.split(',')
    return int(x), int(y)


def parse_fold(line):
    matches = re.findall(r'(\w)=(\d+)', line)
    axis, num = matches[0]
    return axis, int(num)


coords = [parse_coord(line) for line in coords]
folds = [parse_fold(line) for line in folds]


def do_fold(coord, fold):
    x, y = coord
    axis, num = fold
    if axis == 'y':
        if y < num:
            return x, y  # top part, no change
        else:
            distance_from_fold = y - num
            return x, y - distance_from_fold*2
    elif axis == 'x':
        if x < num:
            return x, y
        else:
            distance_from_fold = x - num
            return x - distance_from_fold*2, y


for fold in folds:
    coords = [do_fold(coord, fold) for coord in coords]
    # print(len(set(coords)))


# visualize
x_max = max(x for x, y in coords)
y_max = max(y for x, y in coords)

grid = []
for i in range(y_max+1):
    grid.append([' '] * (x_max+1))

for coord in coords:
    x, y = coord
    grid[y][x] = '█'

for y in grid:
    print(''.join(y))
