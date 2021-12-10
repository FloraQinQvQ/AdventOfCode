f = open('./2021/inputs/10.txt')
lines = f.read().splitlines()

lefts = ['(', '{', '<', '[']
rights = [')', '}', '>', ']']
corrupted = []
points = {')': 1, ']': 2, '}': 3, '>': 4}

completes = []

for line in lines:
    stack = []
    complete = []
    is_corrupted = False
    for char in line:
        if char in lefts:
            stack.append(char)
        if char in rights:
            top = stack.pop()
            if top not in lefts:
                corrupted.append(char)
                is_corrupted = True
            elif lefts.index(top) != rights.index(char):
                corrupted.append(char)
                is_corrupted = True
    while stack and not is_corrupted:
        top = stack.pop()
        complete.append(rights[lefts.index(top)])

    if complete:
        completes.append(complete)

scores = []
for complete in completes:
    score = 0
    for ele in complete:
        score = score * 5
        score += points[ele]
    scores.append(score)

scores = sorted(scores)

print(scores)
print(scores[int(len(scores)/2)])
