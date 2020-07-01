import math
#функція range з числами float
def myrange(start, stop, step):
    n = int((stop - start) / step)
    range1 = map(lambda i: start + i*step, range(n))
    return range1

def func(x):
        return (x+math.cos(2*x))/(3*x) 
 
for i in myrange(2.3, 5.4, 0.8):
        y = func(i)
        print('func(', i, ') =', y)
print()
