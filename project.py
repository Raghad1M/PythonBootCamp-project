import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def on_button_click(self, row, col):
        button_index = 3 * row + col
        if self.board[button_index] == " ":
            self.board[button_index] = self.current_player
            self.buttons[button_index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.root.quit()
            elif " " not in self.board:
                messagebox.showinfo("Draw!", "It's a draw!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
