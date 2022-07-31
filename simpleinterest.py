def sivalue(p,t,r):
    print("principal amount is", p)
    print("period of loan is", t)
    print("rate of intrest is", r)

    si = (p * t * r)/100

    print("simple interest of loan is", si)

a=int(input("principal amount is:"))
b=int(input("period of loan is:"))
c=int(input("rate of intrest is:"))

sivalue(a,b,c)