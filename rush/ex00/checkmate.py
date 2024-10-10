def check(board):
    n = len(board)  # Size of the board (n x n)
    
    # Find the position of the King ('K')
    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")  # If there's no King, return Fail
        return

    king_row, king_col = king_pos
    
    # Check if any piece threatens the King
    def is_rook_threat():
        # Check row and column for Rook ('R') or Queen ('Q')
        # Horizontal check (left and right of the king)
        for i in range(king_col - 1, -1, -1):
            if board[king_row][i] == 'R' or board[king_row][i] == 'Q':
                return True
            elif board[king_row][i] != '.':
                break  # Blocked by another piece
        
        for i in range(king_col + 1, n):
            if board[king_row][i] == 'R' or board[king_row][i] == 'Q':
                return True
            elif board[king_row][i] != '.':
                break  # Blocked by another piece

        # Vertical check (above and below the king)
        for i in range(king_row - 1, -1, -1):
            if board[i][king_col] == 'R' or board[i][king_col] == 'Q':
                return True
            elif board[i][king_col] != '.':
                break  # Blocked by another piece
        
        for i in range(king_row + 1, n):
            if board[i][king_col] == 'R' or board[i][king_col] == 'Q':
                return True
            elif board[i][king_col] != '.':
                break  # Blocked by another piece
        
        return False

    def is_bishop_threat():
        # Check diagonals for Bishop ('B') or Queen ('Q')
        # Top-left diagonal
        i, j = king_row - 1, king_col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            elif board[i][j] != '.':
                break
            i -= 1
            j -= 1
        
        # Top-right diagonal
        i, j = king_row - 1, king_col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            elif board[i][j] != '.':
                break
            i -= 1
            j += 1

        # Bottom-left diagonal
        i, j = king_row + 1, king_col - 1
        while i < n and j >= 0:
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            elif board[i][j] != '.':
                break
            i += 1
            j -= 1
        
        # Bottom-right diagonal
        i, j = king_row + 1, king_col + 1
        while i < n and j < n:
            if board[i][j] == 'B' or board[i][j] == 'Q':
                return True
            elif board[i][j] != '.':
                break
            i += 1
            j += 1
        
        return False

    def is_pawn_threat():
        # Check if a pawn ('P') can attack the King
        # Pawns can only capture diagonally forward (from the enemy's perspective)
        if king_row > 0:
            if king_col > 0 and board[king_row - 1][king_col - 1] == 'P':
                return True
            if king_col < n - 1 and board[king_row - 1][king_col + 1] == 'P':
                return True
        return False

    if is_rook_threat() or is_bishop_threat() or is_pawn_threat():
        print("Success")
    else:
        print("Fail")

def main():
    board = [
        ".... ",
        ".QK.",
        "....",
        "...."
    ]
    check(board)

if __name__ == "__main__":
    main()
