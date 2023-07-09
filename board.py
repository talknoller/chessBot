from piece import Piece
from square import array_to_cord
import copy
from constants import *


def is_square_in_list(square_cord_list, square_cord):
    for square in square_cord_list:
        if square[0] == square_cord[0] and square[1] == square_cord[1]:
            return True
    return False


def move_to_string(move):
    if move == "w0-0" or move == "b0-0":
        return "0-0"
    if move == "w0-0-0" or move == "b0-0-0":
        return "0-0-0"
    return array_to_cord(move[0]) + " to " + array_to_cord(move[1])


class Board:
    def __init__(self, squares):
        self.squares = squares
        self.size = 8

    def print_board(self):
        for i in range(self.size):
            for file in self.squares:
                if file[i].piece is not None and file[i].piece.id != "none":
                    print(file[i].piece.__str__() + " is at " + array_to_cord([file[i].file, file[i].row]))

    def available_moves(self, square_cord):
        if square_cord[0] >= self.size or square_cord[1] >= self.size:
            print("square doesn't exist")
            return []
        square = self.get_square(square_cord)
        if square.piece is None:
            print("empty square")
            return []

        available_moves = []
        if square.piece.id == 'p' and square.piece.color == 'w':
            if square.row < self.size - 1 and self.get_square([square.file, square.row + 1]).piece.color == "none":
                available_moves.append([square.file, square.row + 1])
                if square.file < self.size - 1 and self.get_square(
                        [square.file + 1, square.row + 1]).piece.color != "none" and self.get_square(
                        [square.file + 1, square.row + 1]).piece.color != square.piece.color:
                    available_moves.append([square.file + 1, square.row + 1])
                if square.file > 0 and self.get_square(
                        [square.file - 1, square.row + 1]).piece.color != square.piece.color and self.get_square(
                    [square.file - 1, square.row + 1]).piece.color != "none":
                    available_moves.append([square.file - 1, square.row + 1])

            if square.row == 1 and self.get_square([square.file, square.row + 2]).piece.color == "none":
                available_moves.append([square.file, square.row + 2])

        if square.piece.id == 'p' and square.piece.color == 'b':
            if square.row > 0 and self.get_square([square.file, square.row - 1]).piece.color == "none":
                available_moves.append([square.file, square.row - 1])

                if square.file < self.size - 1 and self.get_square(
                        [square.file + 1, square.row - 1]).piece.color != square.piece.color and self.get_square(
                    [square.file + 1, square.row - 1]).piece.color != "none":
                    available_moves.append([square.file + 1, square.row - 1])

                if square.file > 0 and self.get_square(
                        [square.file - 1, square.row - 1]).piece.color != square.piece.color and self.get_square(
                    [square.file - 1, square.row - 1]).piece.color != "none":
                    available_moves.append([square.file - 1, square.row - 1])

            if square.row == 6 and self.get_square([square.file, square.row - 2]).piece.color == "none":
                available_moves.append([square.file, square.row - 2])

        if square.piece.id == 'r' or square.piece.id == 'q':
            for i in range(square.row + 1, self.size):
                if self.get_square([square.file, i]).piece.color == "none":
                    available_moves.append([square.file, i])

                elif self.get_square([square.file, i]).piece.color != square.piece.color:
                    available_moves.append([square.file, i])
                    break
                else:
                    break
            for i in range(square.row - 1, -1, -1):
                if self.get_square([square.file, i]).piece.color == "none":
                    available_moves.append([square.file, i])
                elif self.get_square([square.file, i]).piece.color != square.piece.color:
                    available_moves.append([square.file, i])
                    break
                else:
                    break

            for i in range(square.file + 1, self.size):
                if self.get_square([i, square.row]).piece.color == "none":
                    available_moves.append([i, square.row])
                elif self.get_square([i, square.row]).piece.color != square.piece.color:
                    available_moves.append([i, square.row])
                    break
                else:

                    break
            for i in range(square.file - 1, -1, -1):

                if self.get_square([i, square.row]).piece.color == "none":
                    available_moves.append([i, square.row])
                elif self.get_square([square.file, i]).piece.color != square.piece.color:
                    available_moves.append([i, square.row])
                    break
                else:
                    break

        if square.piece.id == 'b' or square.piece.id == 'q':
            row = square.row + 1
            file = square.file + 1

            while file < self.size and row < self.size:
                if self.get_square([file, row]).piece.color == "none":
                    available_moves.append([file, row])
                    row += 1
                    file += 1
                elif self.get_square([file, row]).piece.color != square.piece.color:
                    available_moves.append([file, row])
                    break
                else:
                    break

            row = square.row - 1
            file = square.file - 1

            while file >= 0 and row >= 0:
                if self.get_square([file, row]).piece.color == "none":
                    available_moves.append([file, row])
                    row -= 1
                    file -= 1
                elif self.get_square([file, row]).piece.color != square.piece.color:
                    available_moves.append([file, row])
                    break
                else:
                    break

            row = square.row - 1
            file = square.file + 1

            while file < self.size and row >= 0:
                if self.get_square([file, row]).piece.color == "none":
                    available_moves.append([file, row])
                    row -= 1
                    file += 1
                elif self.get_square([file, row]).piece.color != square.piece.color:
                    available_moves.append([file, row])
                    break
                else:
                    break

            row = square.row + 1
            file = square.file - 1

            while file >= 0 and row < self.size:
                if self.get_square([file, row]).piece.color == "none":
                    available_moves.append([file, row])
                    row += 1
                    file -= 1
                elif self.get_square([file, row]).piece.color != square.piece.color:
                    available_moves.append([file, row])
                    break
                else:
                    break

        if square.piece.id == 'k':
            if square.row < self.size - 1 and square.file < self.size - 1 and self.get_square(
                    [square.file + 1, square.row + 1]).piece.color != square.piece.color:
                available_moves.append([square.file + 1, square.row + 1])

            if square.file < self.size - 1 and self.get_square(
                    [square.file + 1, square.row]).piece.color != square.piece.color:
                available_moves.append([square.file + 1, square.row])

            if square.row - 1 >= 0 and square.file < self.size - 1 and self.get_square(
                    [square.file + 1, square.row - 1]).piece.color != square.piece.color:
                available_moves.append([square.file + 1, square.row - 1])

            if square.row < self.size - 1 and self.get_square(
                    [square.file, square.row + 1]).piece.color != square.piece.color:
                available_moves.append([square.file, square.row + 1])

            if square.file - 1 >= 0 and square.row < self.size - 1:
                available_moves.append([square.file - 1, square.row + 1])

            if square.file - 1 >= 0 and self.get_square(
                    [square.file - 1, square.row]).piece.color != square.piece.color:
                available_moves.append([square.file - 1, square.row])

            if square.row - 1 >= 0 and self.get_square([square.file, square.row - 1]).piece.color != square.piece.color:
                available_moves.append([square.file, square.row - 1])

            if square.row - 1 >= 0 and square.file - 1 >= 0 and self.get_square(
                    [square.file - 1, square.row - 1]).piece.color != square.piece.color:
                available_moves.append([square.file - 1, square.row - 1])

        if square.piece.id == 'n':
            if square.row < self.size - 2:
                if square.file - 1 >= 0 and self.get_square(
                        [square.file - 1, square.row + 2]).piece.color != square.piece.color:
                    available_moves.append([square.file - 1, square.row + 2])
                if square.file + 1 <= self.size - 1 and self.get_square(
                        [square.file + 1, square.row + 2]).piece.color != square.piece.color:
                    available_moves.append([square.file + 1, square.row + 2])

            if square.file < self.size - 2:
                if square.row - 1 >= 0 and self.get_square(
                        [square.file + 2, square.row - 1]).piece.color != square.piece.color:
                    available_moves.append([square.file + 2, square.row - 1])
                if square.row + 1 <= self.size - 1 and self.get_square(
                        [square.file + 2, square.row + 1]).piece.color != square.piece.color:
                    available_moves.append([square.file + 2, square.row + 1])

            if square.row - 2 >= 0:
                if square.file - 1 >= 0 and self.get_square(
                        [square.file - 1, square.row - 2]).piece.color != square.piece.color:
                    available_moves.append([square.file - 1, square.row - 2])
                if square.file + 1 <= self.size - 1 and self.get_square(
                        [square.file + 1, square.row - 2]).piece.color != square.piece.color:
                    available_moves.append([square.file + 1, square.row - 2])

            if square.file - 2 >= 0:
                if square.row - 1 >= 0 and self.get_square(
                        [square.file - 2, square.row - 1]).piece.color != square.piece.color:
                    available_moves.append([square.file - 2, square.row - 1])
                if square.row + 1 <= self.size - 1 and self.get_square(
                        [square.file - 2, square.row + 1]).piece.color != square.piece.color:
                    available_moves.append([square.file - 2, square.row + 1])

        return available_moves

    def make_move(self, move):
        if self.get_square(move[0]).piece.id == 'p' and self.get_square(move[1]).piece.id == "none" and \
                move[0][0] != move[1][0] and self.get_square(move[0]).piece.color == 'w':
            self.get_square([move[1][0], move[1][1] + 1]).piece = Piece("none", "none")

        if self.get_square(move[0]).piece.id == 'p' and self.get_square(move[1]).piece.id == "none" and \
                move[0][0] != move[1][0] and self.get_square(move[0]).piece.color == 'b':
            self.get_square([move[1][0], move[1][1] - 1]).piece = Piece("none", "none")

        if move == "w0-0":
            self.make_move([WHITE_KING_STARTING_POSITION, WHITE_KINGS_KNIGHT_STARTING_POSITION])
            self.make_move([WHITE_KINGS_ROOK_STARTING_POSITION, WHITE_KINGS_BISHOP_STARTING_POSITION])
            return
        if move == "b0-0":
            self.make_move([BLACK_KING_STARTING_POSITION, WHITE_KINGS_KNIGHT_STARTING_POSITION])
            self.make_move([BLACK_KINGS_ROOK_STARTING_POSITION, WHITE_KINGS_BISHOP_STARTING_POSITION])
            return
        if move == "w0-0-0":
            self.make_move([WHITE_KING_STARTING_POSITION, WHITE_QUEENS_BISHOP_STARTING_POSITION])
            self.make_move([WHITE_QUEENS_ROOK_STARTING_POSITION, WHITE_QUEEN_STARTING_POSITION])
            return
        if move == "b0-0-0":
            self.make_move([BLACK_KING_STARTING_POSITION, BLACK_QUEENS_BISHOP_STARTING_POSITION])
            self.make_move([BLACK_KINGS_ROOK_STARTING_POSITION, BLACK_QUEEN_STARTING_POSITION])
            return

        self.get_square(move[1]).piece = self.get_square(move[0]).piece
        self.get_square(move[0]).piece = Piece("none", "none")

    def get_square(self, cord):
        return self.squares[cord[0]][cord[1]]

    def get_available_moves_by_color(self, color):
        legal_moves = []
        for row in self.squares:
            for square in row:
                if square.piece.color == color:
                    for move in self.available_moves(square.get_cord()):
                        legal_moves.append([square.get_cord(), move])
        return legal_moves

    def threatened_squares_by_color(self, color):
        squares = []
        moves = self.get_available_moves_by_color(color)
        for move in moves:
            squares.append(move[1])
        return squares

    def does_color_do_check(self, color):
        threats = self.threatened_squares_by_color(color)
        for threat in threats:
            if self.get_square(threat).piece.id == "k" and self.get_square(threat).piece.color != color:
                return True
        return False

    def legal_moves(self, color):
        legal_moves = []
        if color == "w":
            for move in self.get_available_moves_by_color(color):
                clone = copy.deepcopy(self)
                clone.make_move(move)
                if not clone.does_color_do_check("b"):
                    legal_moves.append(move)

        elif color == "b":
            for move in self.get_available_moves_by_color(color):
                clone = copy.deepcopy(self)
                clone.make_move(move)
                if not clone.does_color_do_check("w"):
                    legal_moves.append(move)
        return legal_moves
