
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