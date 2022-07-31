def leafyr(year):
    count=0
    leap_year_list=[]
    leap_year_nos=int(input("Enter Qty of Required next leap years:"))
    while(count<leap_year_nos):
        if (year%4==0 and year%100!=0) or year%400==0:
            leap_year_list.append(year)
            count+=1
        year+=1
    return leap_year_list
y=int(input("Enter Year:"))
print("===================================================================================================")
print(leafyr(y))
print("===================================================================================================")