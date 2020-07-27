'''
Created on Jul 26, 2020

@author: wirt
'''
from pieces import King
from __builtin__ import False
class Board():
    '''
    classdocs
    '''
    #black_king = King(e,1)
    def __init__(self):
        self.b = self.build_board()
        
    def build_board(self):
        #may add functionality here later on for different layouts
        white_king = King(True)
        side =8;
        col = [None] * side
        b = [col] * side
        b[self.row_to_i('e')][self.col_to_i(1)] = white_king
        return b
    
    def row_to_i(self, ch):
        #convert ch to lowercase
        ch = ch.lower()
        ch.strip()
        return ord(ch[0])- ord('a')
    
    def i_to_row(self, i):
        return chr(ord('a')+i)
    
    def col_to_i(self, i):
        return i-1
    
    def i_to_col(self, i):
        return i+1
    
    def is_piece(self, row, col):
        if self.b[self.row_to_i(row)][self.col_to_i(col)] == None:
            return False
        return True
    
    def get_piece(self, row, col):
        return self.b[self.row_to_i(row)][self.col_to_i(col)]
        
    def place_piece(self, piece, row, col):
        i_r = self.row_to_i(row)
        i_c = self.col_to_i(col)
        self.b[i_r][i_c] = piece
        pass
        
    def remove_piece(self, row, col):
        self.b[self.row_to_i(row)][self.col_to_i(col)] = None
        
    def move(self, init_row, init_col, fin_row, fin_col ):
        #convert from notation to cordinates
        if self.is_piece(init_row, init_col):
            piece = self.get_piece(init_row, init_col)
            self.place_piece(piece, fin_row, fin_col)
            self.remove_piece(init_row, init_col)
            print("%s %s moved to %s%d" % (piece.color, piece.name, fin_row, fin_col))
        else:
            print("no piece there")
            
        
    #to move or capture a chess person
    #param is the chess person to grap, then the detstination square
    #use the object's rules to determine legality of move direction