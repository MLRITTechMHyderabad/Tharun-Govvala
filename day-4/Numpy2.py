import numpy as np
resources = np.array([
    [15, 40, 32],
    [20, 42, 35],
    [25, 38, 30],
    [18, 50, 40],
    [22, 37, 36],
    [28, 45, 33]
])
resource_sum=np.sum(resources,axis=0)
print("Total resources needed (tons): Oxygen:" ,resource_sum[0],", Water: ",resource_sum[1],", Food: ",resource_sum[2])
high_val=np.unravel_index(np.argmax(resources),resources.shape)
high_val1=np.max(resources)
print(high_val1)
print(high_val)
def resource_identity(value):
    if(value==0):
        return "oxygen"
    elif(value==1):
        return "water"
    else:
        return "food"
print("Highest consumption in a month:", resource_identity(high_val[1]), "(",high_val1 ,"tons in month", high_val[0]+1,")")

std_values=np.std(resources,axis=0)
round_std_values=np.round(std_values,decimals=1)
print("Standard deviation of consumption: Oxygen:", round_std_values[0],", Water: ",round_std_values[1],", Food: ",round_std_values[2])

print("Transposed matrix :\n",resources.reshape(3,6))