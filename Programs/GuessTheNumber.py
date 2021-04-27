#This program is a guessing game example
import random

#Ask the user to enter their name
print("Hello, what is your name?")
name=input()

#Take the name of the user entered above and use it in our next question
print("Hello " +name+ " would you like to play a game? Y/N")
answer=input()

#ends the program after choosing No option 
if answer == ('N') or answer == ('n'):
    print("Okay maybe next time!")

#starts the game after choosing yes option
elif answer == ('Y') or answer == ('y'):

  #Sets gNum = to a number randomly generated from any number 1-20
  gNum = random.randint(1, 20) 
   #Generates a the loop range ending at 6
  for gtake in range(1,7):

    #sets the guess number input to integer so nothing other than an int will be accepted
    print("I'm thinking of a number 1-20")
    guess = int(input())

    #sets limit on how many guesses can be taken before the for loop reaches its end and it stops the program.
    if gtake == 6:
      print("Sorry you only had " +str(gtake)+ " chances to guess, The number I was think of was " +str(gNum)+ ", better luck next time!")
      break

    #Gives feedback based on if the guess is higher than, lower than, or equal to the randomly generated number
    if guess < gNum:
      print('Your guess is too low.')
    elif guess > gNum:
      print('Your guess is too high')
    elif guess == gNum:
      print("That's correct wow you're really good at this " +str(gNum)+ " was my number.")
      break