# factorial using function
def fact(x):

    if x==1:
        return 1
    else:
        return (x*fact(x-1))
num=int(input("Enter a number to find factorial: "))
b=fact(num)
print("factorial of given number is" , b )