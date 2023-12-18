import pygame

from main import CIRCLE_SIZE


class CheckerPiece:
    def __init__(self, screen, color, row, col):
        self.screen = screen
        self.color = color
        self.row = row
        self.col = col
        self.CIRCLE_SIZE = CIRCLE_SIZE
        self.king = False
        self.selected = False

    def draw_piece(self):
        pygame.draw.circle(self.screen, self.color, (
            self.col * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2,
            self.row * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2), self.CIRCLE_SIZE // 2)

        if self.king:
            pygame.draw.circle(self.screen, (255, 255, 0), (
                self.col * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2,
                self.row * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2), self.CIRCLE_SIZE // 4)

        if self.selected:
            pygame.draw.circle(self.screen, (255, 0, 0), (
                self.col * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2,
                self.row * self.CIRCLE_SIZE + self.CIRCLE_SIZE // 2), self.CIRCLE_SIZE // 4)
