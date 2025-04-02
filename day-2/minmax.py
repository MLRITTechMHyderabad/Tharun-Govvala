li=[1,2,3,4,7,3,45,7,6,45,9]
min=li[0]
max=li[0]
for i in range(0,len(li)):
    if(max<li[i]):
        max=li[i]
    elif(min>li[i]):
        min=li[i]

print(" min : ", min)
print(" max : ", max)
