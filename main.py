#just testing the repo system
#print("hello world")

#Dictonaries: we can set keys to 
myCat = {'size':'fat', 'color':'gray', 'disposition': 'Loud'}
print(myCat['size'])

spam = {12345: 'locker combianation', 6789: 'zip code'}
print('My '+spam[12345]+ ' is ' +str(12345))

#dictonaries have no order so when comparing two if they have the same values it will return as true as shown below
eggs = {"name": "charlie", "Age": 10, "species": 'dog'}
ham = {"species": 'dog', "name": "charlie", "Age": 10,}
print(eggs == ham)

#We can check if a key exists in a value with in or not in operators for exampl
print('name' in eggs)
print('height' not in eggs)

print('length' in ham)
print('Age' not in ham)
#3 Dictonary methods keys(), values(), & items()

#returns a list of the keys in this dictonary
print(list(eggs.keys()))
#returns a list of the values in this dictonary
print(list(eggs.values()))
#returns a list of two item tuples of the dictonary with both keys & values
print(list(eggs.items()))
#They all return as list like datatypes

#We can use for loops to print out the specific items in a dictonary as well
for k in eggs.keys():
  print(k)

for k in eggs.values():
  print(k)

for k in eggs.items():
  print(k)

#We can also store the information of a dictonary as 2 values and print them together using 2 assigning variables. prints them out as tuples(immutable)
for k, v in eggs.items():
  print(k, v)

#We can check for values in dictonary by listing the value in the dictonary:
print('dog' in eggs.values())

#To check whether a key exists in a dictonary we can use the get method on a list for example:

print(eggs.get('Age', 0))