import tkinter as tk
from tkinter import messagebox
from game import Game

class GameUI:
    def __init__(self, window):
        self.window = window
        self.grid_size = 4
        self.cell_size = 100
        self.frames = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.max_score = 0
        self.create_grid()
        self.start_new_game()

        self.window.bind('<KeyPress>', self.handle_key_press)

    def create_grid(self):
        # Create score frame
        self.score_frame = tk.Frame(self.window)
        self.score_frame.grid(row=0, column=0, columnspan=self.grid_size, sticky="ew")
        
        # Score label
        self.score_label = tk.Label(self.score_frame, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(side=tk.RIGHT)

        # Max score label
        self.max_score_label = tk.Label(self.score_frame, text="Max Score: 0", font=("Arial", 16))
        self.max_score_label.pack(side=tk.LEFT)

        # Create grid cells
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = tk.Frame(self.window, width=self.cell_size, height=self.cell_size, bg='lightgray', borderwidth=2, relief="ridge")
                cell.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nsew")
                self.frames[row][col] = cell

        # Configure grid resizing
        for i in range(self.grid_size):
            self.window.grid_columnconfigure(i, weight=1)
            self.window.grid_rowconfigure(i + 1, weight=1)

    def get_cell_color(self, number):
        colors = {
            0: 'lightgray',  # Empty cell color
            2: '#eee4da',
            4: '#ede0c8',
            8: '#f2b179',
            16: '#f59563',
            32: '#f67c5f',
            64: '#f65e3b',
            128: '#edcf72',
            256: '#edcc61',
            512: '#edc850',
            1024: '#edc53f',
            2048: '#edc22e'
        }
        return colors.get(number, '#3c3a32')

    def update_board(self, board):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                number = board[row][col]
                if number == 0:
                    number = ""

                for widget in self.frames[row][col].winfo_children():
                    widget.destroy()

                cell_color = self.get_cell_color(number)
                label = tk.Label(self.frames[row][col], text=str(number), font=("Arial", 24), bg=cell_color, fg='black' if number != 0 else 'lightgray')
                label.pack(expand=True, fill='both')

    def update_score(self):
        score = self.game.return_score()
        self.score_label.config(text=f"Score: {score}")
        self.max_score_label.config(text=f"Max Score: {self.max_score}")

    def start_new_game(self):
        self.game = Game()
        self.game.generate_random_cell()
        self.update_board(self.game.board)
        self.update_score()

    def handle_key_press(self, event):
        if event.keysym == 'Up':
            if not self.game.check_if_move_up_is_playable():
                return
            self.game.move_up()
        elif event.keysym == 'Down':
            if not self.game.check_if_move_down_is_playable():
                return
            self.game.move_down()
        elif event.keysym == 'Left':
            if not self.game.check_if_move_left_is_playable():
                return
            self.game.move_left()
        elif event.keysym == 'Right':
            if not self.game.check_if_move_right_is_playable():
                return
            self.game.move_right()
        else:
            return

        self.game.generate_random_cell()
        self.update_board(self.game.board)
        self.update_score()

        if not self.game.contains_zero():
            if not self.game.check_possible_moves():
                score = self.game.return_score()
                if score > self.max_score:
                    self.max_score = score

                response = messagebox.askyesno("Game Over", f"Game is over, your score is: {score}\nDo you want to play again?")
                if response:
                    self.start_new_game()
                else:
                    self.window.destroy()

def main():
    window = tk.Tk()
    window.title("2048 Game")
    window.geometry("400x400")
    app = GameUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
