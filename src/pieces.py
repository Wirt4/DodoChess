from enum import Enum

class Type(Enum):
    KING = "king"
    NULL = "none"

class Piece:
    board_size = 8
    is_king = False
    attack_squares = []
    position = ()
    type = Type.NULL

    def __init__(self, pos_tup, color_bool):
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


class King(Piece):
    is_king = True
    type = Type.KING

    def __init__(self, pos_tup, color_bool):
        super().__init__(pos_tup, color_bool)
        self.update_attacks()

    def update_attacks(self):
        self.attack_squares = self.get_attack_diag(1) + self.get_attack_rankfile(1)

    def get_attacks(self):
        return self.attack_squares

    def at_end(self):
        if self.position[1] == self.board_size-1:
            return True
        return False
