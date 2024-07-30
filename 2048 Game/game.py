import random

class Game:

    def __init__(self):
        self.size = 4
        self.score = 0
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def return_score(self):
        return self.score

    def return_board(self):
        return self.board

    def add_to_score(self, points):
        self.score += points

    def contains_zero(self):
        return any(0 in row for row in self.board)

    def generate_random_cell(self):
        if not self.contains_zero():
            return False

        while(True):
            column = random.randint(0, 3)
            row = random.randint(0, 3)
            if self.board[row][column] == 0:
                self.board[row][column] = 2 if random.random() < 0.9 else 4
                return True

    def check_if_move_left_is_playable(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if (self.board[i][j] == 0 and self.board[i][j + 1]) or (self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0) != 0:
                    return True
        
        return False
    
    def check_if_move_right_is_playable(self):
        self.reverse_rows()
        if self.check_if_move_left_is_playable():
            self.reverse_rows()
            return True
        self.reverse_rows()
        return False
    
    def check_if_move_up_is_playable(self):
        self.rotate_left()
        if self.check_if_move_left_is_playable():
            self.rotate_right()
            return True
        self.rotate_right()
        return False
    

    def check_if_move_down_is_playable(self):
        self.rotate_right()
        if self.check_if_move_left_is_playable():
            self.rotate_left()
            return True
        self.rotate_left()
        return False
    
    def in_bounds(self, x, y):
        return (x >= 0 and y >= 0 and x < self.size and y < self.size)

    def check_possible_moves(self):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for x in range(self.size):
            for y in range(self.size):
                for i in range(len(dx)):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if self.in_bounds(xx, yy) and self.board[xx][yy] == self.board[x][y]:
                        return True
        return False

    def rotate_left(self):
        n = len(self.board)

        for i in range(n):
            for j in range(i + 1, n):
                self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]

        for i in range(n):
            for j in range(n // 2):
                self.board[j][i], self.board[n - j - 1][i] = self.board[n - j - 1][i], self.board[j][i]

    def rotate_right(self):
        n = len(self.board)

        for i in range(n):
            for j in range(i + 1, n):
                self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]

        for i in range(n):
            self.board[i] = self.board[i][::-1]

    def reverse_rows(self):
        for i in range(len(self.board)):
            self.board[i] = self.board[i][::-1]

    def move_left(self):
        for i in range(len(self.board)):
            new_row = [num for num in self.board[i] if num != 0]
            new_row.extend([0] * (len(self.board[i]) - len(new_row)))
            self.board[i] = new_row

        for i in range(len(self.board)):
            for j in range (len(self.board[i]) - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    self.board[i][j] *= 2
                    self.add_to_score(self.board[i][j])
                    self.board[i][j + 1] = 0

                    new_row = [num for num in self.board[i] if num != 0]
                    new_row.extend([0] * (len(self.board[i]) - len(new_row)))
                    self.board[i] = new_row          

    def move_right(self):
        self.reverse_rows()
        self.move_left()
        self.reverse_rows()

    def move_up(self):
        self.rotate_left()
        self.move_left()
        self.rotate_right()

    def move_down(self):
        self.rotate_right()
        self.move_left()
        self.rotate_left()