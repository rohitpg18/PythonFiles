def check_if_ele_occurs(ele,list):

    count_element=list.count(ele)

    if count_element>0:
        print('''=================================================
        Element occurs in list
=================================================''')
    else:
        print('''=================================================
        Element does not exist
=================================================''')

list= [10, 15, 20, 7, 46, 2808, 7]

ele= int(input("Enter element to find whether its present or not: \n"))

check_if_ele_occurs(ele,list)



    
    
        