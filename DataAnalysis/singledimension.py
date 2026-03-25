import numpy as np
totalmarks=[]
n = int(input("enter the number of students"))
for a in range(n):
    totalmark=int(input("enter the total marks"))
    totalmarks.append(totalmark)
print(totalmarks)
output = np.array(totalmarks)
print(output+1)



