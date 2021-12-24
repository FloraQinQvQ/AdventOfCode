f = open('./2021/inputs/3.txt')
content = f.read()
inputs = content.splitlines()

map = [0] * len(inputs[0])

for idx, input in enumerate(inputs):
    for index, i in enumerate(input):
        if i == '0':
            map[index] -= 1
        else:
            map[index] += 1

gamma = 0
epsilon = 0
for idx, element in enumerate(map):
    if element > 0:
        gamma += pow(2, len(map)-1 - idx) * 1
        epsilon += pow(2, len(map)-1 - idx) * 0

    else:
        gamma += pow(2, len(map)-1 - idx) * 0
        epsilon += pow(2, len(map)-1 - idx) * 1

print(gamma, epsilon)
print(gamma*epsilon)
