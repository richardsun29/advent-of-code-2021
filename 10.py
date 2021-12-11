with open('input.txt') as f:
    lines = f.read().splitlines()


closing_chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

scores_incomplete = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

corrupted_score = 0
incomplete_scores = []

for line in lines:
    stack = []
    is_corrupted = False
    incomplete_score = 0
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            top = stack.pop()
            if char != closing_chars[top]:  # corrupted
                corrupted_score += scores[char]
                is_corrupted = True
                break
    if not is_corrupted:  # incomplete
        for char in reversed(stack):
            points = scores_incomplete[closing_chars[char]]
            incomplete_score *= 5
            incomplete_score += points
        incomplete_scores.append(incomplete_score)

print(corrupted_score)

incomplete_scores.sort()
print(incomplete_scores[len(incomplete_scores) // 2])
