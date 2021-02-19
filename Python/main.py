import pygame, sys
from pygame.locals import *

from MoveHandling import Moves
from Drawing import DrawBoard

class Main:

    def __init__(self):
        self.STARTFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        game = DrawBoard(self.STARTFEN)

        while True:
            game.draw()
            self.eventHandler(game)
            
    def mouseToGrid(self):
        pos = pygame.mouse.get_pos()
        x = [int(x) for x in str(pygame.mouse.get_pos()[0])]
        y = [int(x) for x in str(pygame.mouse.get_pos()[1])]
        pos = [x, y]
        
        for i in range(len(pos)):
            if len(pos[i]) != 3:
                pos[i] = 0
            
            else:
                pos[i] = pos[i][0]
        
        sq = (pos[1] * 8) + pos[0]

        return (sq, pos)

    def eventHandler(self, game):
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                sq, pos = self.mouseToGrid()
                # print(sq, pos)    
                legalMoves = Moves().getLegalMoves(sq, pos)
                game.markSquare([pos, legalMoves])

if __name__ == "__main__":
    
    Main()
    