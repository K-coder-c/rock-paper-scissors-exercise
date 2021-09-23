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

user_chose = input("Please Input either Rock, Paper, or Scissors:")

#print("*************") #13 stars

#use an if statment here

print("You chose: " +user_chose)

#print("You Chose: " +x)

#print("*************") #13 stars

#checks to see if user entered valid input


options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options) 

print("The computer chose: " +computer_choice)



#if input == "Rock" and "rock" : #changed or to and to see if that works

    #print("You chose: " +user_chose)

#elif input == "Paper" or "paper" :

    #print("You chose: " +user_chose) #this might be the problem..

#elif input == "Scissors" or "scissors" :

    #print("You chose: " +user_chose)

#else :
    #print("You have entered an Inaccurate Input!")

