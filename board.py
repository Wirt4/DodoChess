import pygame
from square import Square


class Board:
    #need to set up a board of 8 by 8 squares
    #need to create the board in init
    #also will want a draw board method to call in init
    def __init__(self, dc_game, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.screen = dc_game.screen
        self.settings = dc_game.settings
        self.color = self.settings.dark_purple
        self.rect = pygame.Rect(0, 0, self.settings.board_width, self.settings.board_width)
        self.screen_rect = self.screen.get_rect()
        self.squares = []
        self.create_board(self.settings.board_width)
        #self.rect.midtop = dc_game.screen.midtop

    def create_board(self, size):
        """creates a list of all squares, initilized with appropriate colors and screen coordinates"""
        #link together a bunch of squares in size*size formation
        #white goes in the lower righthand corner
        length = self.settings.square_size * (self.settings.board_width - 1)
        white = True
        start_x_coord = self.x_cord + length
        x_cord = start_x_coord
        y_cord = self.y_cord + length
        for i in range(8):
            for j in range(8):
                square = Square(self.settings, white, x_cord, y_cord)
                self.squares.append(square)
                white = self._toggle_white(white)
                x_cord -= self.settings.square_size
            x_cord = start_x_coord
            white = self._toggle_white(white)
            y_cord -= self.settings.square_size

    def draw_board(self):
        """draws the chessboard we created"""
        for s in self.squares:
            s.draw_square(self.screen)

    def _toggle_white(self, white):
        if white:
            return False
        return True
