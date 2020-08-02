'''
Created on Jul 28, 2020

@author: wirt
'''
from src.pieces import*

class Board():
    length = 8
    squares = dict()
    white_turn = True

    def __init__(self):
        self.make_board()
        self.piece_set = PieceSet(self)

    def make_board(self):
        for r in range(self.length):
            for c in range(self.length):
                self.squares[r*10 + c] = Square(r, c)

    def get_all_coords(self):
        #returns a full list of all pieces board and their coordinates
        #might require a piece set to iterate over
        return self.piece_set.get_cords()

    def is_valid(self, row, col):
        return self.check_span(row) and self.check_span(col)

    #helper function
    def check_span(self, rank):
        return (rank < self.length) and (rank >= 0)

    def get_square(self, row, col):
        #would have to amend this if board size changes
        return self.squares[row*10 +col]
    
class Square():
    has_piece = False
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def is_equal(self, square):
        return (self.row == square.row) and (self.col == square.col)

    
class PieceSet():
    the_set ={}
    def __init__(self, board):
        self.white_king = King(board.get_square(0, 0), Color.WHITE)
        self.black_king = King(board.get_square(0, 7), Color.BLACK)
        self.the_set.add(self.white_king)
        self.the_set.add(self.black_king)

    def get_cords(self):
        foo = []
        for p in self.the_set:
             foo.append(p.get_coords)
        return foo
    
