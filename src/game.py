'''
Created on Jul 29, 2020

@author: wirt
'''
import enum

from pieces import PieceColor

class CheckStatus(enum.Enum):
    BLACK_IN_CHECK ="black in check"
    WHITE_IN_CHECK = "white in check"
    BLACK_CHECKMATED = "black checkmated"
    WHITE_CHECKMATED = "white checkmated"
    NO_CHECK = "no check"
    
class Game():
    #need list of moves
    turn = PieceColor.WHITE
    #a cinch since white goes first
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
        