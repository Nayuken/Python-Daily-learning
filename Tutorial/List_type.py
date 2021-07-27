
#learning to use list data type.

#index = single Value
#Slice = list of values

sList= ['soccer','cars','gaming','video editing']
print(sList)

#When you want to call an item from a list you will choose its index number shown below
print(sList[0])
print(sList[1])
print(sList[2])
print(sList[3])
print('\n')

#same can be used to referencing a list within a list as shown below(list of list)
ssList=[['arsenal','genesis'],['anime','music']]
#this will print out ['arsenal','genesis']
print(ssList[0])
#this will print out ['anime','music']
print(ssList[1])
print('\n')

#We can also call and item within a list within a list simply by providing a second index number after the first. first index picks the list in the list within a list and the second selects the index within that list.

#this will print out arsenal
print(ssList[0][0])
#this will print out anime
print(ssList[1][0])
print('\n')

#An example of using string concatenation with list
print('This is an example of using a list, I like to watch ' +ssList[0][0]+ ' play on the weekends\n')

#Slice allows us to call up to, but not including the number of indexes in a list as shown below if we do [0:3] it will print indexes 0-2.
print(sList[0:3])
print('\n')

#just like assigning other variable list indexs can be changed as with example below:
sssList=[10,20,30]
print(sssList)

#this will replace the index 1(20) with the string 'hi'
sssList[1]= 'hi'
print(sssList)

#The same applies for Slices This will replace the indexes 1('hi') and 2('30') with 'hello' and 'wow'
sssList[1:3]= ['hello','wow']
print(sssList)
print('\n')

#slices can also use [:2] that will go from the start all the way up to the 2nd indexed value or [1:] which will start from the 2nd index and list all the rest of the index list
print(sssList[:2])
print(sssList[1:])
print('\n')

#We can also delete an index using a del statement, we will be deleting the only none string member of this list this will move all the indexes in front of it down 1 number.
del sssList[0]
print(sssList)
print('\n')

#we can also pass the lenth function (len) through a list to get the number of items in a list
countL=len(sssList)
print(countL)
print('\n')

#We can also do list concatenation(+ adds them together)/(* can multiply the index/ list)
trueList=(sList+ssList+sssList)
print("This is a combination of all 3 listes used for this example document: ")
print(trueList)
print('\n')

#We can also use the list function to break down string values in to a list shown in the example below:
functL=list('hello')
print(functL)
print('\n')

#using in or out to figure out if the value is in a list for example:
print('wow' in sssList)
print('winner' in sssList)
#using not in to figure out if the value is not in the list for example:
print('winner' not in sssList)
print('wow' not in sssList)


#List with functions

#ex 1.

#1. Using just the range function we will only see the range of the numbers being counted up to 4
ex1 = range(4)
print(ex1)

#2. Using the list function and passing the range function through it allows for the range to be counted up to 4, then it allows the list to list out each item in that range visually.
ex1 = list(range(4))
print(ex1)

#3. Adding the extra number in the range function makes it so that when the range function is being run its incrementing it's count by 2 instead of 1. The list function operates the same as it is just listing out the range values.
ex1 = list(range(0, 100, 2))
print (ex1)

#ex 2. Good example of using range function in a for loop to get both the index and the item out of a list.

#1. Using a for loop we iterate over the values in a lists, we can use the range function to get the list like value of the index as well as the item associated with that index as shown below
supplies = ['soccer', 'tennis', 'skateboarding', 'basketball']
for i in range(len(supplies)):
  print('The index ' + str(i) + ' in supplies belongs to '+ supplies[i])

#ex 3. Multiple Assignment 

#1. This how the mutiple assignments function operates taking a variable and assigning it to its correspond place in the index 
colors = ['orange', 'red', 'white', 'purple', 'green', 'black']
orange = colors[0]
red = colors[1]
white = colors[2]
purple = colors[3]
green = colors[4]
black = colors[5]
print(orange , red , white, purple , green, black)

#2. This sets the variables that will be assignemed to the corresponding index in teh list colors
orange , red , white, pruple , green, black=colors
print(orange , red , white, pruple , green, black)

#3. Mutiple assigment also works with assigning list function values
orange, red, white = 'not orange', 'not red', ' not white'

#4. example of using multiple assignment to show the swapping of variables in 1 line of assignment code
a = 'AAA'
b = 'BBB'
print('before: a = '+ a + ' and b = ' + b)
a, b, = b, a
print('after: a = ' + a +  ' and b = ' + b)

#5. augmented operators example(can us: +=,-=,*=, %=, /=)
#5a .typical way of increase the value of an already assigned variable
spam = 42
spam = 42 +1
print('Printed result of typical method: '+str(spam))
#5b. Augmented assignment method
spam += 1
print('Printed result of augmented assignment method: '+str(spam))