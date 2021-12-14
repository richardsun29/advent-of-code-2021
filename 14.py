from collections import defaultdict
import string
import re

with open('input.txt') as f:
    lines = f.read().splitlines()


def parse_rule(line):
    matches = re.findall(r'(\w)(\w) -> (\w)', line)
    return matches[0]


polymer = list(lines[0])
rules = [parse_rule(line) for line in lines[2:]]


rules_dict = defaultdict(int)
for r1, r2, insert in rules:
    rules_dict[(r1, r2)] = insert


def find_insert_char(pair1, pair2):
    try:
        return rules_dict[(pair1, pair2)]
    except KeyError:
        return None

    #for r1, r2, insert in rules:
    #    if r1 == pair1 and r2 == pair2:
    #        return insert
    #return None


def run_insert_step(polymer):
    new_polymer = [polymer[0]]

    for char in polymer[1:]:
        pair1 = new_polymer[-1]
        pair2 = char
        insert_char = find_insert_char(pair1, pair2)
        if insert_char:
            new_polymer.append(insert_char)
        new_polymer.append(char)

    return new_polymer


#for i in range(40):
#    polymer = run_insert_step(polymer)
#    #print(f'step {i+1}: {len(polymer)} {"".join(polymer)}')
#    print(f'step {i+1}: {len(polymer)}')


def combine_segments(seg1, seg2):
    return seg1 + seg2[1:]


cache = {}

#def run_inserts1(pair1, pair2, depth):
#    if depth == 0:
#        return [pair1, pair2]
#
#    insert_char = find_insert_char(pair1, pair2)
#    if insert_char:
#        if (pair1, insert_char, depth) in cache:
#            seg1 = cache[(pair1, insert_char, depth)]
#        else:
#            seg1 = run_inserts(pair1, insert_char, depth - 1)
#            cache[(pair1, insert_char, depth)] = seg1
#
#        if (insert_char, pair2, depth) in cache:
#            seg2 = cache[(insert_char, pair2, depth)]
#        else:
#            seg2 = run_inserts(insert_char, pair2, depth - 1)
#            cache[(insert_char, pair2, depth)] = seg2
#
#        return combine_segments(seg1, seg2)
#    else:
#        return [pair1, pair2]


def run_inserts(pair1, pair2, depth):
    if depth == 0:
        #cache[(pair1, pair2, depth)] = [pair1, pair2]
        return [pair1, pair2]

    for d in range(depth, 0, -1):
        if (pair1, pair2, d) in cache:
            segment = cache[(pair1, pair2, d)]
            remaining_depth = depth - d
            if remaining_depth > 0:
                segment = expand_polymer(segment, remaining_depth)
                cache[(pair1, pair2, depth)] = segment
            return segment

    try:
        #cache[(pair1, pair2, depth)] = [pair1, pair2]
        return cache[(pair1, pair2, depth)]
    except KeyError:
        pass

    insert_char = find_insert_char(pair1, pair2)
    if insert_char:
        seg1 = run_inserts(pair1, insert_char, depth - 1)
        cache[(pair1, insert_char, depth-1)] = seg1

        seg2 = run_inserts(insert_char, pair2, depth - 1)
        cache[(insert_char, pair2, depth-1)] = seg2

        combined = combine_segments(seg1, seg2)
        #cache[(pair1, pair2, depth)] = combined
        return combined
    else:
        #cache[(pair1, pair2, depth)] = [pair1, pair2]
        return [pair1, pair2]


def expand_polymer(polymer, depth):
    new_polymer = [polymer[0]]
    for i in range(len(polymer)-1):
        pair1 = polymer[i]
        pair2 = polymer[i+1]
        segment = run_inserts(pair1, pair2, depth)
        #print(len(segment))
        new_polymer = combine_segments(new_polymer, segment)
    return new_polymer


new_polymer = []
#for i in range(10):
#new_polymer = expand_polymer(polymer, 10)
print('cache len', len(cache))
print('polymer len', len(new_polymer))




pair_counts = defaultdict(int)
for i in range(len(polymer) - 1):
    pair1 = polymer[i]
    pair2 = polymer[i + 1]
    pair_counts[(pair1, pair2)] = 1

def run_inserts2(pair_counts):
    new_pair_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules_dict:
            insert_char = rules_dict[pair]
            new_pair_counts[pair[0], insert_char] += pair_counts[pair]
            new_pair_counts[insert_char, pair[1]] += pair_counts[pair]
        else:
            new_pair_counts[pair] += pair_counts[pair]
    return new_pair_counts

for i in range(40):
    pair_counts = run_inserts2(pair_counts)
#print(pair_counts)


counts = defaultdict(int)
for pair in pair_counts:
    counts[pair[0]] += pair_counts[pair]
    counts[pair[1]] += pair_counts[pair]

for count in counts:
    #print(f'{count} = {counts[count]}')
    counts[count] //= 2

# first and last were not double counted
counts[polymer[0]] += 1
counts[polymer[-1]] += 1

#for c in new_polymer:
#    counts[c] += 1

min_count = 2**64
max_count = 0
min_char = '.'
max_char = '.'

for c in counts:
    count = counts[c]
    if count < min_count:
        min_count = count
        min_char = c
    if count > max_count:
        max_count = count
        max_char = c


print(f'{min_char} = {min_count}')
print(f'{max_char} = {max_count}')
print(max_count - min_count)