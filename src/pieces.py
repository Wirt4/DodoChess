

class King():
    def __init__(self, square):
        self.square = square

    def move(self, new_square):
        self.square = new_square

    def end_square(self, board):
        return self.square.col == board.length-1

    def is_legal_move(self, new_square):
        if self.square.is_equal(new_square):
            return False
        return abs(self.square.row - new_square.row) <= 1 and abs(self.square.col - new_square.col) <= 1

    def get_coords(self):
        coords = "" +str(self.square.row )+ " " + str(self.square.col)
        return coords