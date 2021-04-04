"""This is the main script for the rock paper scissors game."""


import os 
import time 

# Constants that will be used throughout the game
ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

class Player:
    """This is the player class. It is the blueprint for the two player objects used throughout the game."""
    def __init__(self, name ):
        self.name = name
        self.pick = None
        self.win = 0


def game():
    """This function is used when running the game. 
    The players can set their names and choose how many rounds they want to play."""
    print("---WELCOME TO ROCK, PAPER, SCISSORS---\n")

    try:
        p1 = Player(input("\nYou are Player 1.\nEnter your name:\n"))
    except ValueError:
        p1 = Player("Player 1")
    try:
        p2 = Player(input("\nYou are Player 2.\nEnter your name:\n"))
    except ValueError:
        p2 = Player("Player 2")

    print("\nHow would you want to play?")
    choice = input("\nBest of:\n(1.)Three\n(2.)Five\n(3.)Sudden Death - one round\n")
    
    valid = False
    while not valid:
        if choice.lower() in ["1", "1.", "one"]:
            play(3, p1, p2)
            valid = True
        if choice.lower() in ["2", "2.", "two"]:
            play(5, p1, p2)
            valid = True
        if choice.lower() in ["3", "3.", "three"]:
            play(1, p1, p2)
            valid = True
        else:
            print("That was not a valid selection.\nPlease tyr again")
        
    print(f"\n{p1.name} won {p1.win} round(s) and {p2.name} won {p2.win} round(s)\n")

    if p1.win > p2.win:
        print(f"{p1.name} IS THE WINNER")
    elif p2.win > p1.win:
        print(f"{p2.name} IS THE WINNER")
    else:
        print("The game ended as a draw")

    print("\n\nTHANK YOU FOR PLAYING")


def play(repeat, player1, player2):
    """This function is used to run the player's turns.
    This function also determines who wins each round."""
    def turn(player1, player2):
        """This function is used for each turn."""
        time.sleep(0.75)
        os.system("cls")

        pick1 = input(f"\n\n{player1.name}, what do you pick?\n1.Rock\n2.Paper\n3.Scissors\n")
        valid = False
        while not valid:
            if pick1.lower() in ["1", "1.", "one"]:
                player1.pick = "ROCK"
                valid = True
            elif pick1.lower() in ["2", "2.", "two"]:
                player1.pick = "PAPER"
                valid = True
            elif pick1.lower() in ["3", "3.", "three"]:
                player1.pick = "SCISSORS"
                valid = True
            else:
                print("You have selected an invalid character. Please try again.")
        time.sleep(0.25)
        os.system("cls")

        pick2 = input(f"\n\n{player2.name}, what do you pick?\n1.Rock\n2.Paper\n3.Scissors\n")
        valid = False
        while not valid:
            if pick2.lower() in ["1", "1.", "one"]:
                player2.pick = "ROCK"
                valid = True
            elif pick2.lower() in ["2", "2.", "two"]:
                player2.pick = "PAPER"
                valid = True
            elif pick2.lower() in ["3", "3.", "three"]:
                player2.pick = "SCISSORS"
                valid = True
            else:
                print("You have selected an invalid character. Please try again.")
        time.sleep(0.25)
        os.system("cls")

        if player1.pick == ROCK and player2.pick == ROCK:
            print("\nDRAW")
        elif player1.pick == ROCK and player2.pick == PAPER:
            player2.win += 1
            print(f"\n{player2.name} WINS\n")
        elif player1.pick == ROCK and player2.pick == SCISSORS:
            player1.win += 1
            print(f"\n{player1.name} WINS\n")
        elif player1.pick == PAPER and player2.pick == ROCK:
            player1.win += 1
            print(f"\n{player1.name} WINS\n")
        elif player1.pick == PAPER and player2.pick == PAPER:
            print("\nDRAW")
        elif player1.pick == PAPER and player2.pick == SCISSORS:
            player2.win += 1
            print(f"\n{player2.name} WINS\n")
        elif player1.pick == SCISSORS and player2.pick == ROCK:
            player2.win += 1
            print(f"\n{player2.name} WINS\n")
        elif player1.pick == SCISSORS and player2.pick == PAPER:
            player1.win += 1
            print(f"\n{player1.name} WINS\n")
        elif player1.pick == SCISSORS and player2.pick == SCISSORS:
            print("\nDRAW\n")
        else:
            pass
    
    for rep in range(repeat):
        turn(player1, player2)
        if rep == repeat:
            break

if __name__ == "__main__":
    game()
    print("\nPress any key to exit.")
    input()
