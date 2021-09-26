#Advanced  string syntax

#To be able to use both double and single quotes in python we must use an escape characters starts with a "\" + the mark you want to use for example:
#list of escape character types:
#\' - Single quote
#\" - Dobule quote
#\t - Tab
#\n - Newline(line break)
#\\ - Backslash

#print('That is Jim's ball') This wont work as python choose the middle quote to ended the ability for the print function to see there other characters. Alternatively we can use double quotes

#Now that solves our single quote issue now what happens if we want to use double quotes to actually quote someone
print("That is Jim's ball")
print("And I said \"who cares about the weather\"")

# Raw String: incase there is text that includes many backslahes that dont want to be seen as the beginning of an escape character we use raw string represented at the beginning of a string text quotation as just an r followed by the quotations example:
print(r'Who\'s watch is that?')
#as opposed to the regular escape character method of doing this 
print('Who\'s watch is that?')

#Multiline Strings with triple quotes: begins and ends with either 3 single quote characters(''') or 3 double quote characters (""") python reads this all as one line of code.  good for long paragraphs example:
print("""We've been trying to reach you concerning your vehicle's extended warranty. You should've received a notice in the mail about your car's extended warranty eligibility """)
#side note strings work very similarly like lists so functions can work with them for intance checking indexs finding if a character exists in a string variable etc etc.