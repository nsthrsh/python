import random

n = int(input('n='))
arr1 =[random.randint(0,1) for x in range(2*n)]
print("our random list: ", arr1)
part = int(len(arr1)/2)
part1=arr1[:part]
part2=arr1[part:]
arr = []
for j in range(len(part1)):
    arr.append(part1[j])
    arr.append(part2[j])
print("our new list: ", arr)
