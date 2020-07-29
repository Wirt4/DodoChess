'''
Created on Jul 26, 2020

@author: wirt
'''
from pieces import King
from __builtin__ import False, True
class Board():
    '''
    classdocs
    '''
    #black_king = King(e,1)
    def __init__(self):
        self.b = self.build_board()
        self.white_king = King(True)
        self.place_piece(self.white_king, 'e', 1)
        
    def build_board(self):
        #may add functionality here later on for different layouts
        side =8;
        col = [None] * side
        b = [col] * side
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
        piece.int_row = i_r
        piece.int_col = i_c
        
    def remove_piece(self, row, col):
        self.b[self.row_to_i(row)][self.col_to_i(col)] = None
        
    def on_board(self, row, col):
        i_r = self.row_to_i(row)
        i_c = self.col_to_i(col)
        size = len(self.b)
        if i_r < 0 or i_c < 0:
            return False
        if i_r > size or i_c > size:
            return False
        return True
        
    def move(self, init_row, init_col, fin_row, fin_col ):
        if not self.on_board(fin_row, fin_col):
            print("%s%d not on board" %(fin_row, fin_col))
        if not self.is_piece(init_row, init_col):
            print ("no piece there")
            return 0
        piece = self.get_piece(init_row, init_col)
        if piece.is_legal(self.row_to_i(fin_row), self.col_to_i(fin_col)):
            self.place_piece(piece, fin_row, fin_col)
            self.remove_piece(init_row, init_col)
            print("%s %s moved to %s%d" % (piece.color, piece.name, fin_row, fin_col))
        else:
            print("illegal move for %s %s" % (piece.color, piece.name))
        return 0
    
            
        
    #to move or capture a chess person
    #param is the chess person to grap, then the detstination square
    #use the object's rules to determine legality of move direction