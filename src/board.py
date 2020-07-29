'''
Created on Jul 28, 2020

@author: wirt
'''

from pieces import *

class Board():
    #to be filled with Square objects
    squares=[[]]
    #to be filled with Piece objects
    piece_set=[]
    #also want a PieceSet member that is "PieceSet top

    def __init__(self, is_dodo):
        self.squares = self.create_board()
        
    def create_board(self):
        board =[]
        for i in range(ord('a'),ord('a')+8):
            row = []
            for j in range(1, 1+8):
                row.append(Square(chr(i), j))
            board.append(row)
        return board
    
class Square():
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
class PieceSet():
    #need a list of pieces in set
    
    #also need a PieceColor object 
    foo = 0

    
