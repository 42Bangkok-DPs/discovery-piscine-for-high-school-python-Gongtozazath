# main.py

from checkmate import checkmate #นำเข้าฟังก์ชัน checkmate จาก checkmate.py


def main(): #ใช้ฟังก์ชัน main เพื่อกำหนดกระดานหมาก R=Rook Q=Queen K=King P=Pawn
    board = """\
...Q
....
..K.
....\
"""
    checkmate(board) #ใช้ฟังก์ชัน checkmate เพื่อเช็คตำแหน่งหมาก

if __name__ == "__main__": #ใช้นำข้อมูลจาก checkmate.py มาใช้ใน main.py เพิ่อแสดงผลลัพธ์
    main()
