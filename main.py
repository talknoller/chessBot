from board import Board, move_to_string
from constants import *
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


def create_game_starting_position():
    game = Game(generate_board(), "w")

    w_a_pawn = Piece('p', 'w')
    w_b_pawn = Piece('p', 'w')
    w_c_pawn = Piece('p', 'w')
    w_d_pawn = Piece('p', 'w')
    w_e_pawn = Piece('p', 'w')
    w_f_pawn = Piece('p', 'w')
    w_g_pawn = Piece('p', 'w')
    w_h_pawn = Piece('p', 'w')

    w_k_rook = Piece('r', 'w')
    w_q_rook = Piece('r', 'w')
    w_k_knight = Piece('n', 'w')
    w_q_knight = Piece('n', 'w')
    w_k_bishop = Piece('b', 'w')
    w_q_bishop = Piece('b', 'w')
    w_queen = Piece('q', 'w')
    w_king = Piece('k', 'w')

    b_a_pawn = Piece('p', 'b')
    b_b_pawn = Piece('p', 'b')
    b_c_pawn = Piece('p', 'b')
    b_d_pawn = Piece('p', 'b')
    b_e_pawn = Piece('p', 'b')
    b_f_pawn = Piece('p', 'b')
    b_g_pawn = Piece('p', 'b')
    b_h_pawn = Piece('p', 'b')

    b_k_rook = Piece('r', 'b')
    b_q_rook = Piece('r', 'b')
    b_k_knight = Piece('n', 'b')
    b_q_knight = Piece('n', 'b')
    b_k_bishop = Piece('b', 'b')
    b_q_bishop = Piece('b', 'b')
    b_queen = Piece('q', 'b')
    b_king = Piece('k', 'b')

    # game.board.get_square(WHITE_KINGS_ROOK_STARTING_POSITION).piece = w_k_rook
    # game.board.get_square(WHITE_KINGS_KNIGHT_STARTING_POSITION).piece = w_k_knight
    # game.board.get_square(WHITE_KINGS_BISHOP_STARTING_POSITION).piece = w_k_bishop
    # game.board.get_square(WHITE_KING_STARTING_POSITION).piece = w_king
    # game.board.get_square(WHITE_QUEEN_STARTING_POSITION).piece = w_queen
    # game.board.get_square(WHITE_QUEENS_ROOK_STARTING_POSITION).piece = w_q_rook
    # game.board.get_square(WHITE_QUEENS_KNIGHT_STARTING_POSITION).piece = w_q_knight
    # game.board.get_square(WHITE_QUEENS_BISHOP_STARTING_POSITION).piece = w_q_bishop

    game.board.get_square(WHITE_A_PAWN_STARTING_POSITION).piece = w_a_pawn
    game.board.get_square(WHITE_B_PAWN_STARTING_POSITION).piece = w_b_pawn
    # game.board.get_square(WHITE_C_PAWN_STARTING_POSITION).piece = w_c_pawn
    # game.board.get_square(WHITE_D_PAWN_STARTING_POSITION).piece = w_d_pawn
    # game.board.get_square(WHITE_E_PAWN_STARTING_POSITION).piece = w_e_pawn
    # game.board.get_square(WHITE_F_PAWN_STARTING_POSITION).piece = w_f_pawn
    # game.board.get_square(WHITE_G_PAWN_STARTING_POSITION).piece = w_g_pawn
    # game.board.get_square(WHITE_H_PAWN_STARTING_POSITION).piece = w_h_pawn
    #
    # game.board.get_square(BLACK_KINGS_ROOK_STARTING_POSITION).piece = b_k_rook
    # game.board.get_square(BLACK_KINGS_KNIGHT_STARTING_POSITION).piece = b_k_knight
    # game.board.get_square(BLACK_KINGS_BISHOP_STARTING_POSITION).piece = b_k_bishop
    # game.board.get_square(BLACK_KING_STARTING_POSITION).piece = b_king
    # game.board.get_square(BLACK_QUEEN_STARTING_POSITION).piece = b_queen
    # game.board.get_square(BLACK_QUEENS_ROOK_STARTING_POSITION).piece = b_q_rook
    # game.board.get_square(BLACK_QUEENS_KNIGHT_STARTING_POSITION).piece = b_q_knight
    # game.board.get_square(BLACK_QUEENS_BISHOP_STARTING_POSITION).piece = b_q_bishop

    game.board.get_square(BLACK_A_PAWN_STARTING_POSITION).piece = b_a_pawn
    game.board.get_square(BLACK_B_PAWN_STARTING_POSITION).piece = b_b_pawn
    # game.board.get_square(BLACK_C_PAWN_STARTING_POSITION).piece = b_c_pawn
    # game.board.get_square(BLACK_D_PAWN_STARTING_POSITION).piece = b_d_pawn
    # game.board.get_square(BLACK_E_PAWN_STARTING_POSITION).piece = b_e_pawn
    # game.board.get_square(BLACK_F_PAWN_STARTING_POSITION).piece = b_f_pawn
    # game.board.get_square(BLACK_G_PAWN_STARTING_POSITION).piece = b_g_pawn
    # game.board.get_square(BLACK_H_PAWN_STARTING_POSITION).piece = b_h_pawn
    return game


game = create_game_starting_position()
game.make_move([[0,1], [0,3]])
game.make_move([[0,6], [0,4]])
game.make_move([[1,1], [1,3]])
game.make_move([[0,4], [1,3]])


game.board.print_board()
