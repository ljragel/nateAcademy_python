
numbers=[1,2,3,4,5,6,7,8,9,9,10,11,12,14,20,15,30,60,70]

max=0
for i in range(numbers.__len__()):
    if numbers[i]>max:
        max=numbers[i]

print(max)