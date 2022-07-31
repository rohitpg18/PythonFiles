def temp1(cel):
    far=(cel*1.8)+32
    print("Temperature in farenheit is", far)



def temp2(far):
    cel=0.55*(far-32)
    print("Temperature in Celsius is", cel)


a=input("Please choose option \n A : Celsius to Farenheit \n B : Farenheit to Celsius \n ---->")


if a=="A":
    b=(int(input("Enter Temperature value in Celsius:")))
    temp1(b)
else:
    c=(int(input("Enter Temperature value in Farenheit:")))
    temp2(c)
