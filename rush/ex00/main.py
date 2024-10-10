import itertools
WHITE = "white"
BLACK = "black"

class Game:
    def __init__(self):
        self.playersturn = BLACK
        self.message = "this is where prompts will go"
        self.gameboard = {}
        self.placePieces()
        print("chess program. enter moves in algebraic notation separated by space")
        self.main()

    def placePieces(self):
        # วางตำแหน่งเบี้ย
        for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
        
        # วางตำแหน่งหมากอื่น ๆ ยกเว้นม้า
        placers = [Rook,Bishop,Queen,King,Bishop,Rook]
        
        for i in range(0,8):
            self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
            self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
        placers.reverse()

    def main(self):
        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startpos,endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "could not find piece; index probably out of range"
                target = None
                
            if target:
                print("found "+str(target))
                if target.Color != self.playersturn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue
                if target.isValid(startpos,endpos,target.Color,self.gameboard):
                    self.message = "that is a valid move"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    self.isCheck()
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else: 
                        self.playersturn = BLACK
                else: 
                    self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
            else: 
                self.message = "there is no piece in that space"

    def isCheck(self):
        # หาตำแหน่งของกษัตริย์และตรวจสอบว่าถูกคุกคามหรือไม่
        kingDict = {}
        pieceDict = {BLACK : [], WHITE : []}
        for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            pieceDict[piece.Color].append((piece, position))
        # ตรวจสอบว่ากษัตริย์ฝ่ายขาวหรือดำอยู่ในเช็คหรือไม่
        if self.canSeeKing(kingDict[WHITE], pieceDict[BLACK]):
            self.message = "White player is in check"
        if self.canSeeKing(kingDict[BLACK], pieceDict[WHITE]):
            self.message = "Black player is in check"
        
    def canSeeKing(self, kingpos, piecelist):
        # ตรวจสอบว่าชิ้นหมากจากรายการสามารถโจมตีกษัตริย์ได้หรือไม่
        for piece, position in piecelist:
            if piece.isValid(position, kingpos, piece.Color, self.gameboard):
                return True
        return False
                
    def parseInput(self):
        try:
            a, b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            return (a, b)
        except:
            print("error decoding input. please try again")
            return((-1, -1), (-1, -1))

    def printBoard(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0,8):
            print("-"*32)
            print(chr(i+97),end="|")
            for j in range(0,8):
                item = self.gameboard.get((i,j)," ")
                print(str(item) + ' |', end=" ")
            print()
        print("-"*32)

class Piece:
    def __init__(self, color, name):
        self.name = name
        self.Color = color
    
    def isValid(self, startpos, endpos, Color, gameboard):
        return endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color)
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def availableMoves(self, x, y, gameboard, Color):
        print("ERROR: no movement for base class")

    def AdNauseum(self, x, y, gameboard, Color, intervals):
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.isInBounds(xtemp, ytemp):
                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break
                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def isInBounds(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def noConflict(self, gameboard, initialColor, x, y):
        return self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor)

chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

class Rook(Piece):
    def availableMoves(self, x, y, gameboard, Color = None):
        if Color is None:
            Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)
        
class Bishop(Piece):
    def availableMoves(self, x, y, gameboard, Color = None):
        if Color is None:
            Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)
        
class Queen(Piece):
    def availableMoves(self, x, y, gameboard, Color = None):
        if Color is None:
            Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals + chessDiagonals)

class King(Piece):
    def availableMoves(self, x, y, gameboard, Color = None):
        if Color is None:
            Color = self.Color
        return [(xx, yy) for xx, yy in kingList(x, y) if self.noConflict(gameboard, Color, xx, yy)]

class Pawn(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.Color = color
        self.direction = direction
    
    def availableMoves(self, x, y, gameboard, Color = None):
        if Color is None:
            Color = self.Color
        answers = []
        if (x+1, y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction):
            answers.append((x+1, y+self.direction))
        if (x-1, y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction):
            answers.append((x-1, y+self.direction))
        if (x, y+self.direction) not in gameboard:
            answers.append((x, y+self.direction))
        return answers

uniDict = {WHITE: {Pawn: "P", Rook: "R", Bishop: "B", King: "K", Queen: "Q"},
           BLACK: {Pawn: "P", Rook: "R", Bishop: "B", King: "K", Queen: "Q"}}

Game()
