'''
Created on Jul 29, 2020

@author: wirt
'''

from src.board import *

board = Board()

while board.king.end_square(board)==False:
    print("king at", board.king.get_coords())
    print("enter 0 indexed coordinates to move to.")
    row = input("row: ")
    col = input("column: ")
    row = int(row)
    col = int(col)
    if board.is_valid(row, col) == False:
        print("invalid board coordinates")
        continue
    square = Square(row, col)
    if board.king.is_legal_move(square)==False:
        print("illegal move for the king")
        continue
    board.king.move(square)

print("hooray, you won")
