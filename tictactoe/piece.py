class Piece():
    def __init__(self, alias, level=0):
        self.side = alias # side -> X/O
        self.name = alias + str(level) # name -> X0/X1/X2/O0/O1/O2
        self.level = level # level -> 0/1/2