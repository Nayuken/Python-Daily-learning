# mutable and Immutable data types; while string variable and list functions are similar they are different in the fact that one can actively have it's parts(index) changed(mutable). Where the other cannot(immutable) example provided below:
name = 'Real McName'
print(name[5])

#using a string if we try and change the value at index 5 we will get an error
#name[4] = 'x'

#proper way to modifiy a string is to use slices
newName = name[0:4] + ' Actual' 
print(newName)

#references and how to understand them in terms of mutable and immutable data types

#With strings:
spam = 100
print('Spam is equal to: '+str(spam))
cheese = spam
print('Cheese is equal to spam, so cheese equals: ' +str(cheese))
spam = 200
print('Spam is equal to: '+str(spam)+ ' which means cheese is equal to: '+str(cheese))
#When cheese was first assigned the value of spam it took over the value itself and stored it to cheese variable. Just because we updated spam later doesnt change cheese as cheese is now treated as this: cheese=100 we would need to add a line of code to update cheese to match spam

#With Lists, when assigning a list to a variable python assigns a reference to the list, wwhen we set cheese = spam it makes a copy of the reference for itself but they're referncing the same list so any changes made on either will effect both. mutable values store references so that they can replace the values inside the reference.
spam = [0, 1, 2, 3, 4, 5]
print('Spam is equal to the list: ' +str(spam))
cheese = spam
print('Cheese is equal to the list: ' +str(cheese))
cheese[0] = 6
print('Spam is equal to: ' +str(spam[0])+ ' at index 0 which means cheese is equal to: '+str(cheese[0]))

#Creating a completely seperate list from an existing list
import copy
#Makes copy of a list function, but instead of just having reference to the same list it makes its own list just copying the values of the list that is passed through it.
spam = ['A','B','C','D']
print('Spam is equal to the list: ' +str(spam))
cheese = copy.deepcopy(spam)
print('Cheese is equal to the list: ' +str(cheese))
cheese[0] = 6
print('Spam is equal to: ' +str(spam)+ ' which means cheese is equal to: '+str(cheese))

#Line contiuation: list can span multiple lines of code and still run just fine as the list function knows even on multiple line anything contained between the brakets is apart of the list, good for when list are alot of values
spam = [
  'apples',
  'oranges',
  'grapes'
]

print(spam)