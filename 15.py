with open('input.txt') as f:
    lines = f.read().splitlines()

grid = [[int(d) for d in line] for line in lines]


def increase_risk(row):
    new_row = [n + 1 if n < 9 else 1 for n in row]
    return new_row


# make board bigger to the right
for row in grid:
    current_row = row
    for i in range(4):
        new_row = increase_risk(current_row)
        current_row = new_row
        row += new_row

# make board bigger down
original_r_max = len(grid)
for i in range(original_r_max * 4):
    new_row = increase_risk(grid[i])
    grid.append(new_row)



r_max = len(grid)
c_max = len(grid[0])

risk_levels = [[2**63] * c_max for i in range(r_max)]
risk_levels[0][0] = 0


def get_adj(r, c):
    for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= adj_r < r_max and 0 <= adj_c < c_max:
            yield adj_r, adj_c


changed = 1
while changed > 0:
    changed = 0
    for r in range(r_max):
        for c in range(c_max):
            min_risk = risk_levels[r][c]
            for adj_r, adj_c in get_adj(r, c):
                # move from adj -> current
                path_risk = risk_levels[adj_r][adj_c] + grid[r][c]
                min_risk = min(min_risk, path_risk)
            if min_risk < risk_levels[r][c]:
                risk_levels[r][c] = min_risk
                changed += 1
    print(f'changed = {changed}')

print(risk_levels[-1][-1])