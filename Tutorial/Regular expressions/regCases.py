import re

# the ^ metacharacter is for begins with, if an object doesnt match the case of the ^metacharacter
beginswithHelloreg = re.compile (r'^Hello')
tst = beginswithHelloreg.search('Hello is from the otherside')
#if this search doesnt match the object beginswithHelloreg it will return as none, if it does it will return as true
if tst == None:
  print("False, this test doesn't start with the value")
else:
  print("True, this test starts with the correct value")

#in this example we will be looking in to the $ metacharacter for ends with in which the regex has to match the ending characters in order to return true metacharacter$
endswithGoodBye = re.compile(r'goodbye$')
tst = endswithGoodBye.search("That\'s all folks, goodbye")
if tst == None:
  print("False, this test doesn't start with the value")
else:
  print("True, this test starts with the correct value")

# In the case where you want to check if an object starts with and ends with a character you would set up thje compile expressions as follows: ^metacharacter$

#matching a specific character case can be done by adding a '. metacharacer' example below

atRegex = re.compile(r'.at')
#This will only find the character at and any 1 character before it so if we want to include more letters before it to include for instances the full word "flat" we would add preceded by {1,2} letters of any which will allow it to see up to 2 letters in a given search
mo = atRegex.findall('The cat in the hat got a flat on the tar mat in atlanta')
print('\nFor this example it will print a list of all the characters that have a \'at\' some where in them:  '+str(mo))

#Now with this we see that the 'n' in the word 'in' was add for the at in atlanta this is because it again counted the whitespace but also 'n' since it fit the expression of 1 or 2.
atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat got a flat on the tar mat in atlanta')
print('\nFor this example it will print a list of all the characters that have a \'at\' some where in them:  '+str(mo))

#How to get around this space .* regex(.metacharacter = any character at all, *metacharacter = zero or more)

#finding name using regular expressions using the pattern recognition with the .* metacharacter we cab setup our regex to find a specific phrase and parse the information we're looking for out of that common phrase by using .*meta character examples below

nameEntry = ('First Name: Nyenty Last Name: Ayuk')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall(nameEntry)
print(mo)

#personal test find the phone number and email from this string.
ksuDirect = '''
Admissions
Phone: 770-423-6300
Email: ksuadmit@kennesaw.edu

Employment
Phone: 470-578-6030
Email: hr@kennesaw.edu

Financial Aid
Phone: 770-423-6074
Email: finaid@kennesaw.edu

IT Service Desk
Faculty/Staff:
Phone: 470-578-6999
Email: service@kennesaw.edu

Students:
Phone: 470-578-3555
Email: studenthelpdesk@kennesaw.edu

Strategic Communications and Marketing
Phone: 470-578-6203
Email: stratcomm@kennesaw.edu

Student Involvement
Phone: 470-578-6280
Email: studentlife@kennesaw.edu

Registrar
Phone: 770-423-6200
Email: registrar@kennesaw.edu '''

emailREG = re.compile(r'Email: (.*)')
mo = emailREG.findall(ksuDirect)
print('\nThe emails found in this document are as followed:\n ' +str(mo))

PhoneREG = re.compile(r'Phone: (.*)')
mo = PhoneREG.findall(ksuDirect)
print('\nThe phone numbers found in this doucment are as followed:\n '+str(mo))


#.* by default is in greedy mood so it will find any and all matching case to make it non-greedy we just need to add .*?

serve = '<We serve steak> and mashed potatoes>'
nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print('\nExample of non-greedy mood:\n '+str(mo))

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print('\nExample of greedy mood:\n '+str(mo))

#Casematching the easy way with ,re.I in our re.compile parameters:

vow = 'And then the day came, when the risk to remain tight in a bud was more painful than the risk it took to blossom'

#This regex will find vowels in a string, specifically lowercased vowels
vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall(vow)
print('\nThis is an example of just finding lowercase vowels from a string:\n' +str(mo))

#This regex will find vowels in a string, in this case it will find both the upper and lowercase version of the case provided
vowelRegex = re.compile(r'[aeiou]',re.I)
mo = vowelRegex.findall(vow)
print('\nThis is an example of finding both upper and lower case vowels from a string:\n' +str(mo))

#to include newlines when searching an expression we would use ,re.DOTALL in our re.compile parameters.

muLine = 'And then the day came, \nwhen the risk \nto remain tight \nin a bud \nwas more painful \nthan the risk \nit took \nto blossom'

#wrong way this will print out the first case that matches as it wont include any newline breaks
muRegex = re.compile('.*')
mo = muRegex.findall(muLine)
print(mo)

#Using the re.DOTALL to print the full string
muRegex = re.compile('.*',re.DOTALL)
mo = muRegex.findall(muLine)
print(mo)