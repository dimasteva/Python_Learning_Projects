import random

score = 0

def print_score():
    print()
    global score
    print("Score: " + str(score))

def print_board(board):
    for row in board:
        print(row)
    print()

def add_to_score(points):
    global score
    score += points

def contains_zero(board):
    return any(0 in row for row in board)

def generate_random_cell(board):
    if not contains_zero(board):
        return False

    while(True):
        column = random.randint(0, 3)
        row = random.randint(0, 3)
        if board[row][column] == 0:
            board[row][column] = 2 if random.random() < 0.9 else 4
            return True

def rotate_left(board):
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in range(n):
        for j in range(n // 2):
            board[j][i], board[n - j - 1][i] = board[n - j - 1][i], board[j][i]

def rotate_right(board):
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in range(n):
        board[i] = board[i][::-1]

def reverse_rows(board):
    for i in range(len(board)):
        board[i] = board[i][::-1]

def move_left(board):
    for i in range(len(board)):
        new_row = [num for num in board[i] if num != 0]
        new_row.extend([0] * (len(board[i]) - len(new_row)))
        board[i] = new_row

    for i in range(len(board)):
        for j in range (len(board[i]) - 1):
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                add_to_score(board[i][j])
                board[i][j + 1] = 0

                new_row = [num for num in board[i] if num != 0]
                new_row.extend([0] * (len(board[i]) - len(new_row)))
                board[i] = new_row          

def move_right(board):
    reverse_rows(board)
    move_left(board)
    reverse_rows(board)

def move_up(board):
    rotate_left(board)
    move_left(board)
    rotate_right(board)

def move_down(board):
    rotate_right(board)
    move_left(board)
    rotate_left(board)


def main():
    print("Commands are as follows:\n"
      "'W' or 'w' : Move Up\n"
      "'S' or 's' : Move Down\n"
      "'A' or 'a' : Move Left\n"
      "'D' or 'd' : Move Right")
    size = 4
    board = [[0 for _ in range(size)] for _ in range(size)]
    generate_random_cell(board)
    print_score()
    print_board(board)
    while(True):
        print("Press the command:", end = " ")
        move = input()
        move = move.lower()
        if move != 'a' and move != 'w' and move != 's' and move != 'd':
            print("Invalid command!")
            continue
        if move == 'a':
            move_left(board)
        elif move == 'w':
            move_up(board)
        elif move == 's':
            move_down(board)
        elif move == 'd':
            move_right(board)
        if not generate_random_cell(board):
            print()
            print("Game over, your score is: " + str(score))
            return
        print_score()
        print_board(board)



if __name__ == "__main__":
    main()