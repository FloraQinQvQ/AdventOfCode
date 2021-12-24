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


def get_all(str):
    if str == '' or int(str, 2) == 0:
        return 0

    version = int(str[0:3], 2)
    typeid = int(str[3:6], 2)

    # literal value:
    if typeid == 4:
        start = 6
        num_string = ''
        end = False

        while not end:
            if str[start] == '0':
                end = True
            num_string += str[start+1: start+5]
            start += 5

        return version + get_all(str[start:])

    # operator packet
    operator = str[6]
    if operator == '0':
        num_bits = int(str[7:22], 2)
        return version + get_all(str[22:22+num_bits]) + get_all(str[22+num_bits:])
    else:
        return version + get_all(str[18:])


print(get_all(outermost_packet))
