from tictactoe.game import Game

def main():
    # Instansiasi objek game
    game = Game()
    run = True

    print("\n=== [[ LEVELED TIC TAC TOE ]] ===")
    print("# Developed by Reinhard Kevin 2019104402")
    
    while run:
        game.inputStep()

        if game.checkWinner(): # Cek apakah ada pemenang
            if restartGame(): # Cek apakah user ingin main ulang
                game = Game()
            else: 
                print('\n[#] Thank you for playing! - by Reinhard Kevin [#]')
                run = False

def restartGame():
    res = input("\n[?] Do you want to play again? [y/n] : ").lower()
    if res == 'y':
        return True
    elif res == 'n':
        return False
    else:
        print('\n[!] Wrong Value. [!]')
        return restartGame()

if __name__ == "__main__":
    main()