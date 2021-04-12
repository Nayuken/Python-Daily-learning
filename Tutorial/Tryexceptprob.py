print('how many dogs do you have?')
numDog = input()
try:
  if int(numDog) >= 5:
      print('That is a lot of dogs')
  elif int(numDog) < 0:
      print('it doesnt make sense to have negative pets friend')
  else:
      print('That is not a lot of dogs')
except ValueError:
      print('Error: you did not print an int number')

  #try adding a try and except in the case that a string varible is taken as input