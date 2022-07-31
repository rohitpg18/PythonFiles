def compound_int(p,t,r):
    c_i = ( p*(pow ((1+r/100), t))-p)
    print(c_i)
A=int(input("Enter Principal Amount:"))
B=int(input("Enter Period of Loan:"))
C=int(input("Enter Rate of Interest:"))

compound_int(A,B,C)

