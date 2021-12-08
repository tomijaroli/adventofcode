with open('input') as file:
    bingo = file.read()

numbers, *bingo_boards = bingo.split('\n\n')
numbers = map(int, numbers.split(','))

winner_board_combinations = []
for bingo_board in bingo_boards:
    bingo_board = bingo_board.split('\n')
    current_board = [list(map(int, line.split())) for line in bingo_board]
    current_board += list(map(list, zip(*current_board)))
    winner_board_combinations.append(list(map(set, current_board)))

called = set()
for number in numbers:
    called.add(number)
    for board in winner_board_combinations:
        if any(line.issubset(called) for line in board):
            print(sum(set.union(*board) - set(called)) * number)
            break
    else:
        continue
    break
