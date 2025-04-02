import random
n=int(input("enter no of ways"))
li=[]


for i in range(0,n):
    list=[]
    for j in range(0,4):
        list.append(random.randint(1,6))
    li.append(list)

print(li)
def find_prob(number,nw):
    if(number<8):
        return float((number-1)/nw)*100
    else:
        return float((13-number)/nw)*100
    

first_win=0
second_win=0
for i in range (0,len(li)):
    first=li[i][0]+li[i][1]
    second=li[i][2]+li[i][3]

    firstprob = find_prob(first,36)
    secondprob = find_prob(second,36)
    print(firstprob,secondprob)
    if(firstprob<secondprob):
        first_win+=1
    elif(firstprob>secondprob):
        second_win+=1


if(first_win>second_win):
    print("player 1 wins")
elif(first_win<second_win):
    print("player 2 wins")
else:
    print("its a draw")




