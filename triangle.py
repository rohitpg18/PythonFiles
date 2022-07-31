row = int(input("Enter No. of Rows:"))
col = int(input("Enter No. of Column:"))

for row in range (row):
    for col in range (col):
        if (row==0) or row==2 or col==0 or (row==1 and col==4):
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print()