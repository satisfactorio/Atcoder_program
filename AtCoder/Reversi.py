import random
import numpy as np
import sys

EMPTY = 0
WHITE = -1
BLACK = 1
WALL = 2

BOARD_SIZE = 8

NONE = 0
LEFT = 2**0
UPPER_LEFT = 2**1
UPPER = 2**2
UPPER_RIGHT = 2**3
RIGHT = 2**4
LOWER_RIGHT = 2**5
LOWER = 2**6
LOWER_LEFT = 2**7

IN_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
IN_NUMBER = ['1', '2', '3', '4', '5', '6', '7', '8']

MAX_TURNS = 60

if len(sys.argv) == 2:
    HUMAN_COLOR = sys.argv[1]
else:
    HUMAN_COLOR = ''

class Board:
    def __init__(self):
        self.RawBoard = np.zeros((BOARD_SIZE + 2, BOARD_SIZE + 2), dtype = int)

        self.RawBoard[0, :] = WALL
        self.RawBoard[:, 0] = WALL
        self.RawBoard[BOARD_SIZE + 1, :] = WALL
        self.RawBoard[:, BOARD_SIZE + 1] = WALL

        self.RawBoard[4, 4] = WHITE
        self.RawBoard[5, 5] = WHITE
        self.RawBoard[4, 5] = BLACK
        self.RawBoard[5, 4] = BLACK

        self.Turns = 0

        self.CurrentColor = BLACK

        self.MovablePos = np.zeros((BOARD_SIZE + 2, BOARD_SIZE + 2), dtype = int)
        self.MovableDir = np.zeros((BOARD_SIZE + 2, BOARD_SIZE + 2), dtype = int)

        self.initMovable()




    def move(self, x, y):
        if x < 1 or BOARD_SIZE < x:
            return False
        if y < 1 or BOARD_SIZE < y:
            return False
        if self.MovablePos[x, y] == 0:
            return False
        
        self.flipDiscs(x, y)

        self.Turns += 1

        self.CurrentColor = -self.CurrentColor

        self.initMovable()

        return True

    
    def flipDiscs(self, x, y):
        self.RawBoard[x, y] = self.CurrentColor

        self.RawBoard[x, y] = self.CurrentColor
 
        dir = self.MovableDir[x, y]
 
        if dir & LEFT:  
            x_tmp = x - 1
 
            while self.RawBoard[x_tmp, y] == - self.CurrentColor:
                self.RawBoard[x_tmp, y] = self.CurrentColor
                x_tmp -= 1
 
        if dir & UPPER_LEFT:  
            x_tmp = x - 1
            y_tmp = y - 1
 
            while self.RawBoard[x_tmp, y_tmp] == - self.CurrentColor:
                self.RawBoard[x_tmp, y_tmp] = self.CurrentColor
                x_tmp -= 1
                y_tmp -= 1
 
        if dir & UPPER: 
            y_tmp = y - 1
            while self.RawBoard[x, y_tmp] == - self.CurrentColor:
                self.RawBoard[x, y_tmp] = self.CurrentColor
                y_tmp -= 1
 
        if dir & UPPER_RIGHT:
            x_tmp = x + 1
            y_tmp = y - 1

            while self.RawBoard[x_tmp, y_tmp] == - self.CurrentColor:
                self.RawBoard[x_tmp, y_tmp] = self.CurrentColor
                x_tmp += 1
                y_tmp -= 1
 
        if dir & RIGHT: 
            x_tmp = x + 1

            while self.RawBoard[x_tmp, y] == - self.CurrentColor:
                self.RawBoard[x_tmp, y] = self.CurrentColor
                x_tmp += 1

        if dir & LOWER_RIGHT:
            x_tmp = x + 1
            y_tmp = y + 1
 
            while self.RawBoard[x_tmp, y_tmp] == - self.CurrentColor:
                self.RawBoard[x_tmp, y_tmp] = self.CurrentColor
                x_tmp += 1
                y_tmp += 1

        if dir & LOWER:  
            y_tmp = y + 1
 
            while self.RawBoard[x, y_tmp] == - self.CurrentColor:
                self.RawBoard[x, y_tmp] = self.CurrentColor
                y_tmp += 1
 
        if dir & LOWER_LEFT: 
            x_tmp = x - 1
            y_tmp = y + 1
 
            while self.RawBoard[x_tmp, y_tmp] == - self.CurrentColor:
                self.RawBoard[x_tmp, y_tmp] = self.CurrentColor
                x_tmp -= 1
                y_tmp += 1

    
    def checkMobility(self, x, y, color):
        dir = 0

        if self.RawBoard[x, y] != EMPTY:
            return dir

        if self.RawBoard[x - 1, y] == - color:
            x_tmp = x - 2
            y_tmp = y

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
            
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LEFT
        
        if self.RawBoard[x - 1, y - 1] == - color:
            x_tmp = x - 2
            y_tmp = y - 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
                y_tmp -= 1
            
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER_LEFT

        if self.RawBoard[x, y - 1] == - color:
            x_tmp = x
            y_tmp = y - 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                y_tmp -= 1
            
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER 
            
        if self.RawBoard[x + 1, y - 1] == - color:
            x_tmp = x + 2
            y_tmp = y - 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
                y_tmp -= 1

            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER_RIGHT
            
        if self.RawBoard[x + 1, y] == - color:
            x_tmp = x + 2
            y_tmp = y

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
            
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | RIGHT
            
        if self.RawBoard[x + 1, y + 1] == - color:
            x_tmp = x + 2
            y_tmp = y + 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
                y_tmp += 1
            
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER_RIGHT
            
        if self.RawBoard[x, y + 1] == - color:
            x_tmp = x
            y_tmp = y + 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                y_tmp += 1

            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER 
            
        if self.RawBoard[x - 1, y + 1] == - color:
            x_tmp = x - 2
            y_tmp = y + 2

            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
                y_tmp += 1

            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER_LEFT

        return dir
    

    def initMovable(self):
        self.MovablePos[:, :] = False

        for x in range(1, BOARD_SIZE + 1):
            for y in range(1, BOARD_SIZE + 1):
                dir = self.checkMobility(x, y, self.CurrentColor)

                self.MovableDir[x, y] = dir

                if dir != 0:
                    self.MovablePos[x, y] = True
    

    def isGameOver(self):
        if self.Turns >= MAX_TURNS:
            return True
        if self.MovablePos[:, :].any():
            return False
        
        for x in range(1, BOARD_SIZE + 1):
            for y in range(1, BOARD_SIZE + 1):
                if self.checkMobility(x, y, - self.CurrentColor) != 0:
                    return False
        
        return True


    def skip(self):
        if any(self.MovablePos[:, :]):
            return False
        if self.isGameOver():
            return False
        self.CurrentColor = - self.CurrentColor

        self.initMovable()

        return True


    def display(self):
        print(' a b c d e f g h')

        for y in range(1, 9):
            print(y, end='')
            
            for x in range(1, 9):
                grid = self.RawBoard[x, y]
                if grid == EMPTY:
                    print('□', end=' ')
                elif grid == WHITE:
                    print('●', end=' ')
                elif grid == BLACK:
                    print('○', end=' ')
                
            print()
    
    def checkIN(self, IN):
        if not IN:
            return False

        if IN[0] in IN_ALPHABET:
            if IN[1] in IN_NUMBER:
                return True
 
        return False
    
        
    
    
    def randomInput(self):
        if board.skip == True:
            return False

        grids = np.where(self.MovablePos == 1)

        random_chosen_index = random.randrange(len(grids[0]))
        x_grid = grids[0][random_chosen_index]
        y_grid = grids[1][random_chosen_index]

        return IN_ALPHABET[x_grid - 1] + IN_NUMBER[y_grid - 1]

    






