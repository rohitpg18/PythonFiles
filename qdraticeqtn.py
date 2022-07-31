# Python Program to Solve Quadratic Equation
# ax**2+bx+c=0

import cmath

print('''Quadratic equation is: ax**2+bx+c=0
where''')


a=int(input("a is "))
b=int(input("b is "))
c=int(input("c is "))

z= (b**2 - 4*a*c)

x1= (-b+ cmath.sqrt(z))/2*a
x2= (-b- cmath.sqrt(z))/2*a

y1=(-b + (b**2 - 4*a*c)**0.5 )/2*a
y2=(-b - (b**2 - 4*a*c)**0.5 )/2*a

print("Solution of given quadratic equation in complex format: {} , {}".format(x1,x2))
print("Solution of given quadratic equation in normal format: {} , {}".format(y1,y2))