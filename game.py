# game.py
import random


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
#Let's play!
my_input = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("You chose: '"+ my_input+"'")

my_choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(my_choices)
print("The computer chose: '"+computer_choice+"'")

separators()

#Display game result
if my_input == computer_choice:
    print("It's a tie!")
elif my_input=="rock" and computer_choice=="paper":
    print("Good Job! You won!")
elif my_input=="rock" and computer_choice=="scissors":
    print("Good Job! You won!")
elif my_input=="paper" and computer_choice=="rock":
    print("Oh, the computer won. It's ok.")
elif my_input=="paper" and computer_choice=="scissors":
    print("Oh, the computer won. It's okay")
elif my_input=="scissors" and computer_choice=="rock":
    print("Oh, the computer won. It's okay")
elif my_input=="scissors" and computer_choice=="paper":
    print("Good Job! You won!")
else:
    print("blahhhhh")

#Thank you message
separators()
thankyou_message()

