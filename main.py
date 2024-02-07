import pygame
from constants import *
from board import GridDrawer

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen.fill(GRID_COLOR)
    pygame.display.set_caption(TITLE)
    
    gridBoard = GridDrawer(8, 8, 100, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    gridBoard.init_grid()
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
