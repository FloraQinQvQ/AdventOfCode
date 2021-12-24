import heapq

f = open('2021/inputs/15.txt')
lines = f.read().splitlines()

row = len(lines)
col = len(lines[0])
matrix = [[0 for _ in range(row)] for _ in range(col)]

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        matrix[i][j] = int(x)

cost_map = {}
pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()

while len(pq) > 0:
    cost, i, j = heapq.heappop(pq)

    if (i, j) in visited:
        continue

    visited.add((i, j))
    cost_map[(i, j)] = cost

    if i == row - 1 and j == col - 1:
        break

    for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        ii = i + di
        jj = j + dj
        if ii < 0 or jj < 0 or ii >= row or jj >= col:
            continue
        heapq.heappush(pq, (cost + matrix[ii][jj], ii, jj))

print(cost_map)
print(cost_map[(row-1, col-1)])
