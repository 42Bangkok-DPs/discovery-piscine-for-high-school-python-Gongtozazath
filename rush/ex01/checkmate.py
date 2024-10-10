# checkmate.py

def checkmate(board):
    # Split the board into rows
    rows = board.strip().splitlines()
    size = len(rows)
    
    # Find the position of the King
    king_position = None
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_position = (r, c)
                break
        if king_position:
            break
    
    if not king_position:
        return "Error: No King found on the board."
    
    king_row, king_col = king_position
    
    # Check if the King is in check by any piece
    if is_under_attack(rows, king_row, king_col, size):
        print("Success")
    else:
        print("Fail")

def is_under_attack(board, king_row, king_col, size):
    # Check for Pawn attacks (P)
    if king_row < size - 1:  # Pawns can only attack from below
        if king_col > 0 and board[king_row + 1][king_col - 1] == 'P':
            return True
        if king_col < size - 1 and board[king_row + 1][king_col + 1] == 'P':
            return True
    
    # Check for Rook (R) and Queen (Q) in straight lines
    for d in [-1, 1]:  # Up and down
        for row in range(king_row + d, size if d == 1 else -1, d):
            if board[row][king_col] == 'R' or board[row][king_col] == 'Q':
                return True
            if board[row][king_col] != '.':
                break  # Stop if there's any piece
    
    for d in [-1, 1]:  # Left and right
        for col in range(king_col + d, size if d == 1 else -1, d):
            if board[king_row][col] == 'R' or board[king_row][col] == 'Q':
                return True
            if board[king_row][col] != '.':
                break
    
    # Check for Bishop (B) and Queen (Q) in diagonal lines
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            if board[row][col] == 'B' or board[row][col] == 'Q':
                return True
            if board[row][col] != '.':
                break  # Stop if there's any piece
            row += dr
            col += dc
    
    return False
