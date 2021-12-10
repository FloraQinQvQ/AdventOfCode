f = open('./2021/inputs/6.txt')
content = f.read()
inputs = [int(ele) for ele in content.splitlines()[0].split(',')]

total_days = 80

for day in range(total_days):
    length = len(inputs)
    for idx in range(length):
        inputs[idx] -= 1
        if inputs[idx] == -1:
            inputs[idx] = 6
            inputs.append(8)
print(inputs)
print(len(inputs))
