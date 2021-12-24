f = open('2021/inputs/16.txt')
lines = f.read().splitlines()

binary_mapping = {'0': '0000',
                  '1': '0001',
                  '2': '0010',
                  '3': '0011',
                  '4': '0100',
                  '5': '0101',
                  '6': '0110',
                  '7': '0111',
                  '8': '1000',
                  '9': '1001',
                  'A': '1010',
                  'B': '1011',
                  'C': '1100',
                  'D': '1101',
                  'E': '1110',
                  'F': '1111'}

line = lines[0].strip()
outermost_packet = ''.join([binary_mapping[x] for x in line])


def operate(typeid, subpackets):
    if typeid == 0:
        return sum(subpackets)

    if typeid == 1:
        tmp = 1
        for x in subpackets:
            tmp *= x
        return tmp

    if typeid == 2:
        return min(subpackets)

    if typeid == 3:
        return max(subpackets)

    if typeid == 5:
        return int(subpackets[0] > subpackets[1])

    if typeid == 6:
        return int(subpackets[0] < subpackets[1])

    if typeid == 7:
        return int(subpackets[0] == subpackets[1])


def get_all(start, end=-1, remaining=-1):
    if remaining == 0 or start == end or (start > len(outermost_packet) - 4):
        return None, None

    version = int(outermost_packet[start:start+3], 2)
    typeid = int(outermost_packet[start+3:start+6], 2)

    # literal value:
    if typeid == 4:
        start += 6
        num_string = ''
        endyet = False

        while not endyet:
            if outermost_packet[start] == '0':
                endyet = True
            num_string += outermost_packet[start+1: start+5]
            start += 5

        value = int(num_string, 2)
        return value, start

    # operator packet
    sub_packets = []
    next_start = None

    operator = outermost_packet[start + 6]
    if operator == '0':
        num_bits = int(outermost_packet[start+7: start+22], 2)
        end = start + 22 + num_bits

        index = start + 22
        prev_index = None
        while index != None:
            prev_index = index
            x, index = get_all(index, end)
            sub_packets.append(x)
        sub_packets = sub_packets[:-1]
        next_start = prev_index
    else:
        num_packs = int(outermost_packet[start+7: start+18], 2)
        index = start + 18
        while num_packs > 0:
            x, index = get_all(index, remaining=num_packs)
            num_packs -= 1
            sub_packets.append(x)
        next_start = index

    return operate(typeid, sub_packets), next_start


print(get_all(0))
