import tkinter as tk #tkinter ใช้สร้าง gui
from tkinter import messagebox #ใช้แสดงข้อความตอนเกมจบ
import chess #module ใช้แก้ตารางหมาก

#กำหนดตัวหมากให้พิมพ์ใหญ่เป็นหมากขาว พิมพ์เล็กเป็นหมากดำ
piece_symbols = {
    'P': 'P', 'N': 'N', 'B': 'B', 'R': 'R',
    'Q': 'Q', 'K': 'K',
    'p': 'p', 'n': 'n', 'b': 'b', 'r': 'r',
    'q': 'q', 'k': 'k'
}

class ChessGUI: #สร้างคลาสเพื่อจัดการ gui 
    def __init__(self, root):
        self.root = root #หน้าต่างหลักของ gui
        self.root.title("Chess Game") #ข้อความบน gui 
        self.board = chess.Board() #เรียกค่าในตารางบอร์ด
        self.selected_square = None #เก็บตำแหน่งของสี่เหลี่ยมที่เลือก
        self.buttons = {} #เก็บค่าปุ่มแต่ละตำแหน่งบนบอร์ด
        self.create_board() #สร้างบอร์ดหมาก

    def create_board(self): #สร้างตาราง 8 x 8
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row) #แปลงพิกัดของตารางให้ซ้ายล่างเป็น 0
                piece = self.board.piece_at(square) #ดึงค่าของตัวหมาก
                color = 'white' if (row + col) % 2 == 0 else 'gray' #สลับสีของบอร์ด
                btn = tk.Button(self.root, text=piece_symbols.get(piece.symbol(), '') if piece else '', #สร้างปุ่มในสี่เหลี่ยมแต่ละช่อง
                                font=('Helvetica', 20, 'bold'),
                                bg=color,
                                fg='black' if piece and piece.symbol().isupper() else 'red',
                                width=4, height=2,
                                command=lambda s=square: self.on_square_click(s)) #ฟังก์ชันที่จะถูกเรียกเมื่อกดปุ่ม
                btn.grid(row=row, column=col)
                self.buttons[square] = btn #เก็บปุ่มไว้ใน self.buttons เพื่อใช้งานต่อไป

    def on_square_click(self, square):
        if self.selected_square is None: #ถ้า self.selected_square เป็น None แสดงว่ายังไม่มีการเลือกสี่เหลี่ยม
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn: #เช็คตำแหน่งที่คลิกว่ามีหมากมั้ย
                self.selected_square = square #ถ้ามีหมากในสี่เหลี่ยมจะไฮไลท์ช้่องสี่เหลี่ยม
                self.highlight_square(square)
        else:
            move = chess.Move(self.selected_square, square) #เช็คการเคลื่อนที่ของหมาก
            if move in self.board.legal_moves: #ถ้าเคลื่อนถูกหมากจะเปลี่ยนตำแหน่ง
                self.board.push(move) #คลิกเปลี่ยนตำแหน่งของหมาก
                self.update_board() #ถ้าเคลื่อนถูกหมากจะเปลี่ยนตำแหน่ง
                self.selected_square = None
                if self.board.is_checkmate(): #เช็คผลเมื่อจบเกม
                    messagebox.showinfo("Game Over", "Checkmate! " + ("White" if self.board.turn == chess.BLACK else "Black") + " wins.")
                elif self.board.is_stalemate():
                    messagebox.showinfo("Game Over", "Stalemate!")
            else:
                self.selected_square = None #ถ้าเคลื่อนหมากผิดก็จะแสดงผลเหมือนเดิม
                self.update_board()

    def highlight_square(self, square): #ไฮไลท์ช่องที่มีหมากเมื่อคลิกช่องนั้น
        for sq, btn in self.buttons.items():
            row, col = chess.square_rank(sq), chess.square_file(sq)
            color = 'white' if (7 - row + col) % 2 == 0 else 'gray'
            btn.configure(bg=color)
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
            row, col = chess.square_rank(square), chess.square_file(square)
            color = 'white' if (7 - row + col) % 2 == 0 else 'gray'
            btn.configure(bg=color)

def main():
    root = tk.Tk() #สร้างหน้าต่าง
    gui = ChessGUI(root) #แสดงบอร์ดหมาก
    root.mainloop() #เริ่มต้นลูปหลักของ tkinter เพื่อรอเคลื่อนหมาก

if __name__ == "__main__": #ตรวจสอบว่าไฟล์นี้ถูกเรียกใช้โดยตรง และไม่ใช่ถูกนำเข้าเป็นโมดูลจากไฟล์อื่น
    main()
