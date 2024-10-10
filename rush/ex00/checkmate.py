# checkmate.py

def checkmate(board):
    rows = board.strip().splitlines() #แยกกระดานหมากเป็นบรรทัค
    size = len(rows) #กำหนดขนาดให้เป็นสี่เหลี่ยมจัตุรัส
    
    king_position = None #หาตำแหน่งของ King ในตารางถ้าเจอตำแหน่งจะหยุดหา
    for r in range(size):
        for c in range(size):
            if rows[r][c] == 'K':
                king_position = (r, c)
                break
        if king_position:
            break
    
    if not king_position: #ถ้าไม่เจอ King จะแสดงคำว่า Fail
        return print("Fail")
    
    king_row, king_col = king_position
    
    if is_under_attack(rows, king_row, king_col, size): #เช็คการโจมตีจากหมากชนิดต่างๆในฟังก์ชัน is_under_attack
        print("Success") #ถ้า King ถูกโจมตีจะแสดงคำว่า Success
    else:
        print("in check") #ถ้า King ไม่ถูกโจมตีจะแสดงคำว่า in check

def is_under_attack(board, king_row, king_col, size): 
    if king_row < size + 1: #เช็คตำแหน่งหมาก Pawn ที่โจมตีจากด้านบน
        if king_col > 0 and board[king_row + 1][king_col - 1] == 'P': #เช็คว่ามี King อยู่ในตำแหน่งแนวทแยงซ้ายขวามั้ย
            return True
        if king_col < size - 1 and board[king_row + 1][king_col + 1] == 'P':
            return True #ถ้ามี Pawn อยู่ในตำแหน่งตามเงื่อนไขแปลว่า King ถูกโจมตี

    for d in [-1, 1]: #เช็คตำแหน่งบนและล่างของหมาก Queen กับ Rook
        for row in range(king_row + d, size if d == 1 else -1, d):
            piece = board[row][king_col]
            if piece == 'R' or piece == 'Q': #เช็คว่ามี Queen กับ Rook และ King อยู่ในตำแหน่งบนและล่างมั้ย
                return True
            if piece != '.': #ถ้าเป็นช่องว่างจะไม่เช็ค
                break  
    
    for d in [-1, 1]: #เช็คตำแหน่งซ้ายขวาของหมาก Queen กับ Rook เหมือนเช็คบนและล่าง
        for col in range(king_col + d, size if d == 1 else -1, d):
            piece = board[king_row][col]
            if piece == 'R' or piece == 'Q':
                return True
            if piece != '.':
                break
    
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]: #เช็คแนวทแยง
        for distance in range(1, 4): #เช็คระยะของหมาก Bishop และ Queen กับ King
            row = king_row + dr * distance
            col = king_col + dc * distance
            if 0 <= row < size and 0 <= col < size:
                piece = board[row][col]
                if piece == 'B' or piece == 'Q': #ถ้าเจอ Bishop และ Queen ในระยะที่กำหนด
                    return True
                if piece != '.': #ถ้าเป็นช่องว่างจะไม่เช็ค
                    break 
            else:
                break  
    
    return False  #ถ้าไม่เจอหมากใดๆเลย
