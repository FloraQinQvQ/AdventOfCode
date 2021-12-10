import sys

f = open('./2021/inputs/7.txt')
content = f.read()
inputs = [int(ele) for ele in content.splitlines()[0].split(',')]


def sum_up(n):
    results = n + (n-1) * n/2

    return results


total = sys.maxsize
for i in range(max(inputs)):
    temp_sum = sum([sum_up(abs(ele - i)) for ele in inputs])
    if temp_sum < total:
        total = temp_sum

print(int(total))
