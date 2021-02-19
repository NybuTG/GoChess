import pygame
import sys

class Moves():

    def __init__(self):
        self.tempString = [
        'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
        'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 
        8, 8, 8, 8, 
        'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
        'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

        
    def getLegalMoves(self, pieceSq, coords):
        legalMoves = []

        # Converts the number on the chess board to an array index
        for i in range(len(self.tempString)):

            if isinstance(self.tempString[i], int):
                pieceSq -= (self.tempString[i] - 1)
        
        piece = self.tempString[pieceSq]
        if piece == "P":
            if coords[1] == 6:
                # legalMoves = [[coords[0], coords[1]+1], [coords[0], coords[1]+2][]
                legalMoves = [[coords[0], coords[1] - 1], [coords[0], coords[1] - 2]]
            else:
                legalMoves = [coords[0], coords[1] - 1]

        

        return legalMoves

    
    def selectPiece(self):
        ...

    def handleKeys(self):        
        ...

if __name__ == "__main__":

    legal = Moves()
    print(legal.getLegalMoves(50, (4, 6)))