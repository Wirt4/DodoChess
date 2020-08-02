from enum import Enum


class Type(Enum):
    KING ="king"
    NULL = "no type"


class Piece:
    board_size = 8
    is_king = False
    #at this point, attack squares ARE move squares
    #this would change in the case of castling or pawn moves (std chess, not racing kings)
    attack_squares = []
    position = ()
    type = Type.NULL
    def __init__(self, pos_tup, color_bool):
       # square.has_piece = True
        self.position = pos_tup
        self.is_white = color_bool

    def on_board(self, file):
        return 0 <= file < self.board_size

    def get_attack_rankfile(self, limit):
        squares = []
        for i in range(limit):
            if self.on_board(self.position[0]+1):
                squares.append((self.position[0]+1, self.position[1]))
            if self.on_board(self.position[0]-1):
                squares.append((self.position[0]-1, self.position[1]))
            if self.on_board(self.position[1]+1):
                squares.append((self.position[0], self.position[1]+1))
            if self.on_board(self.position[1]-1):
                squares.append((self.position[0], self.position[1]-1))
        return squares

    def get_attack_diag(self, limit):
        squares = []
        for i in range(limit):
            if self.on_board(self.position[0]-1) and self.on_board(self.position[1]-1):
                squares.append((self.position[0]-1, self.position[1]-1))
            if self.on_board(self.position[0]-1) and self.on_board(self.position[1]+1):
                squares.append((self.position[0]-1, self.position[1]+1))
            if self.on_board(self.position[0]+1) and self.on_board(self.position[1]-1):
                squares.append((self.position[0]+1, self.position[1]-1))
            if self.on_board(self.position[0] + 1) and self.on_board(self.position[1] + 1):
                squares.append((self.position[0] + 1, self.position[1] + 1))
        return squares

    def get_attacks(self):
        pass
    # def move(self, new_square):
    #     self.square.has_piece = False
    #     new_square.has_piece = True
    #     self.square = new_square
    #
    # def end_square(self, board):
    #     return self.square.col == board.length-1
    #
    # def is_legal_move(self, new_square):
    #     if self.square.is_equal(new_square):
    #         return False
    #     return True
    #
    # def get_coords(self):
    #     coords = self.is_white + " " + " " + self.type + str(self.square.row) + " " + str(self.square.col)
    #     return coords


class King(Piece):
    type = Type.KING
    is_king = True
    def get_attacks(self):
        attacks = self.get_attack_diag(1) + self.get_attack_rankfile(1)
        return attacks

    def at_end(self):
        if self.position[1] == self.board_size-1:
            return True
        return False
