def addition(number):
    s=0
    for i in range(len(number)):
        number[i]=int(number[i])
        s=number[i]+s
    return s
   
number=[8,2,3,0,7]
add=addition(number)
print("The total sum is",add)
