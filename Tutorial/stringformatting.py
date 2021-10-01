spam = "We're on the lowers"
print(spam.lower())

spam1 = "this is purely upper "
print(spam1.upper())

#Using upper and lower function are good for when a comparison is made using case senseitive if states example:
answer= input()


  #in this first example if the user enters any uppercase characters then the if statement will return as false but if we do it like this:



  #Then before it checks for the input it will lower case all strings values checked in the input statement

if answer.lower() == 'yes':
  print('Play again')

  #isalpha() - letters only
  #isalnum() - letters and number only
  #isdecimal() - numbers only
  #isspace() - white space only
  #istitle() - title case only

  #startwith() & ends with method return true if a string vlaue that they're called on begins or ends with a string passed through the method

  #string interpellation(%s inserted in the string sentence)

  