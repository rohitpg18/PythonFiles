""" 
      * 
     * * 
    *   *
   *     *
  *       *
 * * * * * *
input = 6
"""

for i in range(6) :
    for j in range(6-i) :
        print(' ',end='')
    for j in range(i+1) :
        if (i==2 and j==1) or (i==3 and j==1) or (i==3 and j==2) or (i==4 and j==1) or (i==4 and j==2) or (i==4 and j==3) :
            print('  ', end='')
        else :
            print(' *', end='')
    print()