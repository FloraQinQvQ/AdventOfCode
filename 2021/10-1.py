f = open('./2021/inputs/10.txt')
lines = f.read().splitlines()

lefts = ['(', '{', '<', '[']
rights = [')', '}', '>', ']']
corrupted = []
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

for line in lines:
    stack = []
    for char in line:
        if char in lefts:
            stack.append(char)
        if char in rights:
            top = stack.pop()
            if top not in lefts:
                corrupted.append(char)
            elif lefts.index(top) != rights.index(char):
                corrupted.append(char)
            else:
                continue
sum = 0
for corr in corrupted:
    sum += points[corr]
print(sum)




