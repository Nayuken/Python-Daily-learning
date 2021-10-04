##small programming that will validate regular US/Canada phone number expression
def isPhoneNumber(text):
  if len(text) != 12:
    return False #not phone number size

  for i in range (0,3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False

  for i in range (4,7):
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False

  for i in range (8,12):
    if not text[i].isdecimal():
      return False
  return True

pNum = input("Please enter your phone #: ")
pValidate = print(isPhoneNumber(pNum))
if isPhoneNumber(pNum) == True:
  print("Oh your phone number is: "+pNum)
if isPhoneNumber(pNum) == False:
  print("Please enter the correct format ***-***-****")
quit()




