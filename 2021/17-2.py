f = open('2021/inputs/17.txt')
line = f.read().splitlines()[0]
data = line.split('target area: x=')[1].split(', y=')

# target area: x= 20..30, y=-10..-5
x_range = (int(data[0].split('..')[0]), int(data[0].split('..')[1]))

y_range = (int(data[1].split('..')[0]), int(data[1].split('..')[1]))


target_range = (x_range, y_range)


def calculate_next_velocity(pos, vel):
    new_pos = [0, 0]
    new_vel = [0, 0]

    new_pos[0] = pos[0] + vel[0]
    new_pos[1] = pos[1] + vel[1]

    new_vel[1] = vel[1] - 1

    if vel[0] > 0:
        new_vel[0] = vel[0] - 1
    elif vel[0] < 0:
        new_vel[0] = vel[1] + 1

    return new_pos, new_vel


def is_within_target_range(pos):
    global target_range
    return target_range[0][0] <= pos[0] <= target_range[0][1] and target_range[1][0] <= pos[1] <= target_range[1][1]


def is_past_target_range(pos, vel):
    global target_range

    if vel[1] < 0 and target_range[1][0] > pos[1]:
        return True

    if vel[0] < 0 and target_range[0][0] > pos[0]:
        return True

    if vel[0] > 0 and target_range[0][1] < pos[0]:
        return True

    return False


def is_hit_target_range(vel):
    global target_range

    pos = (0, 0)
    max_y = 0

    while not is_past_target_range(pos, vel):
        max_y = max(max_y, pos[1])

        if is_within_target_range(pos):
            return True, max_y
        pos, vel = calculate_next_velocity(pos, vel)

    return False, None


y_vel_max = max([abs(target_range[1][0]), abs(target_range[1][1])])
y_tmp = y_vel_max

ans = 0

while y_tmp >= target_range[1][0]:
    for x_vel in range(-1000, 1000):
        works, max_y = is_hit_target_range((x_vel, y_tmp))
        if works:
            ans += 1
    # print(x_vel, y_tmp)
    y_tmp -= 1

print(ans)
