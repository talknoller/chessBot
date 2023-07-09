from constants import *


class Game:
    def __init__(self, board, color_turn, white_king_castle=True, white_queen_castle=True, black_king_castle=True,
                 black_queen_castle=True):
        self.board = board
        self.color_turn = color_turn
        self.white_king_castle = white_king_castle
        self.white_queen_castle = white_queen_castle
        self.black_king_castle = black_king_castle
        self.black_queen_castle = black_queen_castle
        self.last_pawn_double_push = [7, 4]

    def legal_moves(self):
        moves = self.board.legal_moves(self.color_turn)
        if self.color_turn == "w" and self.white_king_castle and \
                self.board.get_square(WHITE_KING_STARTING_POSITION).piece.id == "k" and \
                self.board.get_square(WHITE_KING_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(WHITE_KINGS_ROOK_STARTING_POSITION).piece.id == "r" and \
                self.board.get_square(WHITE_KINGS_ROOK_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(WHITE_KINGS_KNIGHT_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(WHITE_KINGS_BISHOP_STARTING_POSITION).piece.id == "none":
            moves.append("w0-0")

        if self.color_turn == "b" and self.white_king_castle and \
                self.board.get_square(BLACK_KING_STARTING_POSITION).piece.id == "k" and \
                self.board.get_square(BLACK_KING_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(BLACK_KINGS_ROOK_STARTING_POSITION).piece.id == "r" and \
                self.board.get_square(BLACK_KINGS_ROOK_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(BLACK_KINGS_KNIGHT_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(BLACK_KINGS_BISHOP_STARTING_POSITION).piece.id == "none":
            moves.append("b0-0")

        if self.color_turn == "w" and self.white_king_castle and \
                self.board.get_square(WHITE_KING_STARTING_POSITION).piece.id == "k" and \
                self.board.get_square(WHITE_KING_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(WHITE_QUEENS_ROOK_STARTING_POSITION).piece.id == "r" and \
                self.board.get_square(WHITE_QUEENS_ROOK_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(WHITE_QUEENS_KNIGHT_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(WHITE_QUEENS_BISHOP_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(WHITE_QUEEN_STARTING_POSITION).piece.id == "none":
            moves.append("w0-0-0")

        if self.color_turn == "b" and self.white_king_castle and \
                self.board.get_square(BLACK_KING_STARTING_POSITION).piece.id == "k" and \
                self.board.get_square(BLACK_KING_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(BLACK_QUEENS_ROOK_STARTING_POSITION).piece.id == "r" and \
                self.board.get_square(BLACK_QUEENS_ROOK_STARTING_POSITION).piece.color == "w" and \
                self.board.get_square(BLACK_QUEENS_KNIGHT_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(BLACK_QUEENS_BISHOP_STARTING_POSITION).piece.id == "none" and \
                self.board.get_square(BLACK_QUEEN_STARTING_POSITION).piece.id == "none":
            moves.append("b0-0-0")

        if self.last_pawn_double_push is not None and self.last_pawn_double_push[0] + 1 < self.board.size and \
                self.board.get_square([(self.last_pawn_double_push[0] + 1), self.last_pawn_double_push[1]]).piece.id \
                == "p" and self.color_turn == 'w':
            moves.append([[(self.last_pawn_double_push[0] + 1), self.last_pawn_double_push[1]],
                          [(self.last_pawn_double_push[0]), self.last_pawn_double_push[1] + 1]])

        if self.last_pawn_double_push is not None and self.last_pawn_double_push[0] - 1 > 0 and \
                self.board.get_square([(self.last_pawn_double_push[0] - 1), self.last_pawn_double_push[1]]).piece.id \
                == "p" and self.color_turn == 'w':
            moves.append([[(self.last_pawn_double_push[0] - 1), self.last_pawn_double_push[1]],
                          [(self.last_pawn_double_push[0]), self.last_pawn_double_push[1] + 1]])

        return moves

    def make_move(self, move):
        legal_moves = self.legal_moves()
        for legal_move in legal_moves:
            if move == legal_move:
                if self.color_turn == 'w':
                    self.color_turn = 'b'
                else:
                    self.color_turn = 'w'
                self.board.make_move(move)
