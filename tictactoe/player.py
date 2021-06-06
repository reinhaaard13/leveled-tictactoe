from .piece import Piece

class Player():
    def __init__(self, alias):
        self.alias = alias # alias dari player (X/Y)
        self.pieces_left = [
            [Piece(alias,0) for x in range(3)], # Piece level 0
            [Piece(alias,1) for x in range(3)], # Piece level 1
            [Piece(alias,2) for x in range(3)] # Piece level 2
        ]