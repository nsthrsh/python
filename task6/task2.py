from functions import *
import random
arr=list(random.randint(0,10) for x in range(10))
print(arr)

sort(arr)

key1=int(input("Введіть значення-ключ для функції elementValue: "))
elementValue(arr,key1)

arr1=input("Введіть послідовність для функції elementCos: ").split()
key2=input("Введіть послідовність-ключ для функції elementCos: ").split()
if(elementCos(arr1,key2)==True):
    print("Послідовність",key2," існує!")
    print('\n')
else:
    print("Послідовність",key2," не існує!")
    print('\n')

fiveMin(arr)
fiveMax(arr)
summ(arr)
returned(arr)
