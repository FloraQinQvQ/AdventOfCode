import sys

f = open('./2021/inputs/7.txt')
content = f.read()
inputs = [int(ele) for ele in content.splitlines()[0].split(',')]

total = sys.maxsize
for i in range(len(inputs)):
    suma = sum([abs(ele - inputs[i]) for ele in inputs])
    if suma < total:
        total = suma

print(total)
