# 1. The Game Board
# A list of 9 dashes representing the 9 squares of the board



board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

# 2. Game Functions
def display_board():
    print("\n")
    print("_____________")
    print("|---|---|---|")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("|---|---|---|")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("|---|---|---|")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("|---|---|---|")
    print("\n")
def check_win(player):
    if board[0]==player and board[1]==player and board[2]==player :
        return True
    if board[3]==player and board[4]==player and board[5]==player :
        return True
    if board[6]==player and board[7]==player and board[8]==player :
        return True
    if board[0]==player and board[3]==player and board[6]==player :
        return True
    if board[1]==player and board[4]==player and board[7]==player :
        return True
    if board[2]==player and board[5]==player and board[8]==player :
        return True
    if board[0]==player and board[4]==player and board[8]==player :
        return True
    if board[6]==player and board[4]==player and board[2]==player :
        return True
    else:
        return False
    


# 3. The Main Game Loop
def start_game():
    current_player = "X"
    turns = 0
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("Use numbers 1-9 to pick your spot (1 is top-left, 9 is bottom-right).")

    while not game_over and turns < 9:
        display_board()
        print(f"\nPlayer {current_player}'s turn.")
        
        try:
            choice = int(input("Pick a spot (1-9): "))
            index = choice - 1
            if board[index]=="-":
                board[index]=current_player
                turns+=1
                if check_win(current_player):
                    display_board()
                    print("+++++++++++++++++++++++++++++++++++++++++")
                    print(f"you have won the match******{current_player}********")
                    print("+++++++++++++++++++++++++++++++++++++++++")
                    game_over=True
                elif current_player=="X":
                    current_player="O"
                else:
                    current_player="X"
            else:
                print("ops it already taken")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number from 1 to 9.")

    if game_over==False and turns==9 :
        display_board()
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("**************OPPS IT'S A TIE***********")
        print("+++++++++++++++++++++++++++++++++++++++++")


start_game()

