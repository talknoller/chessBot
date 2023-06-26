from board import Board
from square import Square
from piece import Piece


def generate_board():
    board = []
    is_black = True
    for i in range(8):
        row = []
        for j in range(8):
            if is_black:
                square = Square(i, j, 'b', None)
            else:
                square = Square(i, j, 'w', None)
            row.append(square)
            is_black = not is_black
        board.append(row)
        is_black = not is_black
    return board


def array_to_square(board, array):
    return board[array[0], array[1]]


def make_move(board, start_cord, end_cord):
    for move in board[start_cord[0], start_cord[1]].available_moves:
        if move[0] == end_cord[0] and move[1] == end_cord[1]:
            print("here")
            return


def array_to_cord(cord_array):
    if cord_array[0] > 7 or cord_array[0] < 0 or cord_array[1] > 7 or cord_array[1] < 0:
        return "invalid cords"

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return files[cord_array[0]] + str(cord_array[1] + 1)


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
board = Board(generate_board())
test_cord = [6, 7]
board.squares[test_cord[0]][test_cord[1]].piece = wknight

print("knight starts at " + array_to_cord(test_cord))
# for move in board.legal_moves(test_cord):
#     print(array_to_cord(move))
for i in range(10):
    next_cord = board.legal_moves(test_cord)[0]
    board.make_move(test_cord, next_cord)
    test_cord = next_cord
    board.print_pieces()

