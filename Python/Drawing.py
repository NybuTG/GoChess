import os, sys
import pygame
import itertools

from Backend import ProcessFen

class DrawBoard:

    def __init__(self, fenString):
        self.screen = pygame.display.set_mode((800, 800), 0 , 32)
        self.fenString = fenString
        # Light square and dark square colors
        self.colors = ((242, 242, 223), (128,5,0))
        self.markedSquares = []
        self.pieces = {

            # Black
            "b": pygame.image.load(os.path.join("Sprites", "b_b.png")),     # Bishop
            "k": pygame.image.load(os.path.join("Sprites", "k_b.png")),     # King
            "n": pygame.image.load(os.path.join("Sprites", "n_b.png")),     # Knight
            "q": pygame.image.load(os.path.join("Sprites", "q_b.png")),     # Queen
            "p": pygame.image.load(os.path.join("Sprites", "p_b.png")),     # Pawn
            "r": pygame.image.load(os.path.join("Sprites", "r_b.png")),     # Rook

            # White
            "B": pygame.image.load(os.path.join("Sprites", "b_w.png")),     # Bishop
            "K": pygame.image.load(os.path.join("Sprites", "k_w.png")),     # King
            "N": pygame.image.load(os.path.join("Sprites", "n_w.png")),     # Knight
            "Q": pygame.image.load(os.path.join("Sprites", "q_w.png")),     # Queen
            "P": pygame.image.load(os.path.join("Sprites", "p_w.png")),     # Pawn
            "R": pygame.image.load(os.path.join("Sprites", "r_w.png")),     # Rook

        }

        for pcs in self.pieces:
            self.pieces[pcs] = pygame.transform.smoothscale(self.pieces[pcs], (100, 100))

    def createBoard(self):

        for rank in range(0, 800, 100):
            
            for file in range(0, 800, 100):  
                
                if (file + rank) % 200 == 0:
                    pygame.draw.rect(self.screen, self.colors[0], (file, rank, 100, 100))
                else:
                    pygame.draw.rect(self.screen, self.colors[1], (file, rank, 100, 100))
    
    def mergeCoords(self, lst):
        flat_list = []
        # Iterate through the outer list
        for element in lst:
            if type(element) is list:
                # If the element is of type list, iterate through the sublist
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list

            
    def markSquare(self, pos):
        
        # Horrible code lmao
        self.markedSquares.clear()
        self.markedSquares.append(pos)
        self.markedSquares = self.mergeCoords(self.mergeCoords(self.markedSquares))
        
        self.markedSquares[0] = [self.markedSquares[0], self.markedSquares[1]]
        self.markedSquares.pop(1)

        print(self.markedSquares)

    def drawMarkedSquare(self):

        # print(markedSquares) 
        for i in range(len(self.markedSquares)):

            s = pygame.Surface((100,100))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((153,186,221))           # this fills the entire surface
            self.screen.blit(s, (self.markedSquares[i][0] * 100, self.markedSquares[i][1] * 100))   # (0,0) are the top-left coordinates

    def createPieces(self, fenString):

        layout = ProcessFen(fenString).fenToBoard()["board"]
        ranks = 0
        files = 0
        
        for i in range(len(layout)):
            
            if isinstance(layout[i], int) == False:
                self.screen.blit(self.pieces[layout[i]], (ranks, files))
                ranks+=100
            else:
                ranks += layout[i] * 100
               
            if ranks == 800:
                ranks = 0
                files += 100
            
    def draw(self):
        self.createBoard()
        self.drawMarkedSquare()
        self.createPieces(self.fenString)
        pygame.display.flip()
        