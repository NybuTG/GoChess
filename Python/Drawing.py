import os, sys
import pygame
import itertools

from Backend import ProcessFen

class DrawBoard:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800), 0 , 32)

        # Light square and dark square colors
        self.colors = ((227, 237, 213, 255), (92, 105, 85, 255))

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
                    pygame.draw.rect(self.screen, self.colors[0], (file, rank, file + 100, rank + 100))
                else:
                    pygame.draw.rect(self.screen, self.colors[1], (file, rank, file + 100, rank + 100))


    def stringToList(self, string):

        outp = []
        for i in range(len(string)):
            
            if string[i].isdigit():
                outp.append(int(string[i]))
            else:
                outp.append(string[i])
            
        return outp

    def createPieces(self, fenString):
        layout = ProcessFen(fenString).fenToBoard()["board"]
        layout = list(itertools.chain.from_iterable(layout))
        layout = self.stringToList(layout)

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
            
            

        
    def preload(self):
        ...
    
    def draw(self):
        self.createBoard()
        self.createPieces("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
        pygame.display.flip()
        