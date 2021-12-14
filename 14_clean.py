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
for rule in rules:
    r1, r2, insert = rule
    rules_dict[(r1, r2)] = insert

pair_counts = defaultdict(int)
for i in range(len(polymer) - 1):
    pair1 = polymer[i]
    pair2 = polymer[i + 1]
    pair_counts[(pair1, pair2)] = 1


def run_inserts(pair_counts):
    new_pair_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules_dict:
            insert_char = rules_dict[pair]
            new_pair_counts[pair[0], insert_char] += pair_counts[pair]
            new_pair_counts[insert_char, pair[1]] += pair_counts[pair]
        else:
            new_pair_counts[pair] += pair_counts[pair]
    return new_pair_counts


def calc_answer(pair_counts):
    counts = defaultdict(int)
    for pair in pair_counts:
        counts[pair[0]] += pair_counts[pair]
        counts[pair[1]] += pair_counts[pair]

    # chars are double counted
    for count in counts:
        counts[count] //= 2

    # first and last were not double counted
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1

    max_count = max(counts[c] for c in counts)
    min_count = min(counts[c] for c in counts)

    return max_count - min_count


for i in range(40):
    pair_counts = run_inserts(pair_counts)
    print(f'step {i+1}: {calc_answer(pair_counts)}')
