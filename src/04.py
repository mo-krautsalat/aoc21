def calculate_score(number, board):
    sum_unmarked = 0
    for r, row in enumerate(numbers):
        for c, column in enumerate(row):
            if not board[r][c]:
                sum_unmarked += column

    print(f"Sum of unmarked numbers: {sum_unmarked}")
    print(f"FINAL SCORE: {sum_unmarked * number}")


def parse_board(file, boards):
    for i, line in enumerate(file):
        if line == "\n" and i > 5:
            break
        else:
            line = line.strip().replace(" ",",")
            numbers.append([int(num) for num in line.split(",") if num])

    if len(numbers) > 0:
        if len(numbers) > 5:
            del numbers[0]
        boards.append(board)

    print(f"Rows: {numbers}, length: {len(numbers)}")


with open("../res/bingo") as f:
    win_numbers = [int(n) for n in f.readline().split(",")]
    board = [[0 for x in range(5)] for y in range(5)]
    state_boards = list()
    print(f"Empty example board: {board}")
    numbers = list()
    winning_number = 0
    parse_board(f, state_boards)
    print(f"Number of state boards: {state_boards}")

    for w, win_num in enumerate(win_numbers):
        for r, row in enumerate(numbers):
            for c, column in enumerate(row):
                #print(c, win_num)
                if column == win_num:
                    state_boards[0][r][c] = 1
                    #print(board[r])
                    if all(board[r]):
                        winning_number = win_num
                        break
            else:
                continue
            break
        else:
            continue
        break

    print(f"Winning number was: {winning_number}")
    calculate_score(winning_number, board)

