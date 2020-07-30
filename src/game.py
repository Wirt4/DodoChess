'''
Created on Jul 30, 2020

@author: wirt
'''
from board import Board
from enum import Enum
from player import Player
from pieces import ChesspersonColor

class Game(object):
    white_turn = True
    board = Board()
    player_1 = Player(ChesspersonColor.WHITE)
    player_2 = Player(ChesspersonColor.BLACK)

    def play(self):
        while(True):
            if self.white_turn==True:
                self.player_1.move()
                white_turn = False
            else:
                self.player_2.move()
                white_turn = True
                
            if self.player_1.king_at_8th():
                return Outcomes.WHITE
            
            if self.player_2.king_at_8th():
                return Outcomes.BLACK
            
class Outcomes(Enum):
    WHITE = "white wins"
    BLACK = "black wins"
    DRAW ="stalemate"