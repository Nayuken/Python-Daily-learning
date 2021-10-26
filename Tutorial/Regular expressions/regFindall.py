import re

#Patter finding the ? indicates you can either find the extra case 0 or 1 times in the text
batRegex = re.compile(r'bat(wo)?man')
mo=batRegex.search('The adventure of batman and batwoman')
mo.group()
print(mo.group())

#excluding certain data from appearing in a regex search. For this example we are going to show excluding certain numbers from a cell phone number search
phoneRegex = re.compile(r' \d\d\d-\d\d\d-\d\d\d\d')
mo=phoneRegex.search('My phone number is 770-714-2088')
mo.group()
print(mo.group())

#this example shows an optional case where if the search tries to find the first 3 digits it can either show up or not so it will be true even if it doesnt have the first 3 case
phoneRegex = re.compile(r' (\d\d\d-)?\d\d\d-\d\d\d\d')
mo=phoneRegex.search('My phone number is 714-2088')
mo.group()
print(mo.group())

#this example will be for matching an expression 0 or more times
phoneRegex = re.compile(r' \d\d\d-\d\d\d-\d\d\d\d')
mo=phoneRegex.search('My phone number is 770-714-2088')
mo.group()
print(mo.group())

#this will show how to use regex to find all examples of a search present in a variable for this example it will be a string variable.
ksuDirect = '''Admissions
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

phoneRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneRegex.findall(ksuDirect)
count =len(mo)
print('There are '+str(count)+ ' phone numbers in the text result: '+str(mo) )

#using different meta character expressions we can format the regex operation to in this case find emails based on the structure of word@word.word (typical email format)
phoneRegex = re.compile(r'\w+\@\w+\.\w+')
mo=phoneRegex.findall(ksuDirect)
count =len(mo)
print('There are '+str(count)+ ' email addresses in the text result: '+str(mo) )