class Board(): 
    def __init__(self) -> None:
        # Membuat board dengan array 2 dimensi
        self.board = [[0 for x in range(3)] for y in range(3)]

    def drawBoard(self):
        # Convert board agar rapih saat diprint
        board = [["  " if x == 0 else x.name for x in self.board[i]] for i, _ in enumerate(self.board)]
        print()
        print("  " + board[0][0] + "  |  " + board[0][1] + "   |  " + board[0][2])
        print("[0,0] | [0,1] | [0,2]")
        print("---------------------")
        print("  " + board[1][0] + "  |  " + board[1][1] + "   |  " + board[1][2])
        print("[1,0] | [1,1] | [1,2]")
        print("---------------------")
        print("  " + board[2][0] + "  |  " + board[2][1] + "   |  " + board[2][2])
        print("[2,0] | [2,1] | [2,2]")

    def registerStep(self, x, y, level, player):
        # Jika input langkah merupakan langkah yang valid,
        # keluarkan piece yang diminta dari array pieces_left,
        # lalu masukkan ke dalam board.
        if self.isValidMove(x,y, level):
            self.board[x][y] = player.pieces_left[level].pop()
            return True

    def isValidMove(self,x,y,level):
        # Cek apakah langkah adalah valid
        if self.board[x][y] == 0 or self.board[x][y].level < level:
            return True
        print("\n[!] Langkah tidak diperbolehkan!")
        return False
    
    def getAliasOnly(self):
        # Convert papan menjadi alias
        return [[0 if x == 0 else x.side for x in self.board[i]] for i, _ in enumerate(self.board)]