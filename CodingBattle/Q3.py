""" 
* * * * * *
*       *
*     *
*   *
* *
*
Input = 6
"""

for i in range(6) :
    for j in range(6-i) :
        if (i==1 and j==1) or (i==1 and j==2) or (i==1 and j==3) or (i==2 and j==1) or (i==2 and j==2) or (i==3 and j==1):
            print('  ', end='')
        else :
            print(' *', end='')
    print()