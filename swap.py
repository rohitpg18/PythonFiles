# Python Program to Swap Two Variables

a = int(input('a = '))
b = int(input('b = '))

'''other way to swap values
temp= a
a=b
b=temp'''

a , b = b , a

print("Swapped Values of a & b are {} , {}".format(a,b))