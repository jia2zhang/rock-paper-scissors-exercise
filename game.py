# game.py
import random

#Define the determine_winner function used in game_test.py
def determine_winner(u, c):
    winner = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = winner[u][c]
    return winning_choice

#Only if this script is executed from the command-line, so this line of code takes the script out of the global scope
if __name__ == "__main__":

    ##Define functions
    print("Rock, Paper, Scissors, Shoot!")

    def separators():
        print("-------------------")

    def welcome_message():
        print("Welcome to Jessica's Rock-Paper-Scissors game...")

    def thankyou_message():
        print("Thanks for playing. Please play again!")

    ##Game Output
    separators()
    welcome_message()
    separators()
    #Let's play and also validate inputs
    my_input = input("Please choose either 'rock', 'paper', or 'scissors': ")
    my_choices = ['rock', 'paper', 'scissors']

    if my_input not in my_choices:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

    print("You chose: '"+ my_input+"'")
    computer_choice = random.choice(my_choices)
    print("The computer chose: '"+computer_choice+"'")

    separators()

    #Display game result
    # if my_input == computer_choice:
    #     print("It's a tie!")
    # elif my_input=="rock" and computer_choice=="paper":
    #     print("Oh, the computer won. It's okay")
    # elif my_input=="rock" and computer_choice=="scissors":
    #     print("Good Job! You won!")
    # elif my_input=="paper" and computer_choice=="rock":
    #     print("Good Job! You won!")
    # elif my_input=="paper" and computer_choice=="scissors":
    #     print("Oh, the computer won. It's okay")
    # elif my_input=="scissors" and computer_choice=="rock":
    #     print("Oh, the computer won. It's okay")
    # elif my_input=="scissors" and computer_choice=="paper":
    #     print("Good Job! You won!")
    # else:
    #     print("blahhhhh")

    #Alternative 2 to code game result
    winner = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winner[my_input][computer_choice]

    if winning_choice:
        if winning_choice == my_input:
            print("Good Job! You won!")
        if winning_choice == computer_choice:
            print("Oh, the computer won. It's okay")
    else:
        print("It's a tie!")

    #Alternative 3 to code game result

    # if my_input == computer_choice:
    #     winning_choice = None
    # else:
    #     choices = [my_input, computer_choice]
    #     choices.sort() #FYI, this is mutating

    #     if choices == ["paper","rock"]:
    #         winning_choice = "paper"
    #     elif choices == ["paper","scissors"]:
    #         winning_choice = "scissors"
    #     elif choices == ["rock", "scissors"]:
    #         winning_choice = "rock"
    # if winning_choice:
    #     if winning_choice == my_input:
    #         print("Good Job! You Won!")
    #     elif winning_choice == computer_choice:
    #         print("Oh, the computer won. It's okay")
    # else:
    #     print("It's a tie!")    
        
    #Thank you message
    separators()
    thankyou_message()

