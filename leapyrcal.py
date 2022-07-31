#user friendly leap year calculator
while(True):

    def leafyr(n):
        count=0
        leapyrlist=[]
        NextLeapYears=int(input("Enter required leap years:"))

        while(count<NextLeapYears):
            if (n%4==0 and n%100!=0) or n%400==0:
                leapyrlist.append(n)
                count+=1
            n+=1
        return leapyrlist


    y=int(input("Enter Year:\n"))
    list= leafyr(y)

    print('''1. I want list of leap year
2. I want nth leap year''')
    choice=int(input("Enter choice 1 or 2:\n"))



    if choice==2:
        nthleapyr= int(input("Enter nth Number:"))-1
        print(list[nthleapyr])
    else:
        print(list)
    a=input("type Q if you want to quit:")
    if a=='Q' or 'q':
        break
    else:
        continue


