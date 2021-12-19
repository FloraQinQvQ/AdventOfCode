import itertools

f = open('./2021/inputs/19.txt')
lines = f.read().splitlines()
lines = [x for x in lines if x != '']

Beacons = []
tmp = []

for line in lines:
    if line.startswith('--- scanner'):
        if line == '--- scanner 0 ---':
            pass
        else:
            Beacons.append(tmp)
            tmp = []
    else:
        x, y, z = [int(x) for x in line.split(',')]
        tmp.append((x, y, z))
Beacons.append(tmp)

n = len(Beacons)
scanner_poses = [(0, 0, 0) for _ in range(n)]


def overlapping(i, j):
    s1 = set(Beacons[i])
    for p in itertools.permutations([0, 1, 2]):
        for c in itertools.product([-1, 1], [-1, 1], [-1, 1]):
            t = [tuple(ci * x[pi] for pi, ci in zip(p, c))
                 for x in Beacons[j]]

            for x in Beacons[i]:
                for y in t:
                    delta = tuple(yi - xi for xi, yi in zip(x, y))
                    t2 = [tuple(yi - di for yi, di in zip(y, delta))
                          for y in t]
                    s2 = set(t2)
                    ss = s1 & s2
                    if len(ss) >= 12:
                        Beacons[j] = t2
                        scanner_poses[j] = delta
                        return True

    return False


last = 0
fixed = set([0])
free = set(range(1, n))
for _ in range(n - 1):
    found = -1

    for i in free:
        for j in fixed:
            if overlapping(j, i):
                found = i
                break
        if found != -1:
            break

    fixed.add(found)
    free.remove(found)

print(max(sum(abs(x - y) for x, y in zip(a, b))
      for a in scanner_poses for b in scanner_poses))
