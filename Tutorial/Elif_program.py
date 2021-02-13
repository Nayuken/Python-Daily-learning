#Basic function to help understand how Elif statements work
Name = 'bob'
age = 3000

#first conditional statement to see if Name is equal to alice if it is, then return a message
if Name == 'alice':
    print('Hi alice')
#second conditional statement, will be checked if the first condition is not met. In the case this is also not met and is followed up by another elif then it will keep checking until a condition is met.
elif age < 12:
    print("You're not alice")
elif age > 2000:
    print("bob's your uncle!")
elif age > 100:
    print("you're not alice")
