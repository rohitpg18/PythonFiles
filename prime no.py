def prime(n):
    if n<2:
        return False
    for i in range (2, n):
        if n%i==0:
            return False
    return True
y= list (filter( prime, range(0,200)))
print(y)