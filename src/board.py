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
    def __init__(self):
        '''
        Constructor
        '''
        print("you constructed a board")
        