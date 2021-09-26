# game.py

import random

#print("Rock, Paper, Scissors, Shoot!")

#First Prompt User to input "Rock, Paper, or Scissors"

#print("*************") #13 stars

print("Welcome 'Player One' to my Rock, Paper, Scissors Game :)")

#print("*************") #13 stars

#Next Compare the user selection agaisnt the list of valid options

#print("Please Input either Rock, Paper, or Scissors:")

#print("*************") #13 stars

#defined variable

user_choice = input("Please Input either Rock, Paper, or Scissors:")

#print("*************") #13 stars

#use an if statment here

print("You chose: " +user_choice)

#print("You Chose: " +x)

#print("*************") #13 stars

#checks to see if user entered valid input


options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options) 

print("The computer chose: " +computer_choice)


if user_choice == computer_choice : 

    print("It was a tie!")

elif user_choice == "rock" and computer_choice == "paper" :

    print("The Computer won!")

elif user_choice == "scissors" and computer_choice == "paper" :

    print("You won!")

elif user_choice == "paper" and computer_choice == "rock" :
    print("You won")

elif user_choice == "rock" and computer_choice == "Scissors" :
    print("You won!")

elif computer_choice == "scissors" and user_choice == "paper" :
    print("The Computer Won!")

elif computer_choice == "rock" and user_choice == "scissors" :
    print("The Computer Won!")

#breakpoint()

if user_choice != "rock" or "paper" or "scissors" : #it works :))))
    print("ERROR INCORRECT INPUT/OUTPUT")

print("Thanks, Please Play Again")