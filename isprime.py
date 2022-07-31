n=29

flag = False

if n>1:
    for i in range(2,n):
        if (n % i) == 0:
            flag= True


if flag:
    print(n,"is not a prime number")
else:
    print(n,"is prime number")


