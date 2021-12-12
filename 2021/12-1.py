from pprint import pprint

# f = open('./2021/inputs/12-sample.txt')
f = open('./2021/inputs/12.txt')
lines = f.read().splitlines()

data = {}

for line in lines:
    nodes = [x for x in line.split('-')]
    for node in nodes:
        if node not in data:
            data[node] = []

    data[nodes[0]].append(nodes[1])
    data[nodes[1]].append(nodes[0])

path = ['start']
solutions = []


def find_paths():
    global path
    if path[-1] != 'end':
        for next in data[path[-1]]:
            if next.isupper() or next not in path:
                path.append(next)
                find_paths()
                del(path[-1])
    else:
        solutions.append(path.copy())


find_paths()

print(len(solutions))
