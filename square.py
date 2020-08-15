import pygame

class Square:
    """Class to make a chess square"""
    def __init__(self, settings, is_white):
        """initializesa assets for square"""
        #self.screen = screen
        self.settings = settings
        self.is_white = is_white
        self.size = self.settings.square_size
        self.my_rect = pygame.Rect(0, 0, self.settings.square_size, self.settings.square_size)

    def draw_square(self, screen, x_cord, y_cord):
        self.my_rect.x = x_cord
        self.my_rect.y = y_cord
        if self.is_white:
            color = self.settings.white_square
        else:
            color = self.settings.black_square
        pygame.draw.rect(screen, color, self.my_rect)