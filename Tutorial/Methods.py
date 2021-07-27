#Methods using lists
#Setting the varible spam to a list we use the index method to pass argument in this case one of the values from the list to get what its index is.
spam = ['hello','hi','howdy','sup']
print(spam.index('hello'))

#To add new values to a list we'll be using append() and insert() method which can only be used with list values

#the append method adds a value to the end of a list
spam.append('yoo')
print(spam.index('yoo'))

#The insert method is similar to append, but it can add a value anywhere in the list
spam.insert(1,'hola')
print(spam.index('hola'))
print(spam.index('hi'))

#Lists have remove method which does exactly what it sounds like, if there are multiple of the same value in the list it will only remove the first instance of the value
spam.remove('hello')
print(spam.index('hola'))

#Strings or Number values list can be sorted with the sort() list method
#We can pass a keyword argument like 'reverse' which is a boolean value and that will reverse the order of the sort
spam = [7, 3, 18, 1, 5, 9, 13]
spam.sort()
print(spam)

#NOTE: we cant sort list that have a mix of numbers and string values in them.
spam = ['orange', 'apples', 'passionfruit', 'grape', 'banana','strawberry']
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

#The sort function doesnt technically put the list in alphabetical order it sorts it in ascii-betical order, meaning it will proritize the order of an uppercase character first and then sort by the lower case characters. to get true alphabetical sorting we can pass the keyword 'key=str.lower'which is passing the convert to lowercase string method through the sort function
spam = ['Epsilon', 'beta', 'gamma', 'alpha', 'Ro','delta']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)