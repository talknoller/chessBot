class Board:
    def __init__(self, squares):
        self.squares = squares

    def legal_moves(self, square):
        square.available_moves(self.squares)
