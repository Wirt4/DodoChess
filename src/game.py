'''
Created on Jul 29, 2020

@author: wirt
'''
from src.pieces import King

class Game:
    game_over = False
    piece_set = list()
    white_winner = False

    def __init__(self):
        #a time vs space tradeoff here,
        self.white_king = King((0, 1), True)
        self.black_king = King((7, 1), False)
        self.piece_set.append(self.white_king)
        self.piece_set.append(self.black_king)

    #I thing the possible attack moves can be stored with a dictionary keyed to each individual piece on the board
    # just need to rewrite one entry per move, or possibly remove in case of capture
    def commit_move(self,  move):
        move.piece.position = move.target_tup
        move.piece.update_attacks()
        if self.white_king.at_end() or self.black_king.at_end():
            self.game_over = True
            if self.white_king.at_end():
                self.white_winner = True

    def resign(self, player_is_white):
        self.game_over = True
        if not player_is_white:
            self.white_winner = True

    def all_piece_positions(self):
        positions = set()
        for p in self.piece_set:
            record = "White" if p.is_white else "Black"
            record += " " + str(p.type) + " " + str(p.position)
            positions.add(record)
        return positions

    def causes_check(self, move):
        if move.piece.is_white:
            opponent_king = self.black_king
        else:
            opponent_king = self.black_king
        if opponent_king in move.piece.get_attacks():
            return True
        if move.piece.is_king:
            for piece in self.piece_set:
                if piece != move.piece:
                    if move.target_tup in piece.get_attacks():
                        return True
        return False


class Move:
    piece = None
    target_tup = ()

    def __init__(self,color_bool, coords, piece_set):
        for i in piece_set:
            if color_bool == i.is_white:
                self.piece = i
                break
        self.target_tup = (int(coords[-2]), int(coords[-1]))

    def is_legal(self):
        if self.target_tup in self.piece.get_attacks():
            return True
        return False
