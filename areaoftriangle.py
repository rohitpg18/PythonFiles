# Python Program to Calculate the Area of a Triangle by Herons Formula

A=int(input("Length 1:"))

B=int(input("Length 2:"))

C=int(input("Length 3:"))

S=((A+B+C)/2)
# semiperimetr of triangle

area_triangle = (S * (S-A) * (S-B) * (S-C)) ** 0.5

print("Area of Triangle is:", area_triangle)