import pygame, sys
from pygame.locals import QUIT

from Drawing import DrawBoard

if __name__ == "__main__":
    
    STARTFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = DrawBoard()
    
    board.preload()
    while True:
        
        board.draw()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    
    
