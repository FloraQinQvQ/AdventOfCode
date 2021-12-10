f = open('./2021/inputs/1.txt')
content = f.read()
depths = content.splitlines()

total_increases = 0
for idx, depth in enumerate(depths):
    if idx == 0:
        continue

    if int(depth) > int(depths[idx - 1]):
        total_increases += 1

print(total_increases)
