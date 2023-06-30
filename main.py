from board import Board, move_to_string
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


board = generate_board()

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

king_cord = [7, 7]
queen_cord = [1, 0]
knight_cord = [2, 1]
attacker_cord = [6, 2]

board.get_square(king_cord).piece = wking
board.get_square(queen_cord).piece = bbishop
board.get_square(knight_cord).piece = wknight
# board.get_square(attacker_cord).piece = wbishop
board.print_pieces()
for move in board.legal_moves("b"):
    print(move_to_string(move))

# print(board.does_color_do_check("w"))
# print(board.does_color_do_check("b"))
