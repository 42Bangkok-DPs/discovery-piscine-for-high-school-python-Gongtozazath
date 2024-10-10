import tkinter as tk
from tkinter import messagebox
import chess

# Mapping of chess pieces to their corresponding letters
piece_symbols = {
    'P': 'P', 'N': 'N', 'B': 'B', 'R': 'R','Q': 'Q', 'K': 'K',
    'p': 'p', 'n': 'n', 'b': 'b', 'r': 'r','q': 'q', 'k': 'k'
}

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.selected_square = None
        self.buttons = {}
        self.create_board()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                piece = self.board.piece_at(square)
                color = 'white' if (row + col) % 2 == 0 else 'gray'
                btn = tk.Button(self.root, text=piece_symbols.get(piece.symbol(), '') if piece else '',
                                font=('Helvetica', 20, 'bold'),
                                bg=color,
                                fg='black' if piece and piece.symbol().isupper() else 'red',
                                width=4, height=2,
                                command=lambda s=square: self.on_square_click(s))
                btn.grid(row=row, column=col)
                self.buttons[square] = btn

    def on_square_click(self, square):
        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
                self.highlight_square(square)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board()
                self.selected_square = None
                if self.board.is_checkmate():
                    messagebox.showinfo("Game Over", "Checkmate! " + ("White" if self.board.turn == chess.BLACK else "Black") + " wins.")
                elif self.board.is_stalemate():
                    messagebox.showinfo("Game Over", "Stalemate!")
            else:
                # Invalid move, deselect
                self.selected_square = None
                self.update_board()

    def highlight_square(self, square):
        # Reset all buttons to default colors
        for sq, btn in self.buttons.items():
            row, col = chess.square_rank(sq), chess.square_file(sq)
            color = 'white' if (7 - row + col) % 2 == 0 else 'gray'
            btn.configure(bg=color)
        # Highlight the selected square
        btn = self.buttons[square]
        btn.configure(bg='yellow')

    def update_board(self):
        for square, btn in self.buttons.items():
            piece = self.board.piece_at(square)
            btn.configure(text=piece_symbols.get(piece.symbol(), '') if piece else '')
            if piece:
                btn.configure(fg='black' if piece.symbol().isupper() else 'red')
            else:
                btn.configure(fg='black')
            # Reset colors
            row, col = chess.square_rank(square), chess.square_file(square)
            color = 'white' if (7 - row + col) % 2 == 0 else 'gray'
            btn.configure(bg=color)

def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
