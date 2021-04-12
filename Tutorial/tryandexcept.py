def div42by(divideBy):
  try:
    return 42/ divideBy
  except ZeroDivisionError:
    print('you tried to divide by 0, it will print none in place of the answer instead')
#it is import to note the indentation if we dont the program wont run.
print(div42by(4))
print(div42by(2))
print(div42by(0))
print('congrats we ran a try except program!')