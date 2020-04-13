def digital_root(n):
    a = str(n) #Convert the input into a string to get the digits
    sum=0
    for i in range(len(a)):
        sum+=int(a[i])
    newsum=0
    while sum > 9:
        b = str(sum)
        for i in range(len(b)):
            newsum+=int(b[i])
        sum = newsum
    return sum
