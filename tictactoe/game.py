from .player import Player
from .board import Board

class Game():
    def __init__(self):
        self.winner = None
        self.player = [Player('X'), Player('O')]
        self.board = Board()
        self.turn = 0 # 0 -> X ; 1 -> Y
    
    def inputStep(self):
        # Menampilkan papan tic tac toe saat ini dan meminta input langkah
        self.board.drawBoard()
        print(f"\n[ {self.player[self.turn].alias}'s turn! ]")
        step = input(f"\n[?] Langkah {self.player[self.turn].alias} (x,y): ")

        # Menampilkan pion tersedia di masing-masing level
        print(f"\n[Pion Tersedia]\n\tLv0: {len(self.player[self.turn].pieces_left[0])}\n\tLv1: {len(self.player[self.turn].pieces_left[1])}\n\tLv2: {len(self.player[self.turn].pieces_left[2])}")
        level = input(f"Pilih level pion : ")

        # Exception handling false format input
        try:
            level = int(level)
            step.replace(" ","")
            x, y = step.split(',')
            x, y = int(x), int(y)
        except ValueError:
            print("\n[!] Input error! [!]")
            return

        # Validasi nilai input
        if self.checkInputs(level,x,y):
            # Register step yang diinput
            if self.board.registerStep(x,y,level,self.player[self.turn]):
                # Ganti giliran
                self.turn = 1 if self.turn == 0 else 0
    
    def checkInputs(self, level, x, y):
        # Periksa input level hanya bisa 0 - 2
        if level > 2 or level < 0:
            print("Input level salah!")
            return False
        # Periksa input step hanya bisa 0 - 2
        if (
            x < 0 or
            x > 2 or
            y < 0 or
            y > 2
        ):
            print("Input langkah salah!")
            return False
        # Periksa apakah player masih punya bidak dengan level dipilih
        if len(self.player[self.turn].pieces_left[level]) <= 0:
            print("Input Salah!")
            return False
        return True

    def checkWinner(self):
        # Memeriksa apakah ada yang sudah menang
        board = self.board.getAliasOnly() # Meminta papan yang berisi alias (X/Y) bukan objek Piece()
        side = self.player[1 if self.turn == 0 else 0].alias
        if (
            (board[0][0] == side and board[0][1] == side and board[0][2] == side) or
            (board[1][0] == side and board[1][1] == side and board[1][2] == side) or
            (board[2][0] == side and board[2][1] == side and board[2][2] == side) or
            (board[0][0] == side and board[1][0] == side and board[2][0] == side) or
            (board[0][1] == side and board[1][1] == side and board[2][1] == side) or
            (board[0][2] == side and board[1][2] == side and board[2][2] == side) or
            (board[0][0] == side and board[1][1] == side and board[2][2] == side) or
            (board[2][0] == side and board[1][1] == side and board[0][2] == side)
        ):
            print('\n[', side,"wins the game! ]")
            return True
        