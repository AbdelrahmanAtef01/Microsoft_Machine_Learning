import numpy as np
import sys

playGround = np.full((8, 8), '   ', dtype=object)
capturedPieces = np.array([])  # Initialize capturedPieces as an empty list
check = True

class ChessPiece:
    def __init__ (self, color, symbol, position):
        self.color = color
        self.symbol = symbol
        self.position = position  # Position is a tuple like (row, column)
        self.name = self.__class__.__name__

    def capture_piece(self, new_position, target):
        global capturedPieces
        capturedPieces = np.append(capturedPieces, target.symbol)
        pieces.pop(playGround[new_position[0]][new_position[1]].rstrip())

    def move(self, new_position):
        print("Moving")
        return True
    def _print_(self):
        print (self.color + " " + self.name + " at " + str(self.position))

class King(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)

    def check_king_move(self, new_position):
        if (playGround[new_position[0]][new_position[1]] == '   '):
            return True
        else:
            target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
            if target.color != self.color:
                self.capture_piece(new_position, target)
                return True
            else:
                return False

    def move(self, new_position):
        # Kings move one square in any direction
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])
        if row_diff <= 1 and col_diff <= 1 and self.check_king_move(new_position):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("King moved succefully to " + str(self.position))
            return True
        else:
            print("Invalid move for King")
            return False

class Minister(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)

    def check_diagonal_move(self, new_position):
        temp_position = self.position
        row_up = False
        col_up = False
        if new_position[0] > temp_position[0]:
            row_up = True
        if new_position[1] > temp_position[1]:
            col_up = True
        while temp_position[0] != new_position[0]:
            if row_up:
                temp_position = (temp_position[0]+1, temp_position[1])
            else:
                temp_position = (temp_position[0]-1, temp_position[1])
            if col_up:
                temp_position = (temp_position[0], temp_position[1]+1)
            else:
                temp_position = (temp_position[0], temp_position[1]-1)
            if playGround[temp_position[0]][temp_position[1]] != '   ' and temp_position[0] != new_position[0]:
                return False
        return True

    def check_line_move(self, new_position):
        temp_position = self.position
        row_up = 0
        col_up = 0
        if new_position[0] > temp_position[0]:
            row_up = 1
        elif new_position[0] < temp_position[0]:
            row_up = -1
        if new_position[1] > temp_position[1]:
            col_up = 1
        elif new_position[1] < temp_position[1]:
            col_up = -1
        while temp_position[0] != new_position[0] or temp_position[1] != new_position[1]:
            if row_up == 1:
                temp_position = (temp_position[0]+1, temp_position[1])
            elif row_up == -1:
                temp_position = (temp_position[0]-1, temp_position[1])
            if col_up == 1:
                temp_position = (temp_position[0], temp_position[1]+1)
            elif col_up == -1:
                temp_position = (temp_position[0], temp_position[1]-1)
            if playGround[temp_position[0]][temp_position[1]] != '   ' and (temp_position[0] != new_position[0] or temp_position[1]) != new_position[1]:
                return False
        return True


    def check_minister_move(self, new_position, row_diff, col_diff):
        if row_diff == 0 or col_diff == 0 :
           accept = self.check_line_move(new_position)
        else:
           accept = self.check_diagonal_move(new_position)
        if accept:
          if (playGround[new_position[0]][new_position[1]] == '   '):
              return True
          else:
              target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
              if target.color != self.color:
                 self.capture_piece(new_position, target)
                 return True
              else:
                 return False
        else:
          return False

    def move(self, new_position):
        # Ministers move any number of squares in any direction
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])
        if (row_diff == col_diff or new_position[0] == self.position[0] or new_position[1] == self.position[1]) and self.check_minister_move(new_position, row_diff, col_diff):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("Minister moved succefully to " + str(self.position))
            return True
        else:
            print("Invalid move for Minister")
            return False

