#!  python3
import re, pyperclip

#TODO: Create a regex object for phone numbers
phoneRegex = re.compile(r''' 
# Examples: 404-552-5612, 555-0000, (770)-525-0713, 770 424 9888 555-0000 ext 12345
             ((\d\d\d) | (\(\d\d\d))? # Area code (optional)
             (\s|-) # First Seperator(blank space or dash)
             \d\d\d   # First 3 digits
             (\s|-) # Second Seperator
             \d\d\d\d # Last 4 digits
             ((ext(\.)?\s) |x)      #extension word-portion (optional)
             (\d{2,5})    # extension number-portion (optional)
           '''
           ,re.VERBOSE)

#TODO: Create regex object for Emails 
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+ # name part: we have to make our own character class highlighted by the square brakets ("[]") in this we will be doing alphabetic letters that are lowercase or uppercase as well as numbers and symbols just commonly used characters to use in the name section of the email address. The "+" symbol outside the square brakets means to search for 1 or more of the example that match the criteria of the class
                        
@ # @ symbol: just the "@" symbol straight to the point
                        
[a-zA-Z0-9_.+]+ # domain name part: We just copy and paste from the "name part" as the basis for a domain name fits all the criteria of class             
                       ''', re.VERBOSE)

#TODO: Get the text off the clipboard
# will return the string of the text that is currently been copied to the clipboard
text = pyperclip.paste() 



#TODO: Extract the email/phone from this text
# We are taking the clipboard result of the "text" variable and passing it through the phoneRegex findall(which is just checking the info from the clipboard to see if it matches any of the criteria of the regex variable)
phoneRegex.findall(text )


#TODO: Copy the extracted email/phone to the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)