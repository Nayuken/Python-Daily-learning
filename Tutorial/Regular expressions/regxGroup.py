import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('my number is 770-714-2088')
mo = phoneNumRegex.search('my number is 770-714-2088')
print(mo.group())

#By adding () to each sections we are making regex groups out of the phone numbers so there are 3 groups that can now pass through the .group(1,2,3) method
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('my number is 770-714-2088')
print(mo.group(3))

#pipe character "|": used to match one of several patters as a part of regular expressions
batRegex = re.compile(r'Bat(man|mobile|copter|bat|cave)')
mo = batRegex.search('robin ended up in a field of at the Batcave after arresting joker')
print(mo.group())