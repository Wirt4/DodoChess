'''
Created on Jul 26, 2020

@author: wirt
'''
from enum import Enum
class ChessPerson():
    name = "chessman"
    int_row =0
    int_col =0
   
    def __init__(self, isWhite):
        if isWhite:
            self.color = "white"
        else:
            self.color ="black"
            
            
    def get_id(self):
        return self.color + self.name
    
    def is_legal(self, int_row, int_col):
        #should be a part of each piece, this is to override
        if int_row ==self.int_row and int_col == self.int_col:
            return False
        return True
    
class ChesspersonColor(Enum):
    BLACK = "black"
    WHITE = "white"
    
class King(ChessPerson):
    name = "king"
    def is_legal(self, int_row, int_col):
        if ChessPerson.is_legal(self, int_row, int_col) and abs(self.int_row - int_row) <= 1 and abs(self.int_col - int_col) <= 1:
            return True
        return False