li=[[1,2,3],[4,5,6],[7,8,9]]
li1=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(li)):
    for j in range(0,len(li[i])):
        li1[j][i]=li[i][j]
        
for i in range (0,len(li1)):
    print(li1[i])
    

