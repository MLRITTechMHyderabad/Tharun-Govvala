employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

def Sal_inc(rating):
    if(rating==4 or rating==5):
        return 1.1
    elif(rating==3):
        return 1.05
    else:
        return 0.97
    
updated_employyes = list(map(lambda x : int(x['salary'] *Sal_inc(x['rating'])),employees))
c=0
for i in employees:
    i['salary']=updated_employyes[c]
    c+=1
print(employees)