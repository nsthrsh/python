def sort(arr):
    arr.sort()
    print("Сортування:")
    for i in range(len(arr)):
        print(arr[i], " ")
    print('\n')

def elementValue(arr, key):
    for i in range(len(arr)):
        if arr[i]==key:
            print("Значення ",key, " існує!")
            break
    print('\n')

def elementCos(arr, key):
    false=False
    for i in arr: 
        for j in key: 
            if i==j: 
                true=True
                return true             
    return false

def fiveMin(arr):
    arr.sort()
    print("Пошук перших п’яти мінімальних елементів: ")
    for i in range(0,5):
        print(arr[i],end=" ")
    print('\n')

def fiveMax(arr):
    arr.sort(reverse=True)
    print("Пошук перших п’яти максимальних елементів: ")
    for i in range(0,5):
        print(arr[i],end=" ")
    print('\n')

def summ(arr):
    x=sum(arr)/len(arr)
    print("Пошук середнього арифметичного: ",x)
    print('\n')

def returned(arr):
    arr1=list(set(arr))
    print("Повернення списку:", arr1)
    print('\n')
























