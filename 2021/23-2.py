from copy import deepcopy

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
# room1 = ['B', 'D', 'D', 'A']
# room2 = ['C', 'C', 'B', 'D']
# room3 = ['B', 'B', 'A', 'C']
# room4 = ['D', 'A', 'C', 'A']

#############
#...........#
###D#C#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#A#A#B#
  #########
room1 = ['D', 'D', 'D', 'D']
room2 = ['C', 'C', 'B', 'A']
room3 = ['B', 'B', 'A', 'A']
room4 = ['C', 'A', 'C', 'B']

cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
start = ({'A': room1, 'B': room2, 'C': room3, 'D': room4}, ['.' for _ in range(11)])
DP = {}

def done(rooms, hallway):
    for k, v in rooms.items():
        for vv in v:
            if vv != k:
                return False

    return all(x == '.' for x in hallway)


def can_move_to(amphi, room):
    for c in room:
        if c != amphi and c != '.':
            return False
    return True


def can_move_from(amphi, room):
    for value in room:
        if value != amphi and value != '.':
            return True

    return False


def room_idx(amphi):
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[amphi]


def inbetween(i, amphi, idx):
    return (room_idx(amphi) < i < idx) or (idx < i < room_idx(amphi))


def no_blockage(amphi, idx, hallway):
    for i in range(len(hallway)):
        if inbetween(i, amphi, idx) and hallway[i] != '.':
            return False

    return True


def room_depth(room):
    for idx, c in reversed(list(enumerate(room))):
        if c == '.':
            return idx
    return None


def top_idx(values):
    for idx, c in enumerate(values):
        if c != '.':
            return idx
    return None


def calc_cost(state):
    rooms, hallway = state

    key = (tuple((k, tuple(v)) for k, v in rooms.items()), tuple(hallway))

    if done(rooms, hallway):
        return 0
    if key in DP:
        return DP[key]

    for idx, pos in enumerate(hallway):
        if pos in rooms and can_move_to(pos, rooms[pos]) and no_blockage(pos, idx, hallway):
            depth = room_depth(rooms[pos])

            dist = depth + 1 + abs(room_idx(pos) - idx)
            single_cost = cost[pos] * dist
            new_hallway = list(hallway)
            new_hallway[idx] = '.'

            new_rooms = deepcopy(rooms)
            new_rooms[pos][depth] = pos

            return single_cost + calc_cost((new_rooms, new_hallway))

    ans = int(1e9)
    for kind, values in rooms.items():
        if not can_move_from(kind, values):
            continue

        top_i = top_idx(values)
        if top_i is None:
            continue

        top = values[top_i]

        for idx in range(len(hallway)):
            if idx in [2, 4, 6, 8]:
                continue
            if hallway[idx] != '.':
                continue

            if no_blockage(kind, idx, hallway):
                dist = top_i + 1 + abs(room_idx(kind) - idx)
                new_hallway = list(hallway)
                assert new_hallway[idx] == '.'
                new_hallway[idx] = top
                new_rooms = deepcopy(rooms)
                assert new_rooms[kind][top_i] == top

                new_rooms[kind][top_i] = '.'
                ans = min(ans, cost[top] * dist + calc_cost((new_rooms, new_hallway)))

    DP[key] = ans
    return ans


print(calc_cost(start))

# print(calc_cost(start))

