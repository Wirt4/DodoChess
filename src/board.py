'''
Created on Jul 26, 2020

@author: wirt
'''
from pieces import *
class Board():
    '''
    classdocs
    '''
    white_king = King(True, 'e', 1)
    #black_king = King(e,1)
    def __init__(self, width, height):
        self.width = width
        self.height = height
      
    def move(self, chess_person, row, col ):
        pass
    #to move or capture a chess person
    #param is the chess person to grap, then the detstination square
    #use the object's rules to determine legality of move direction