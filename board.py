import pygame
from square import Square


class Board:
    #need to set up a board of 8 by 8 squares
    #need to create the board in init
    #also will want a draw board method to call in init
    def __init__(self, dc_game):
        self.screen = dc_game.screen
        self.settings = dc_game.settings
        self.color = self.settings.dark_purple
        self.rect = pygame.Rect(0, 0, self.settings.board_width, self.settings.board_width)
        self.screen_rect = self.screen.get_rect()
        #might need to check below...
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.midtop = dc_game.screen.midtop

    def create_board(self, size):
        #link together a bunch of squares in size*size formation
        #white goes in the lower righthand corner
        pass

    def draw_board(self):
        """draws the chessboard we created"""
        white = True
        start_x_coord = self.settings.square_size * self.settings.board_width
       # y_cord = x_cord
        x_cord = start_x_coord
        #sets flush  at bottom of square
        y_cord = self.settings.square_size * (self.settings.board_width-1)
        for i in range(8):
            for j in range(8):
                #should get a nice big old board, all yellow
                square = Square(self.settings, white)
                square.draw_square(self.screen, x_cord, y_cord)
                white = self._toggle_white(white)
                x_cord -= self.settings.square_size
            x_cord = start_x_coord
            white = self._toggle_white(white)
            y_cord -= self.settings.square_size

    def _toggle_white(self, white):
        if white:
            return False
        return True