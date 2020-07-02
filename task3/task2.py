import random
n=int(input('n=m='))
h=('')
arr=[[random.randint(-10, 10) for i in range(n)] for j in range(n)]
for i in arr:
    print(i)
for k in range(0,n-1):
    for l in range(k+1,n):
        if arr[k][l]!=arr[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Матриця симетрична')
else:
    print('Матриця не симетрична')
