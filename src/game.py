'''
Created on Jul 29, 2020

@author: wirt
'''
from src.pieces import King

class Game:
    game_over = False
    piece_set = list()

    def __init__(self):
        self.white_king = King((0, 1), True)
        self.black_king = King((7, 1), False)
        self.piece_set.append(self.white_king)
        self.piece_set.append(self.black_king)

    #I thing the possible attack moves can be stored with a dictionary keyed to each individual piece on the board
    # just need to rewrite one entry per move, or possibly remove in case of capture
    def commit_move(self,  move):
        move.piece.position = move.target_tup
        if self.white_king.at_end() or self.black_king.at_end():
            self.game_over= True
        #check if either king has hit the eighth square and update accordingly

    #returns a list of all pieces and their positions on the board
    def all_piece_positions(self):
        #using a set here to reenforce no two piceces may occupy the same space on the board
        positions = set()
        for p in self.piece_set:
            record = "White" if p.is_white else "Black"
            record += " " + str(p.type) + " " + str(p.position)
            positions.add(record)
        return positions

    def causes_check(self, move):
        oppenent_king = None
        if move.piece.is_white:
            oppenent_king = self.black_king
        else:
            oppenent_king = self.black_king
        if oppenent_king in move.piece.get_attacks():
            return True
        if move.piece.is_king:
            for p in self.piece_set:
                if p != move.piece:
                    if move.target_tup in p.get_attacks():
                        return True
        return False

class Move:
    piece = None
    target_tup = ();
    def __init__(self,color_bool, coords, piece_set):
        for i in piece_set:
            if color_bool == i.is_white:
                self.piece = i
                break
        self.target_tup = (int(coords[-2]), int(coords[-1]))
#need to find the piece on the board,and store target coords at target_tup

    def is_legal(self):
        if self.target_tup in self.piece.get_attacks():
            return True
        return False

    #eventually need to evaluate between two same color pieces