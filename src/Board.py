'''
Created on Jul 28, 2020

@author: wirt
'''

import enum

class Board():
    #to be filled with Square objects
    squares=[[]]
    #to be filled with Piece objects
    piece_set=[]
    #also want a PieceSet member that is "PieceSet top

    def __init__(self):
        #constructor, may also take a boolean to switch between chess rules
        pass
    
class Square():
    row = 0;
    col = 0;
    
class PieceSet():
    #need a list of pieces in set
    
    #also need a PieceColor object 
    foo =0
    
class PieceColor(enum.Enum):
    BLACK ="black"
    WHITE ="white"
    
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

class CheckStatus(enum.Enum):
    BLACK_IN_CHECK ="black in check"
    WHITE_IN_CHECK = "white in check"
    BLACK_CHECKMATED = "black checkmated"
    WHITE_CHECKMATED = "white checkmated"
    NO_CHECK = "no check"
    
class Game():
    #need list of moves
    turn = PieceColor.WHITE #a cinch since white goes first
    #need a list of players
    #will need a Result variable
    def add_move(self):
        pass
    
    def is_ended(self):
        pass
    
    def is_checked(self):
        pass
    
    def operation(self):
        pass
    
    def is_checkmated(self):
        pass

class Player():
    #both of these are custom objects
    def __init__(self, engine, piece_color):
        self.engine = engine
        self.piece_color = piece_color    

class PlayerEngineInterface():
    
    def makeMove(self):
        pass
    
class HumanPlayer(PlayerEngineInterface):
    
    def makeMove(self):
        pass

class AIPlayer(PlayerEngineInterface):
    
    def makeMove(self):
        pass
    
