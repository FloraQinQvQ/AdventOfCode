f = open('4.txt')
content = f.read()

contents = content.splitlines()
contents = [content for content in contents if content != '']


def column(matrix, i):
    return [row[i] for row in matrix]


inputs = contents[0].split(',')
boards_lists = contents[1:]

boards = [[[0 for _ in range(5)] for _ in range(5)]
          for _ in range(int(len(boards_lists)/5))]
row_count = 0

for idx, boards_list in enumerate(boards_lists):
    row = boards_list.split(' ')
    num = int(idx/5)
    row = [ele for ele in row if ele.strip() != '']
    for idx, ele in enumerate(row):
        boards[num][row_count][idx] = ele.strip()
    if row_count < 4:
        row_count += 1
    else:
        row_count = 0

combinations = []
for board in boards:
    for i in range(5):
        combinations.append(board[i])
        combinations.append(column(board, i))
max_indexes = []
combines = []
for combi in combinations:
    if set(combi).issubset(set(inputs)):
        max_index_per_combi = max([inputs.index(element)for element in combi])
        max_indexes.append(max_index_per_combi)
        combines.append(combi)

zipped_lists = zip(max_indexes, combines)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [list(tuple) for tuple in tuples]

board_options = [i for i in range(int(len(boards_lists)/5))]
for idx, list in enumerate(list1):
    target_row = list2[idx]
    if len(board_options) != 1:
        try:
            board_options.remove(int(combinations.index(target_row)/10))
        except ValueError:
            pass
    else:
        if int(combinations.index(target_row)/10) != board_options[0]:
            continue
        else:
            print(int(combinations.index(target_row)/10))
            print(target_row)
            break

target_board = boards[board_options[0]]
included_inputs = inputs[0:list1[idx]+1]
sum = 0
for i in range(5):
    for j in range(5):
        if target_board[i][j] in included_inputs:
            continue
        else:
            sum += int(target_board[i][j])
print(sum * int(inputs[list1[idx]]))
