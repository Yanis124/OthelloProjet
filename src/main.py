import pygame
from src.constants import *
from src.grid.board import Grid

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    gridBoard = Grid(GRID_WIDTH, GRID_HEIGHT, 100, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    pygame.display.flip()
    
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gridBoard.handle_click(event)
            pygame.display.flip()

if __name__ == "__main__":
    main()
