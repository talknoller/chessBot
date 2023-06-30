from board import Board, move_to_string
from constants import WHITE_KING_STARTING_POSITION, WHITE_KINGS_ROOK_STARTING_POSITION, \
    WHITE_QUEENS_ROOK_STARTING_POSITION
from game import Game
from square import Square, array_to_cord
from piece import Piece


def generate_board():
    board = []
    is_black = True
    for i in range(8):
        row = []
        for j in range(8):
            if is_black:
                square = Square(i, j, 'b', Piece("none", "none"))
            else:
                square = Square(i, j, 'w', Piece("none", "none"))
            row.append(square)
            is_black = not is_black
        board.append(row)
        is_black = not is_black
    return Board(board)


game = Game(generate_board(), "w")

wpawn = Piece('p', 'w')
bpawn = Piece('p', 'b')

brook = Piece('r', 'b')
bknight = Piece('n', 'b')
bbishop = Piece('b', 'b')
bqueen = Piece('q', 'b')
bking = Piece('k', 'b')

wrook = Piece('r', 'w')
wknight = Piece('n', 'w')
wbishop = Piece('b', 'w')
wqueen = Piece('q', 'w')
wking = Piece('k', 'w')

game.board.get_square(WHITE_KING_STARTING_POSITION).piece = wking
game.board.get_square(WHITE_KINGS_ROOK_STARTING_POSITION).piece = wrook
game.board.get_square(WHITE_QUEENS_ROOK_STARTING_POSITION).piece = wrook
game.board.get_square([0, 5]).piece = wrook

game.board.print_pieces()
game.board.make_move("w0-0-0")
print("white castle queen side")
game.board.print_pieces()
