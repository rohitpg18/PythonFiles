from functools import reduce

fact= int(input("Enter value to find Factorial: \n"))

output= reduce(lambda a,b: a*b   , range (1, fact+1))
print(output)