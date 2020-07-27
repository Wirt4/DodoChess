'''
Created on Jul 26, 2020

@author: wirt
'''

class ChessPerson():
    '''
    classdocs
    '''

    def __init__(self, isWhite, row, col):
        if isWhite:
            self.color = "white"
        else:
            self.color ="black"
        self.row = row
        self.col = col
    
    def get_pos(self):
        return self.row + str(self.col)
    
class King(ChessPerson):