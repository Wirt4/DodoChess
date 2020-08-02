'''
Created on Jul 28, 2020

@author: wirt
'''

class Board():
    length = 8
    squares = dict()

    def __init__(self):
        self.make_board()
        self.king = King(self.get_square(4,0))

    def make_board(self):
        for r in range(self.length):
            for c in range(self.length):
                self.squares[r*10 + c] = Square(r, c)

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

    


    
