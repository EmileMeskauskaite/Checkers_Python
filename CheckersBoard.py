import pygame

from CheckerPiece import CheckerPiece
from main import WIDTH, HEIGHT, WHITE, BOARD_SIZE, SQUARE_SIZE, BLUE, BROWN, BLACK


class CheckersBoard:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")
        self.pieces = []
        self.setup_pieces()
        self.current_player = BROWN
        self.selected_piece = None

    def setup_pieces(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.pieces.append(CheckerPiece(self.screen, BROWN, row, col))
                    elif row >= BOARD_SIZE - 3:
                        self.pieces.append(CheckerPiece(self.screen, BLUE, row, col))

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(self.screen, color, (
                    col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw_piece()

    def handle_click(self, pos):
        col, row = pos[0] // (WIDTH // BOARD_SIZE), pos[1] // (HEIGHT // BOARD_SIZE)
        clicked_piece = self.get_piece_at(row, col)

        if clicked_piece and clicked_piece.color == self.current_player:
            self.handle_selected_piece(clicked_piece)
        elif self.selected_piece:
            self.move_piece(self.selected_piece, row, col)

    def handle_selected_piece(self, clicked_piece):
        if self.selected_piece:
            self.selected_piece.selected = False

        clicked_piece.selected = True
        self.selected_piece = clicked_piece

    def move_piece(self, piece, row, col):
        if not self.is_valid_move(piece, row, col):
            return

        if abs(row - piece.row) == 2 and abs(col - piece.col) == 2:
            self.remove_opponent_piece(piece, (row, col))

        piece.row, piece.col = row, col

        if row in {0, BOARD_SIZE - 1}:
            piece.king = True

        piece.selected = False
        self.selected_piece = None
        self.switch_player()

    def is_valid_move(self, piece, row, col):
        if not (0 <= row < BOARD_SIZE) or not (0 <= col < BOARD_SIZE):
            return False

        direction = 1 if piece.color == BROWN else -1

        if abs(row - piece.row) == 1 and abs(col - piece.col) == 1:
            if piece.king:
                return abs(row - piece.row) == 1 and abs(col - piece.col) == 1
            else:
                return (row - piece.row) * direction > 0 and self.is_target_empty(row, col)

        if abs(row - piece.row) == 2 and abs(col - piece.col) == 2:
            return self.is_jump_move(piece, row, col, direction)

        return False

    def find_opponent_piece(self, jumped_row, jumped_col):
        for opponent_piece in self.pieces:
            if opponent_piece.row == jumped_row and opponent_piece.col == jumped_col:
                return opponent_piece
        return None

    def is_normal_move(self, piece, row, col, direction):
        return (row - piece.row) * direction > 0 and self.is_target_empty(row, col)

    def is_jump_move(self, piece, row, col, direction):
        jumped_row = (piece.row + row) // 2
        jumped_col = (piece.col + col) // 2

        for opponent_piece in self.pieces:
            if opponent_piece.row == jumped_row and opponent_piece.col == jumped_col:
                if opponent_piece.color != piece.color and self.is_target_empty(row, col):
                    if piece.king:
                        return True
                    return (row - piece.row) * direction > 0

        return False

    def remove_opponent_piece(self, piece, target):
        jumped_row, jumped_col = self.find_jumped_coordinates(piece, target)

        opponent_piece = self.find_opponent_piece(jumped_row, jumped_col)
        if opponent_piece:
            self.pieces.remove(opponent_piece)

    def find_jumped_coordinates(self, piece, target):
        jumped_row = (piece.row + target[0]) // 2
        jumped_col = (piece.col + target[1]) // 2
        return jumped_row, jumped_col

    def is_target_empty(self, row, col):
        return all(piece.row != row or piece.col != col for piece in self.pieces)

    def get_piece_at(self, row, col):
        return next((piece for piece in self.pieces if piece.row == row and piece.col == col), None)

    def place_piece_at(self, piece, row, col, color):
        piece.row, piece.col = row, col
        piece.color = color

    def switch_player(self):
        self.current_player = BLUE if self.current_player == BROWN else BROWN

    def check_winner(self):
        brown_pieces = sum(1 for piece in self.pieces if piece.color == BROWN)
        blue_pieces = sum(1 for piece in self.pieces if piece.color == BLUE)

        return "Blue" if brown_pieces == 0 else ("Brown" if blue_pieces == 0 else None)
