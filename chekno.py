# Python Program to Check if a Number is Positive, Negative or 0
while(True):
        
    a = int(input("Enter a Number:\n"))

    if a>0:
        print("Given Number is Positive")

    elif a<0:
        print("Given Number is Negative")

    else:
        print("Given Number is Zero")

    C= input("Enter Q to Exit:")
    
    if C== 'Q' or C == 'q':
        break
    else:
        continue