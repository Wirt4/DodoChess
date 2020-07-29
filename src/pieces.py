'''
Created on Jul 29, 2020

@author: wirt
'''

import enum

class PieceColor(enum.Enum):
    BLACK = "black"
    WHITE = "white"
    
class Piece():
    #needs a PieceColor constant
    # a PlaceAt variable, a Square object
    moved = False
    
    def valid_moves(self):
        #returns an array of Square objects
        pass
    
    def attack_squares(self):
        #returns an array of Square objects
        pass
    
    def capture_free_moves(self):
        #returns an array of Squares
        pass
    
    def too_be_captured(self):
        #todo: implement this method
        return False
        
class King(Piece):
    foo =""
    
class Queen(Piece):
    foo =""
    
class Bishop(Piece):
    foo =""
    
class Horsey(Piece):
    foo =""
    
class Pawn(Piece):
    promoted = False
    #member - promoteTo is a Piece object
    #member - moveTo is a moveTo Enum

class PieceType(enum.Enum):
    KING="king"
    PAWN ="pawn"
    QUEEN ="queen"
    BISHOP = "bishop"
    ROOK = "rook"
    HORSEY = "horsey"
    
class MoveDirection(enum.Enum):
    UP ="up"
    DOWN = "down"
    
    