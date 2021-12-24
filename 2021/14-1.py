from collections import Counter
f = open('2021/inputs/14.txt')
lines = f.read().splitlines()


original = lines[0]
input = original[:]
pairs = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in lines[2:]}
steps = 10

c1 = Counter()
for i in range(len(input) - 1):
    c1[input[i] + input[i + 1]] += 1

for step in range(steps + 1):
    if step == steps:
        cf = Counter()
        for k in c1:
            cf[k[0]] += c1[k]
        cf[input[-1]] += 1
        print(max(cf.values()) - min(cf.values()))
    c2 = Counter()

    for k in c1:
        c2[k[0]+pairs[k]] += c1[k]
        c2[pairs[k]+k[1]] += c1[k]

    c1 = c2
