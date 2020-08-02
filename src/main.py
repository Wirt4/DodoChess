'''
Created on Jul 29, 2020

@author: wirt
'''

from src.game import Game
from src.game import Move
from src.player import Player

game = Game()
p1 = Player("Harvey", True)
p2 = Player("Bruce", False)

player = p1

while not game.game_over:
    coords = input(player.name + ", enter a move, or 'b' for piece positions ")
    if coords[0] == 'b':
        print(game.all_piece_positions())
        continue

    move = Move(player.is_white, coords, game.piece_set)
    # toggle players
    #this happens after move is committed
    if not move.is_legal() or game.causes_check(move):
        print("illegal move")
        continue
    game.commit_move(move)
    if game.game_over:
        break
    player = p1 if player == p2 else p2

print(player.name + " wins")