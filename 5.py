import re


def parse_line(line):
    m = re.search(r'(\d+),(\d+) -> (\d+),(\d+)', line)
    return [int(n) for n in m.groups()]


def is_between(target, val1, val2):
    low = min(val1, val2)
    high = max(val1, val2)
    return low <= target <= high


def is_covered(x, y, coords):
    x1, y1, x2, y2 = coords
    if x1 == x2:
        return x1 == x and is_between(y, y1, y2)
    if y1 == y2:
        return y1 == y and is_between(x, x1, x2)


def is_covered2(x, y, coords):
    x1, y1, x2, y2 = coords
    if x1 == x2:
        return x1 == x and is_between(y, y1, y2)
    if y1 == y2:
        return y1 == y and is_between(x, x1, x2)
    else:  # diagonal
        if not is_between(x, x1, x2) or not is_between(y, y1, y2):
            return False
        if abs(x1 - x2) != abs(y1 - y2):
            return False
        #low_x = min(x1, x2)
        #low_y = min(y1, y2)
        #return (x - low_x) == (y - low_y)
        return abs(x - x1) == abs(y - y1)


def run():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    coords = [parse_line(line) for line in lines]

    multi_covered = 0
    for y in range(999):
        print(y)
        for x in range(999):
            covered = 0
            for c in coords:
                #if is_covered(x, y, c):
                if is_covered2(x, y, c):
                    covered += 1
                if covered >= 2:
                    multi_covered += 1
                    break
            #print(covered, end='')
        #print()
    print(multi_covered)

run()