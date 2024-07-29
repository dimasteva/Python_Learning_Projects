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