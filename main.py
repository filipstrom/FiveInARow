import tkinter as tk
from tkinter import messagebox
import bot
import numpy as np


class FiveInARowGame:
    def __init__(self, root, size=10, bot=False):
        self.root = root
        self.size = size
        self.bot = bot
        self.board = np.full([size, size], np.nan)
        self.current_player = 0
        self.dict = {0: "X", 1: "O"}

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 400 / self.size

        for row in range(self.size):
            for col in range(self.size):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = (col + 1) * cell_size
                y2 = (row + 1) * cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                if self.board[row][col] == 0:
                    x_center = (x1 + x2) / 2
                    y_center = (y1 + y2) / 2
                    self.canvas.create_text(
                        x_center,
                        y_center,
                        text="X",
                        font=("Arial", round(400 / self.size), "bold"),
                    )
                elif self.board[row][col] == 1:
                    self.canvas.create_oval(
                        x1, y1, x2, y2, outline="black", fill="white", width=2
                    )

    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        for dr, dc in directions:
            count = 1

            count += self.count_in_direction(row, col, dr, dc)
            count += self.count_in_direction(row, col, -dr, -dc)
            if count >= 5:
                return True
        return False

    def count_in_direction(self, row, col, dr, dc):
        count = 0
        row += dr
        col += dc
        while (
            0 <= row < self.size
            and 0 <= col < self.size
            and self.board[row][col] == self.current_player
        ):
            count += 1
            row += dr
            col += dc
        return count

    def on_click(self, event):
        x, y = event.x, event.y
        cell_size = 400 / self.size
        col = int(x / cell_size)
        row = int(y / cell_size)
        if np.isnan(self.board[row][col]):
            self.board[row][col] = self.current_player
            self.draw_board()

            if self.check_winner(row, col):
                messagebox.showinfo(
                    "Game Over", f"Player {self.dict[self.current_player]} wins!"
                )
                self.root.quit()
            else:
                self.current_player = 1 if self.current_player == 0 else 0

            if self.bot:
                row, col = bot.play_and_learn(self.board)
                print(row, col)
                self.board[row][col] = self.current_player
                self.draw_board()
                if self.check_winner(row, col):
                    messagebox.showinfo(
                        "Game Over", f"Player {self.dict[self.current_player]} wins!"
                    )
                    self.root.quit()
                else:
                    self.current_player = 1 if self.current_player == 0 else 0


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Five-in-a-Row")
    game = FiveInARowGame(root, bot=True)
    root.mainloop()
