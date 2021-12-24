from functools import lru_cache

f = open('2021/inputs/21.txt')
lines = f.read().splitlines()

players = []
scores = []
for idx, line in enumerate(lines):
    players.append(int(line.split(f'Player {idx + 1} starting position: ')[1]))
    scores.append(0)

freqs = {3: 1,  # (1, 1, 1)
         4: 3,  # (1, 1, 2) (2, 1, 1) (1, 2, 1)
         5: 6,  # (1, 2, 2) * 3 + (1, 1, 3) * 3
         6: 7,  # (1, 2, 3) * 6 + (2, 2, 2)
         7: 6,  # (1, 3, 3) * 3 + (3, 2, 2) * 3
         8: 3,  # (2, 3, 3) * 3
         9: 1}  # (3, 3, 3)


@lru_cache(None)
def gaming(turn, player0, player1, score0, score1):
    tmp_players = [player0, player1]
    tmp_scores = [score0, score1]
    if tmp_scores[0] >= 21:
        return [1, 0]
    elif tmp_scores[1] >= 21:
        return [0, 1]

    ans = [0, 0]
    who = turn % 2

    for val, ways in freqs.items():
        cur_player_prev = tmp_players[who]
        added = (tmp_players[who] + val - 1) % 10 + 1

        tmp_players[who] = added
        tmp_scores[who] += added
        now = gaming(
            turn + 1, tmp_players[0], tmp_players[1], tmp_scores[0], tmp_scores[1])
        ans[0] += ways * now[0]
        ans[1] += ways * now[1]

        tmp_scores[who] -= added
        tmp_players[who] = cur_player_prev

    return ans


print(gaming(0, players[0], players[1], scores[0], scores[1]))
