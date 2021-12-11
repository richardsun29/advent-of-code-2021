with open('input.txt') as f:
    lines = f.read().splitlines()

octs = [[int(d) for d in line] for line in lines]

r_max = len(octs)
c_max = len(octs[0])


def get_adj(r, c):
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            adj_r = r + dr
            adj_c = c + dc
            if 0 <= adj_r < r_max and 0 <= adj_c < c_max:
                yield adj_r, adj_c


def flash(octs, r, c):
    octs[r][c] = 0
    for adj_r, adj_c in get_adj(r, c):
        if octs[adj_r][adj_c] != 0:  # has not flashed yet
            octs[adj_r][adj_c] += 1


def run_step(octs):
    # increase energy
    octs = [[d+1 for d in row] for row in octs]

    # flash
    count_flashes = 0
    changed = True
    while changed:
        changed = False
        for r in range(r_max):
            for c in range(c_max):
                energy = octs[r][c]
                if energy > 9:
                    flash(octs, r, c)
                    changed = True
                    count_flashes += 1

    return octs, count_flashes


total_flashes = 0
for step in range(1000):
    octs, flashes = run_step(octs)
    print(f'step {step+1}: {flashes}')
    total_flashes += flashes
    if flashes == r_max * c_max:
        break  # all flashed

print(total_flashes)
