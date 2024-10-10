
# ฟังก์ชันหลักสำหรับตรวจสอบว่าราชาอยู่ในสถานการณ์รุกหรือไม่
def is_king_in_check(board):
    king_position = find_king(board)
    
    if king_position is None:
        print("Error: King not found")
        return
    
    # ตรวจสอบตัวหมากแต่ละตัวบนกระดาน
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            
            if piece == 'P':  # เบี้ย
                if is_pawn_attacking(row, col, king_position, board):
                    print("Success")
                    return
            elif piece == 'B':  # บิชอป
                if is_bishop_attacking(row, col, king_position, board):
                    print("Success")
                    return
            elif piece == 'R':  # เรือ
                if is_rook_attacking(row, col, king_position, board):
                    print("Success")
                    return
            elif piece == 'Q':  # ราชินี
                if is_queen_attacking(row, col, king_position, board):
                    print("Success")
                    return
    
    # ถ้าไม่มีตัวหมากไหนโจมตีราชาได้
    print("Fail")

# ฟังก์ชันค้นหาตำแหน่งของราชาบนกระดาน
def find_king(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                return (row, col)
    return None  # กรณีที่ไม่มีราชา (ไม่ควรเกิดขึ้น)

# ฟังก์ชันตรวจสอบการโจมตีจากเบี้ย
def is_pawn_attacking(pawn_row, pawn_col, king_position, board):
    king_row, king_col = king_position
    # ตรวจสอบว่าราชาอยู่ในทิศทางที่เบี้ยโจมตี (ทแยงมุมหนึ่งช่องไปข้างหน้า)
    # สมมติว่าเป็นเบี้ยขาวที่เดินขึ้น
    return (pawn_row - 1, pawn_col - 1) == king_position or (pawn_row - 1, pawn_col + 1) == king_position

# ฟังก์ชันตรวจสอบการโจมตีจากบิชอป
def is_bishop_attacking(bishop_row, bishop_col, king_position, board):
    return check_diagonal(bishop_row, bishop_col, king_position, board)

# ฟังก์ชันตรวจสอบการโจมตีจากเรือ
def is_rook_attacking(rook_row, rook_col, king_position, board):
    return check_straight(rook_row, rook_col, king_position, board)

# ฟังก์ชันตรวจสอบการโจมตีจากราชินี (ทั้งทแยงและตรง)
def is_queen_attacking(queen_row, queen_col, king_position, board):
    return check_diagonal(queen_row, queen_col, king_position, board) or check_straight(queen_row, queen_col, king_position, board)

# ฟังก์ชันตรวจสอบการโจมตีในแนวทแยง (สำหรับบิชอปและราชินี)
def check_diagonal(start_row, start_col, king_position, board):
    king_row, king_col = king_position
    # ตรวจสอบทุกแนวทแยง (ซ้ายบน, ขวาบน, ซ้ายล่าง, ขวาล่าง)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        row, col = start_row, start_col
        while 0 <= row < len(board) and 0 <= col < len(board):
            row += direction[0]
            col += direction[1]
            if (row, col) == king_position:
                return True
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != '.':  # เจอหมากขวางหรือออกนอกกระดาน
                break
    return False

# ฟังก์ชันตรวจสอบการโจมตีในแนวตรง (สำหรับเรือและราชินี)
def check_straight(start_row, start_col, king_position, board):
    king_row, king_col = king_position
    # ตรวจสอบแนวตั้งและแนวนอน
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        row, col = start_row, start_col
        while 0 <= row < len(board) and 0 <= col < len(board):
            row += direction[0]
            col += direction[1]
            if (row, col) == king_position:
                return True
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != '.':  # เจอหมากขวางหรือออกนอกกระดาน
                break
    return False
