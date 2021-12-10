f = open('./2021/inputs/6.txt')
content = f.read()
inputs = [int(ele) for ele in content.splitlines()[0].split(',')]

total_days = 256

data = {}
for i in range(max(9, max(inputs))):
    data[i] = 0
for input in inputs:
    data[input] += 1

for day in range(256):
    zeroes = data[0]
    data[0] = 0
    for i in range(1, len(data)):
        data[i - 1] += data[i]
        data[i] = 0
    data[6] += zeroes
    data[8] += zeroes

print(sum(data.values()))