board = Board()

while True:
    board.display()

    if board.CurrentColor == BLACK:
        print('黒の番です: ', end='')
    else:
        print('白の番です: ', end='')
    
    if board.CurrentColor == BLACK:
        IN = input()
    else:
        IN = board.randomInput()
        print(IN)
    print()

    # IN = input()

    if IN == 'e':
        print('おつかれ')
        break

    if board.checkIN(IN):
        x = IN_ALPHABET.index(IN[0]) + 1
        y = IN_NUMBER.index(IN[1]) + 1
    else:
        print('正しい形式（例:f5）で入力してください')
        continue

    if not board.move(x, y):
        print('そこには置けません')
        continue

    if board.isGameOver():
        board.display()
        print('おわり')
        break

    if not board.MovablePos[:, :].any():
        board.CurrentColor = - board.CurrentColor
        board.initMovable()
        print('パスしました')
        print()
        continue

print()
    
count_black = np.count_nonzero(board.RawBoard[:, :] == BLACK)
count_white = np.count_nonzero(board.RawBoard[:, :] == WHITE)
    
print('黒:', count_black)
print('白:', count_white)
 
dif = count_black - count_white
if dif > 0:
    print('黒の勝ち')
elif dif < 0:
    print('白の勝ち')
else:
    print('引き分け')


