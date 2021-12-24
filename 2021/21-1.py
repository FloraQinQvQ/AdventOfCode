f = open('2021/inputs/21-sample.txt')
lines = f.read().splitlines()

players = []
scores = []
for idx, line in enumerate(lines):
    players.append(int(line.split(f'Player {idx + 1} starting position: ')[1]))
    scores.append(0)

die = 1


def roll():
    global die
    tmp = die
    die = (die - 1) % 100 + 1

    return tmp


def gaming():
    turns = 0
    while True:
        who = turns % 2
        players[who] = (players[who] + roll() + roll() + roll() - 1) % 10 + 1
        scores[who] += players[who]
        turns += 1
        if scores[who] >= 1000:
            return 3 * turns, scores


times, results = gaming()

print(times * min(results))
