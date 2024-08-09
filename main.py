import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
    
    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, sticky="nsew")
                self.buttons[row][col] = button
        
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "" and not self.check_winner():
            button["text"] = self.current_player
            if self.check_winner():
                self.show_winner()
            elif self.is_draw():
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for i in range(3):
            if (self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "" or
                self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != ""):
                return True
        
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "" or
            self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != ""):
            return True
        
        return False
    
    def is_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True
    
    def show_winner(self):
        messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
        self.reset_game()
    
    def show_draw(self):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        self.reset_game()
    
    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
