# average of 5 students marks in 5 subjects

import numpy as np

li = []
avg = []
for i in range(0, 5):  # 5 students
    li1 = []
    sum = 0
    for j in range(0, 5):  # 5 subject marks
        a = int(input(f"Student{i + 1}, Mark in sub{j + 1}:"))
        li1.append(a)
        sum += a
    li.append(li1)
    avg.append(sum / 5)
print("List representation:\n", li)
arr = np.array(li)
print("Array representation: \n", arr)

'''
#finding avg
avg=[]

for i in range(0,5):
    sum=0
    for j in range(0,5):
        sum+=arr[i][j]
    avg.append(sum/5)'''

print("List of Average: ", avg)
count = 1
for i in avg:
    print(f"Average of student {count}= {i}")
    count += 1

