import contextlib

with open('input.txt') as f:
    lines = f.read().splitlines()

heightmap = [[int(d) for d in line] for line in lines]
#print(heightmap)

r_max = len(heightmap)
c_max = len(heightmap[0])


def get_adj(r, c):
    for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= adj_r < r_max and 0 <= adj_c < c_max:
            yield adj_r, adj_c


def calc_basin_size(r, c):
    basin_size = 1
    heightmap[r][c] = -1  # mark it
    for adj_r, adj_c in get_adj(r, c):
        adjacent_height = heightmap[adj_r][adj_c]
        if adjacent_height in [9, -1]:
            continue
        basin_size += calc_basin_size(adj_r, adj_c)
    return basin_size


risk_sum = 0
low_points = []
basins = []

for r in range(r_max):
    for c in range(c_max):
        height = heightmap[r][c]
        adjacent_heights = []
        for adj_r, adj_c in get_adj(r, c):
            adjacent_heights.append(heightmap[adj_r][adj_c])
        if height < min(adjacent_heights):
            #print(f'low point found: ({r}, {c})')
            low_points.append((r, c))
            risk_sum += height + 1

print(risk_sum)

for r, c in low_points:
    basin_size = calc_basin_size(r, c)
    basins.append(basin_size)

basins.sort()
print(basins[-1] * basins[-2] * basins[-3])
