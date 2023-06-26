def is_square_in_list(square_cord_list, square_cord):
    for square in square_cord_list:
        if square[0] == square_cord[0] and square[1] == square_cord[1]:
            return True
    return False


def array_to_cord(cord_array):
    if cord_array[0] > 7 or cord_array[0] < 0 or cord_array[1] > 7 or cord_array[1] < 0:
        return "invalid cords"

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return files[cord_array[0]] + str(cord_array[1] + 1)


class Board:
    def __init__(self, squares):
        self.squares = squares
        self.size = 8

    def print_pieces(self):
        for row in self.squares:
            for square in row:
                if square.piece is not None:
                    print(square.piece.id + " is at " + array_to_cord([square.file, square.row]))

    def legal_moves(self, square_cord):
        if square_cord[0] >= self.size or square_cord[1] >= self.size:
            print("square doesn't exist")
            return []
        square = self.squares[square_cord[0]][square_cord[1]]
        if square.piece is None:
            print("empty square")
            return []

        available_moves = []
        if square.piece.id == 'p' and square.piece.color == 'b':
            if square.row < self.size:
                available_moves.append([square.file, square.row + 1])
                if square.file < self.size:
                    available_moves.append([square.file + 1, square.row + 1])
                if square.file > 0:
                    available_moves.append([square.file - 1, square.row + 1])
            if square.row == 1:
                available_moves.append([square.file, square.row + 2])

        if square.piece.id == 'p' and square.piece.color == 'b':
            if square.row > 0:
                available_moves.append([square.file, square.row - 1])
                if square.file < self.size:
                    available_moves.append([square.file + 1, square.row - 1])
                if square.file > 0:
                    available_moves.append([square.file - 1, square.row - 1])

        if square.piece.id == 'r' or square.piece.id == 'q':
            for i in range(square.row + 1, self.size):
                available_moves.append([square.file, i])

            for i in range(square.row - 1, -1, -1):
                available_moves.append([square.file, i])

            for i in range(square.file + 1, self.size):
                available_moves.append([i, square.row])

            for i in range(square.file - 1, -1, -1):
                available_moves.append([i, square.row])

            if square.piece.id == 'b' or square.piece.id == 'q':
                row = square.row + 1
                file = square.file + 1

                while file < self.size and row < self.size:
                    available_moves.append([file, row])
                    row += 1
                    file += 1

                row = square.row - 1
                file = square.file - 1

                while file >= 0 and row >= 0:
                    available_moves.append([file, row])
                    row -= 1
                    file -= 1

                row = square.row - 1
                file = square.file + 1

                while file < self.size and row >= 0:
                    available_moves.append([file, row])
                    row -= 1
                    file += 1

                row = square.row + 1
                file = square.file - 1

                while file >= 0 and row < self.size:
                    available_moves.append([file, row])
                    row += 1
                    file -= 1

        if square.piece.id == 'k':
            if square.row < self.size - 1 and square.file < self.size - 1:
                available_moves.append([square.file + 1, square.row + 1])

            if square.file < self.size - 1:
                available_moves.append([square.file + 1, square.row])
                if square.row - 1 >= 0:
                    available_moves.append([square.file + 1, square.row - 1])

            if square.row < self.size - 1:
                available_moves.append([square.file, square.row + 1])
                if square.file - 1 >= 0:
                    available_moves.append([square.file - 1, square.row + 1])

            if square.file - 1 >= 0:
                available_moves.append([square.file - 1, square.row])

            if square.row - 1 >= 0:
                available_moves.append([square.file, square.row - 1])

            if square.row - 1 >= 0 and square.file - 1 >= 0:
                available_moves.append([square.file - 1, square.row - 1])

        if square.piece.id == 'n':
            if square.row < self.size - 2:
                if square.file - 1 >= 0:
                    available_moves.append([square.file - 1, square.row + 2])
                if square.file + 1 <= self.size - 1:
                    available_moves.append([square.file + 1, square.row + 2])

            if square.file < self.size - 2:
                if square.row - 1 >= 0:
                    available_moves.append([square.file + 2, square.row - 1])
                if square.row + 1 <= self.size - 1:
                    available_moves.append([square.file + 2, square.row + 1])

            if square.row - 2 >= 0:
                if square.file - 1 >= 0:
                    available_moves.append([square.file - 1, square.row - 2])
                if square.file + 1 <= self.size - 1:
                    available_moves.append([square.file + 1, square.row - 2])

            if square.file - 2 >= 0:
                if square.row - 1 >= 0:
                    available_moves.append([square.file - 2, square.row - 1])
                if square.row + 1 <= self.size - 1:
                    available_moves.append([square.file - 2, square.row + 1])

        return available_moves

    def make_move(self, current_square_cord, desired_square_cord):
        moves = self.legal_moves(current_square_cord)
        if len(moves) == 0 or not is_square_in_list(moves, desired_square_cord):
            print("illegal move")
            return

        self.squares[desired_square_cord[0]][desired_square_cord[1]].piece = self.squares[current_square_cord[0]][current_square_cord[1]].piece
        self.squares[current_square_cord[0]][current_square_cord[1]].piece = None
