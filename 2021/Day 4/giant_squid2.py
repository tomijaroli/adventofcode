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
remaining = set(range(len(winner_board_combinations)))
for number in numbers:
    called.add(number)
    for rem in set(remaining):
        board = winner_board_combinations[rem]
        if any(line.issubset(called) for line in board):
            remaining.remove(rem)
            if len(remaining) == 0:
                print(sum(set.union(*board) - set(called)) * number)
