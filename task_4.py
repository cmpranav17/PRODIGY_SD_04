import tkinter as tk
from tkinter import messagebox

# Function to check if a number is valid in a given position
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# Function to solve the Sudoku puzzle
def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Function to find an empty space on the board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to print the Sudoku board in the console (for debugging)
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# GUI Implementation
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0]*9 for _ in range(9)]  # Initialize an empty board
        self.entries = []

        # Create 9x9 grid of entry widgets
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(root, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Solve button
        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9, pady=20)

    def solve(self):
        try:
            # Get values from the grid
            for i in range(9):
                for j in range(9):
                    value = self.entries[i][j].get()
                    if value.isdigit():
                        self.board[i][j] = int(value)
                    else:
                        self.board[i][j] = 0

            # Solve the Sudoku
            if solve_sudoku(self.board):
                self.update_board()
                messagebox.showinfo("Sudoku Solver", "Sudoku Solved!")
            else:
                messagebox.showerror("Sudoku Solver", "No solution exists!")

        except ValueError:
            messagebox.showerror("Sudoku Solver", "Please enter valid numbers.")

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
