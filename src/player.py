'''
Created on Jul 30, 2020

@author: wirt
'''
from pieces import ChesspersonColor

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, color):
        self.ChesspersonColor = color
        
    def move(self):
        return str(self.ChesspersonColor) + "moved"
    
    def king_at_8th(self):
        return False
        