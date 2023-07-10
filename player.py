import random

from board import move_to_string


class Player:
    def __init__(self, game, color):
        self.game = game
        self.color = color

    def play_random_move(self):
        legal_moves = self.game.legal_moves()
        move = legal_moves[random.randint(0, len(legal_moves) - 1)]
        self.game.make_move(move)
        print(move_to_string(move))