class Rook(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)

    def check_rook_move(self, new_position):
        temp_position = self.position
        row_up = 0
        col_up = 0
        if new_position[0] > temp_position[0]:
            row_up = 1
        elif new_position[0] < temp_position[0]:
            row_up = -1
        if new_position[1] > temp_position[1]:
            col_up = 1
        elif new_position[1] < temp_position[1]:
            col_up = -1
        while temp_position[0] != new_position[0] or temp_position[1] != new_position[1]:
            if row_up == 1:
                temp_position = (temp_position[0]+1, temp_position[1])
            elif row_up == -1:
                temp_position = (temp_position[0]-1, temp_position[1])
            if col_up == 1:
                temp_position = (temp_position[0], temp_position[1]+1)
            elif col_up == -1:
                temp_position = (temp_position[0], temp_position[1]-1)
            if playGround[temp_position[0]][temp_position[1]] != '   ' and (temp_position[0] != new_position[0] or temp_position[1] != new_position[1]):
                return False

        if (playGround[new_position[0]][new_position[1]] == '   '):
            return True
        else:
            target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
            if target.color != self.color:
                self.capture_piece(new_position, target)
                return True
            else:
                return False

    def move(self, new_position):
        # Rooks move any number of squares horizontally or vertically
        if (new_position[0] == self.position[0] or new_position[1] == self.position[1]) and self.check_rook_move(new_position):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("Rook moved succefully to " + str(self.position))
            return True
        else:
            print("Invalid move for Rook")
            return False

class Elephant(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)


    def check_elephant_move(self, new_position):
        temp_position = self.position
        row_up = False
        col_up = False
        if new_position[0] > temp_position[0]:
            row_up = True
        if new_position[1] > temp_position[1]:
            col_up = True
        while temp_position[0] != new_position[0]:
            if row_up:
                temp_position = (temp_position[0]+1, temp_position[1])
            else:
                temp_position = (temp_position[0]-1, temp_position[1])
            if col_up:
                temp_position = (temp_position[0], temp_position[1]+1)
            else:
                temp_position = (temp_position[0], temp_position[1]-1)
            if playGround[temp_position[0]][temp_position[1]] != '   ' and temp_position[0] != new_position[0]:
                return False

        if (playGround[new_position[0]][new_position[1]] == '   '):
            return True
        else:
            target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
            if target.color != self.color:
                self.capture_piece(new_position, target)
                return True
            else:
                return False

    def move(self, new_position):
        # Elephants move any number of squares diagonally
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])
        if row_diff == col_diff and self.check_elephant_move(new_position):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("Elephant moved succefully to " + str(self.position))
            return True
        else:
            print("Invalid move for Elephant")
            return False

class Horse(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)

    def check_horse_move(self, new_position):
        if (playGround[new_position[0]][new_position[1]] == '   '):
            return True
        else:
            target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
            if target.color != self.color:
                self.capture_piece(new_position, target)
                return True
            else:
                return False

    def move(self, new_position):
        # Horses move in an L-shape: two squares in one direction and then one square perpendicular
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])
        if ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)) and self.check_horse_move(new_position):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("Horse moved succefully to " + str(self.position))
            return True
        else:
            print("Invalid move for Horse")
            return False

class Soldier(ChessPiece):

    def __init__ (self, color, symbol, position):
        super().__init__ (color , symbol, position)
        self.init = 0

    def check_soldier_move(self, new_position, row_diff, col_diff):
        if row_diff == 2:
          if (playGround[int((new_position[0]+self.position[0])/2)][new_position[1]] != '   '):
            return False
          elif (playGround[new_position[0]][new_position[1]] != '   '):
            return False
          else:
            return True
        else :
          if col_diff == 0:
            if (playGround[new_position[0]][new_position[1]] != '   '):
              return False
            else:
              return True
          else:
              if (playGround[new_position[0]][new_position[1]] == '   '):
                 return False
              else:
                 target = pieces.get(playGround[new_position[0]][new_position[1]].rstrip())
                 if target.color != self.color:
                      self.capture_piece(new_position, target)
                      return True
                 else:
                      return False

    def move(self, new_position):
        # Soldiers move forward one square, or two squares from their initial position
        if self.color == "white":
           row_diff = new_position[0] - self.position[0]
        else:
           row_diff = self.position[0] - new_position[0]
        col_diff = abs(new_position[1] - self.position[1])
        if (col_diff == 0 or col_diff == 1) and ((self.init == 0 and row_diff <= 2)or(self.init !=0 and row_diff == 1)) and self.check_soldier_move(new_position, row_diff, col_diff):
            playGround[self.position[0]][self.position[1]] = "   "
            playGround[new_position[0]][new_position[1]] = self.symbol
            self.position = new_position
            print ("Soldier moved succefully to " + str(self.position))
            self.init += 1
            return True
        else:
            print("Invalid move for Soldier")
            return False

