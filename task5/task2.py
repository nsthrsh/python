import math
import itertools

def y(x, n):
        return pow(-1,n-1)*((2*n-1)/(pow(2,n)*math.factorial(n))*pow(x,n))
p=0.0001
a=-0.8
b=0.8
n=0
i=0
for x in itertools.count(start=a, step=0.2):
    if x>b:
        break
    tmp = y(x,n)
    res = tmp
    i+=1
    while (abs(tmp)>=p):
        n+=1
        tmp= y(x, n)
        res+= tmp
    print(" х  ", "      "," y  ", "      ")
    print("----------------------")
    print('%.1f' %x, "      ", res, "      \n")
print( "Iтерацій:", i)

