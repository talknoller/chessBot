class Square:
    def __init__(self, file, row, color, piece, white_threats, black_threats):
        self.row = row
        self.file = file
        self.color = color
        self.piece = piece
        self.white_threats = white_threats
        self.black_threats = black_threats
        self.board_size = 8

    def available_moves(self):
        if self.piece is None:
            print("empty square")
            return []

        available_moves = []
        if self.piece.id == 'p' and self.piece.color == 'b':
            if self.row < self.board_size:
                available_moves.append([self.file, self.row + 1])
                if self.file < self.board_size:
                    available_moves.append([self.file + 1, self.row + 1])
                if self.file > 0:
                    available_moves.append([self.file - 1, self.row + 1])
            if self.row == 1:
                available_moves.append([self.file, self.row + 2])

        if self.piece.id == 'p' and self.piece.color == 'b':
            if self.row > 0:
                available_moves.append([self.file, self.row - 1])
                if self.file < self.board_size:
                    available_moves.append([self.file + 1, self.row - 1])
                if self.file > 0:
                    available_moves.append([self.file - 1, self.row - 1])

        if self.piece.id == 'r' or self.piece.id == 'q':
            for i in range(self.row + 1, self.board_size):
                available_moves.append([self.file, i])

            for i in range(self.row - 1, -1, -1):
                available_moves.append([self.file, i])

            for i in range(self.file + 1, self.board_size):
                available_moves.append([i, self.row])

            for i in range(self.file - 1, -1, -1):
                available_moves.append([i, self.row])

            if self.piece.id == 'b' or self.piece.id == 'q':
                row = self.row + 1
                file = self.file + 1

                while file < self.board_size and row < self.board_size:
                    available_moves.append([file, row])
                    row += 1
                    file += 1

                row = self.row - 1
                file = self.file - 1

                while file >= 0 and row >= 0:
                    available_moves.append([file, row])
                    row -= 1
                    file -= 1

                row = self.row - 1
                file = self.file + 1

                while file < self.board_size and row >= 0:
                    available_moves.append([file, row])
                    row -= 1
                    file += 1

                row = self.row + 1
                file = self.file - 1

                while file >= 0 and row < self.board_size:
                    available_moves.append([file, row])
                    row += 1
                    file -= 1

        if self.piece.id == 'k':
            if self.row < self.board_size - 1 and self.file < self.board_size - 1:
                available_moves.append([self.file + 1, self.row + 1])

            if self.file < self.board_size - 1:
                available_moves.append([self.file + 1, self.row])
                if self.row - 1 >= 0:
                    available_moves.append([self.file + 1, self.row - 1])

            if self.row < self.board_size - 1:
                available_moves.append([self.file, self.row + 1])
                if self.file - 1 >= 0:
                    available_moves.append([self.file - 1, self.row + 1])

            if self.file - 1 >= 0:
                available_moves.append([self.file - 1, self.row])

            if self.row - 1 >= 0:
                available_moves.append([self.file, self.row - 1])

            if self.row - 1 >= 0 and self.file - 1 >= 0:
                available_moves.append([self.file - 1, self.row - 1])

        if self.piece.id == 'n':
            if self.row < self.board_size - 2:
                if self.file - 1 > 0:
                    available_moves.append([self.file - 1, self.row + 2])
                if self.file + 1 < self.board_size - 1:
                    available_moves.append([self.file + 1, self.row + 2])

            if self.file < self.board_size - 2:
                if self.row - 1 > 0:
                    available_moves.append([self.file + 2, self.row - 1])
                if self.row + 1 < self.board_size - 1:
                    available_moves.append([self.file + 2, self.row + 1])

            if self.row - 2 > 0:
                if self.file - 1 > 0:
                    available_moves.append([self.file - 1, self.row - 2])
                if self.file + 1 < self.board_size - 1:
                    available_moves.append([self.file + 1, self.row - 2])

            if self.file - 2 > 0:
                if self.row - 1 > 0:
                    available_moves.append([self.file - 2, self.row - 1])
                if self.row + 1 < self.board_size - 1:
                    available_moves.append([self.file - 2, self.row + 1])

        return available_moves
