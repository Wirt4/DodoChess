'''
Created on Jul 26, 2020

@author: wirt
'''

class ChessPerson():
    name = "chessman"
   
    def __init__(self, isWhite):
        if isWhite:
            self.color = "white"
        else:
            self.color ="black"
            
    def get_id(self):
        return self.color + self.name
    
    def is_legal(self):
        #should be a part of each piece, this is to override
        pass
    
    
class King(ChessPerson):
    name = "king"