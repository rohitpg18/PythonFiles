# Python Program to Check if a Number is Odd or Even

x=int(input("Enter a year:"))

if (x % 4 == 0 and x % 100 !=0) or x % 400 == 0:
    print("Given year is leap year")
else:
    print("Given year not a leap year")
