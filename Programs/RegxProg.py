#!  python3
import re,pyperclip

#TODO: Create a regex object for phone numbers
re.compile(r''' 
           # Examples: 404-552-5612, 555-0000, (770)-525-0713, 770 424 9888 555-0000 ext 12345
             ((\d\d\d) | (\(\d\d\d)))? # Area code (optional)
             (\s|-) # First Seperator(blank space or dash)
             \d\d\d   # First 3 digits
             (\s|-) # Second Seperator
             \d\d\d\d # Last 4 digits
             ((ext(\.)?\s) |x)      $ extension word-portion (optional)
             (\d{2,5})    $ extension number-portion (optional)
           '''
           ,re.VERBOSE)
#TODO: Create regex object for phone numbers

#TODO: Get the text off the clipboard

#TODO: Extract the email/phone from this text

#TODO: Copy the extracted email/phone to the clipboard

