def LargestNum(list):
    max=list[0]
    for i in list:
        if max<i:
            max=i
    return max

list=[2,5,10,52,22,52,552,545,1]

print(LargestNum(list))