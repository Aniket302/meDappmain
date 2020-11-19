import random
import math

a = int(input())
n = int(input())
random.seed(a)

def distance(x,y):
    s = x*x+y*y
    r = math.sqrt(s)
    return r


arr = [(random.randint(0,2), random.randint(0,2)) for _ in range(n)]
    
c1 = 0
c2 = 0
total = 0

for i in arr:

    total += distance(i[0],i[1])

    if (distance(i[0], i[1]) <= 1):
        c1+=1

    if (distance(i[0], i[1])>=0.5 and distance(i[0], i[1]) <= 1.5):
        c2+=1

print(c1/n)
print(c2/n)
print('%.4f'%(total/n))