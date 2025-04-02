li=[1,2,3,2,3,1,4,5,2,3,4,1,5]

def frequency(li):
    di={}
    for i in range(0,len(li)):
        count=0
        bc=0
        for j in range(0,len(li)):
            if(li[i]==li[j]):
                count+=1
        for k in range (0,i):
            if(li[i]==li[k]):
                bc+=1
        if(bc==0):
            di[li[i]]=count
    print(di)
frequency(li)
