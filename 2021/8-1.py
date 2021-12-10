data = []
with open('./2021/inputs/8.txt') as f:
    line = f.readline()
    while line:
        print(line)
        data.extend(line.strip('\n').split('|')[1].split(' ')[1:])
        line = f.readline()

total = 0
for ele in data:
    # 1.4.7 8
    if len(ele) in [2, 4, 3, 7]:
        total += 1

print(data)
print(total)

