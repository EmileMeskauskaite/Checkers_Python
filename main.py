WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
CIRCLE_SIZE = WIDTH // BOARD_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 76, 60)
BLUE = (0, 90, 150)


if __name__ == "__main__":
    import pygame
    from CheckersGame import CheckersGame

    pygame.init()

    game = CheckersGame()
    game.run()

    pygame.quit()