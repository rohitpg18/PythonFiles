""" 
* * * * *
*       *
* * * * *
Input = 3,5
 """

for i in range(3) :
    for j in range(5) :
        if (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3):
            print('   ', end='')
        else :
            print(' * ', end='')
    print()