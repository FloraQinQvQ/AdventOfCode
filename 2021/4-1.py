f = open('./2021/inputs/4.txt')
content = f.read()

contents = content.splitlines()
contents = [content for content in contents if content != '']


def column(matrix, i):
    return [row[i] for row in matrix]


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
max_index = len(inputs)
minimal_choices = None
for combi in combinations:
    if set(combi).issubset(set(inputs)):
        max_index_per_combi = max([inputs.index(element)for element in combi])
        if max_index_per_combi < max_index:
            max_index = max_index_per_combi
            minimal_choices = combi

board_number = int(combinations.index(minimal_choices)/10)

target_board = boards[board_number]
included_inputs = inputs[0:max_index+1]
sum = 0
for i in range(5):
    for j in range(5):
        if target_board[i][j] in included_inputs:
            continue
        else:
            sum += int(target_board[i][j])
print(sum * int(inputs[max_index]))
