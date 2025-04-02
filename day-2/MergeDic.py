d1 = {"name":"tharun","location":"hyderabad","age":"23"}
d2 = {"name":"ricky","location":"chennai","gender":"male"}
li = []
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    d3[i]=d2[i]
for i in d1.keys():
    list=[]
    for j in d2.keys():
        if i == j:
           list.append(d1[i])
           list.append(d2[j])
           d3[i]=list
    li.append(list)

print(d3)