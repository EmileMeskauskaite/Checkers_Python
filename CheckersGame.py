import sys
import pygame
from CheckersBoard import CheckersBoard
from main import WIDTH, HEIGHT, WHITE


class CheckersGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = CheckersBoard()

    def run(self):
        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.board.handle_click(pos)

            self.screen.fill(WHITE)
            self.board.draw_board()
            self.board.draw_pieces()
            pygame.display.flip()

            winner = self.board.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                running = False

        pygame.quit()
        sys.exit()