s1 = Soldier("white", "s1 ", (1,0))
s2 = Soldier("white", "s2 ", (1,1))
s3 = Soldier("white", "s3 ", (1,2))
s4 = Soldier("white", "s4 ", (1,3))
s5 = Soldier("white", "s5 ", (1,4))
s6 = Soldier("white", "s6 ", (1,5))
s7 = Soldier("white", "s7 ", (1,6))
s8 = Soldier("white", "s8 ", (1,7))
s9  = Soldier("black", "s1.", (6,0))
s10 = Soldier("black", "s2.", (6,1))
s11 = Soldier("black", "s3.", (6,2))
s12 = Soldier("black", "s4.", (6,3))
s13 = Soldier("black", "s5.", (6,4))
s14 = Soldier("black", "s6.", (6,5))
s15 = Soldier("black", "s7.", (6,6))
s16 = Soldier("black", "s8.", (6,7))
k1 = King("white", "k  ", (0,3))
k2 = King("black", "k. ", (7,3))
m1 = Minister("white", "m  ", (0,4))
m2 = Minister("black", "m. ", (7,4))
h1 = Horse("white", "h1 ", (0,1))
h2 = Horse("white", "h2 ", (0,6))
h3 = Horse("black", "h1.", (7,1))
h4 = Horse("black", "h2.", (7,6))
e1 = Elephant("white", "e1 ", (0,2))
e2 = Elephant("white", "e2 ", (0,5))
e3 = Elephant("black", "e1.", (7,2))
e4 = Elephant("black", "e2.", (7,5))
r1 = Rook("white", "r1 ", (0,0))
r2 = Rook("white", "r2 ", (0,7))
r3 = Rook("black", "r1.", (7,0))
r4 = Rook("black", "r2.", (7,7))
pieces = {"s1":s1,"s2":s2,"s3":s3,"s4":s4,"s5":s5,"s6":s6,"s7":s7,"s8":s8,"s1.":s9,"s2.":s10,"s3.":s11,"s4.":s12,"s5.":s13,"s6.":s14,"s7.":s15,"s8.":s16,
          "k":k1,"k.":k2,"m":m1,"m.":m2,"h1":h1,"h2":h2,"h1.":h3,"h2.":h4,"e1":e1,"e2":e2,"e1.":e3,"e2.":e4,"r1":r1,"r2":r2,"r1.":r3,"r2.":r4}
chessPiecesArray = np.array([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,k1,k2,m1,m2,h1,h2,h3,h4,e1,e2,e3,e4,r1,r2,r3,r4])
class Play :
    def __init__ (self):
        for chessPiece in chessPiecesArray :
          playGround[chessPiece.position[0]][chessPiece.position[1]] = chessPiece.symbol

# Main
play = Play()
print(playGround)
print ("Captured pieces are : "+ str(capturedPieces))
lastColor = "black"
while(check):
  kingIsCaptured = False
  for capturedPiece in capturedPieces:
    if capturedPiece.rstrip() == "k":
      kingIsCaptured = True
      print("GAME OVER FOR THE WHITE KINGDOM, BLACK WINS!!")
      break
    elif capturedPiece.rstrip() == "k.":
      kingIsCaptured = True
      print("GAME OVER FOR THE BLACK KINGDOM, WHITE WINS!!")
      break
  if kingIsCaptured :
    sys.exit()
  pieceIsCaptured = False
  name = input("please Enter piece name : ")
  piece = pieces.get(name)
  for capturedPiece in capturedPieces:
    if capturedPiece.rstrip() == name:
      pieceIsCaptured = True
      break
  if pieceIsCaptured:
    print("This piece is captured and cann't be played")
    pieceIsCaptured = False
    continue
  elif piece is None:
    print("Invalid piece name")
    continue
  elif piece.color == lastColor:
    print("Not your turn " + piece.color + " :)")
    continue

  new_position = input("Enter the new position of the piece (row, column): ")
  # Convert position input to a tuple
  new_position = tuple(map(int, new_position.strip("()").split(",")))
  if new_position[0] < 0 or new_position[0] > 7 or new_position[1] < 0 or new_position[1] > 7:
    print("Invalid position")
    continue
  moved = piece.move(new_position)
  if moved:
    lastColor = piece.color
  print(playGround)
  print ("Captured pieces are : "+ str(capturedPieces))

#print(playGround)
#king = King('White', (0, 4))
#king._print_()
#king.move((1, 3))

#minister = Minister('Black', (0, 3))
#minister._print_()
#minister.move((4, 3))

#elephant = Elephant('White', (0, 2))
#elephant._print_()
#elephant.move((2, 3))

#horse = Horse('Black', (0, 1))
#horse._print_()
#horse.move((2, 2))

#soldier = Soldier('Black', (1, 1))
#soldier._print_()
#soldier.move((3, 1))
#soldier.move((5, 1))
#soldier.move((4, 1))