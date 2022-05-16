import re
#regular expression object
nameregex = re.compile(r'Agent \w+')
nameRgx = nameregex.findall('Agent bobby and Agent donald gave the documents to Agent ted')
print('These agents names needs to show up redeacted in the report' +str(nameRgx))
#sub method works similar to findall in that it searches through the printed statement to find the compile case then instead of printing the compiled items it changes them to what ever is placed in the first quotation then prints them if when printed.
nameRegx = nameregex.sub('[REDACTED]', 'Agent bobby and Agent donald gave the documents to Agent ted')
print((nameRegx))



#how to show a partial match using find all. when using re.compile method the 1st group "(\w)" is for any character(letters mostly) in the first position  .The 2nd group "(\w*)')" is for matching any character past the second group. Must match exactly as listed in the quotations
nameregex = re.compile(r'Agent (\w)\w*')
nameRgx = nameregex.findall('Agent bobby and Agent donald gave the documents to Agent ted')
print(str(nameRgx))
#how to find and replace portion of a matched case: make the string raw by adding the 'r' at the start of the string inside the quotation add the text that will be replacing the matching expression case. in this example ours is 1st group of any character"\w" and any character after it in the second group"\w*". The \1 syntax substitutes the matching portion of the original string so it wont change.
nameRegx = nameregex.sub(r'Agent \1******', 'Agent bobby and Agent donald gave the documents to Agent ted')
print((nameRegx))



#verbose regular expression string:.reverbose is used inside of the re.compile argument. it allows for the rules for reading how text appears to be ignore allowing us to change how we organize the text without effecting it's functionality. Good for readability and allows us to come back and comment on 
pRegx = re.compile(r'''
           \d\d\d  #Area code
           - #First dash
           \d\d\d #First 3 digits
           - #Second dash
           \d\d\d\d #Last 4 digits
           '''
           ,re.VERBOSE)
phonRegx = pRegx.findall('My phone number is 334-552-0801.')
print(str(phonRegx))

#To pass multiple arguments through the re.compile() we need to start by adding 1 of the fuctions ex:re.IGNORECASE, then we add a space and add an "|"(or) and add a second fuction ex: re.VERBOSE.
pRegx = re.compile(r'''
           \d\d\d  #Area code
           - #First dash
           \d\d\d #First 3 digits
           - #Second dash
           \d\d\d\d #Last 4 digits
           '''
           ,re.VERBOSE | re.IGNORECASE)
phonRegx = pRegx.findall('My phone number is 334-552-0801.')
print(str(phonRegx))