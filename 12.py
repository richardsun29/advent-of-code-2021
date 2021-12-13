from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()

# bidirectional
graph = defaultdict(set)

for line in lines:
    node1, node2 = line.split('-')
    graph[node1].add(node2)
    graph[node2].add(node1)


def find_paths(current_cave, visited_small, path, visited_small_twice):
    if current_cave == 'end':
        yield path
        return

    visited_small = visited_small.copy()
    if current_cave.islower():  # is small cave
        visited_small.add(current_cave)

    connected_caves = graph[current_cave]
    for next_cave in connected_caves:
        if next_cave not in visited_small:
            yield from find_paths(next_cave, visited_small, path + [next_cave], visited_small_twice)
        elif not visited_small_twice and next_cave not in ['start', 'end']:
            yield from find_paths(next_cave, visited_small, path + [next_cave], True)


paths = []
for path in find_paths('start', set(), ['start'], False):
    paths.append(path)
    #print(path)

print(len(paths))
