from pprint import pprint

# f = open('./2021/inputs/12-sample.txt')
f = open('./2021/inputs/12.txt')
lines = f.read().splitlines()

data = {}

for line in lines:
    nodes = [x for x in line.strip().split('-')]
    for node in nodes:
        if node not in data:
            data[node] = []
    if nodes[1] != 'start' and nodes[0] != 'end':
        data[nodes[0]].append(nodes[1])
    if nodes[1] != 'end' and nodes[0] != 'start':
        data[nodes[1]].append(nodes[0])

solutions = 0
path = [(('start'), set(['start']), False)]


def find_paths():
    global solutions
    global path

    pos, lowercases, twiceyet = path[-1]
    if pos != 'end':
        for next in data[pos]:
            if next not in lowercases:
                if next.islower():
                    path.append(
                        (next, lowercases.union(set([next])), twiceyet))
                else:
                    path.append((next, lowercases, twiceyet))
                find_paths()
                del(path[-1])
            elif next in lowercases and twiceyet != True:
                path.append((next, lowercases, True))
                find_paths()
                del(path[-1])

    else:
        solutions += 1


find_paths()

# 144309
pprint(solutions)
