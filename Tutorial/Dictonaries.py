
import pprint
#Dictonaries: we can set keys to 
myCat = {'size':'fat', 'color':'gray', 'disposition': 'Loud'}
print('My cat is: ' +myCat['size'])

spam = {12345: 'locker combianation', 6789: 'zip code'}
print('My '+spam[12345]+ ' is ' +str(12345))

#dictonaries have no order so when comparing two if they have the same values it will return as true as shown below
eggs = {"name": "charlie", "Age": 10, "species": 'dog'}
ham = {"species": 'dog', "name": "charlie", "Age": 10,}
print("The values of Egg and Ham are ordered different, but have the same keys")
print(eggs == ham)

#We can check if a key exists in a value with in or not in operators for example
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

#Adding a new entry to a dictonary
picnicItem= {'apples:':5,'cups':2}
print("I am bringing "+str(picnicItem.get('napkins', 0))+' to the picnic')
#Using the example above if we try and call the temporary entry napkins it will throw an error so to get around this  we can use .setdefault method to add a new entry if it doesnt already exist, if it does it wont change he entry value
picnicItem.setdefault('napkins', 3)
print("I am bringing " +str(picnicItem['napkins'])+ " napkins to the picnic")


#test, count the number of occurences of a letter in a given a string

message = 'Hi my name is Nyenty'
print(message)
count ={} #for this example we will use S for our letter to be counted

for character in message.upper(): #using .upper()allows us to merge all the letter types (upper case and lowercase) to be counted as 1 value in this case uppercase
  count.setdefault(character, 0) #This starts our count for whatever letter is being counted to 0
  count[character] = count[character]+1
pprint.pprint(count)

#we can also make the out put look better by using the pprint module start first by importing it in to this file. using repl(the place I do my work, importing and applying pprint module to the code alphabetized the letters. )