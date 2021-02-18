import pprint

class ProcessFen:
    # Okay jesus this will need some explaining for later me..
    ####
    # Starting pos in FEN: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    # There are in a way 6 parts to this - part 0 is: The space is a seperator
    
    # 1 | The string is described from whites perspective - You move top to bottom - 2 rows of black pieces, two rows of nothing then two rows of white pieces
    #  a "/" is a line seperator - Capitals are white, lowers are black
    # 2 | active color
    # 3 | Can castle? K: White can castle kingside - Q: White can castle queenside - k: black can castle kingside - q: black can castle queenside, - is a false
    # 4 | En Passant, - is a false
    # 5 | Halfmove clock
    # 6 | Fullmove number
    

    def __init__(self, fenString):
        self.fenString = fenString

    def fenToBoard(self):
        # Split that long string into segments
        steps = self.fenString.split()


        board = steps[0].split("/")

        for i in range(len(board)):
            board[i] = [char for char in board[i]]

        # Return the payload with data
        return {
            "board": board,
            "turn": steps[1],
            "canCastle": steps[2],
            "canEnPassant": steps[3],
            "halfMoveClock": steps[4],
            "fullMoveNumber": steps[5]
        }

if __name__ == "__main__":
    fen = ProcessFen("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
    pprint.pprint(fen.fenToBoard())
                 

        
            

