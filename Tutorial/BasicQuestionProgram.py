#Basic program to practice using if statement and input function.

print("This is a simple question/ reply program")
print()
print(" Did you find the first part of this tutorial easy? ANSWER Y/N")
Qanswer = input()

#An else could be used instead of two ifs to make it quicker to process the answer instead.
if Qanswer == ('y') or Qanswer == ("Y"):
    print()
    print("Well thats good for you bud Keep up the studying!")

if Qanswer == ('n') or Qanswer == ("N"):
    print()
    print(
        "Maybe we should go back and review somethings before moving forward.")
