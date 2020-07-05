import random

def func(x):
    x.sort()
    for i in range(0,5):
        print(x[i],end=" ")

arr=[random.randint(0,100) for x in range(10)]
print(arr)
func(arr)
