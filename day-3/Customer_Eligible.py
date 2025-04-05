customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

Eligible_customers=list(filter(lambda x :  x["age"] <=40,customers))


def Discount(age):
    if(age>=18 and age<=25):
        return 0.90
    elif(age>=26 and age<=40):
        return 0.95

customers=list(map(lambda x : x['total_purchase']*Discount(x['age']),Eligible_customers ))
c=0
for i in Eligible_customers:
    i['total_purchase']=customers[c]
    c+=1
print(Eligible_customers)