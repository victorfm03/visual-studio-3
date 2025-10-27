l=[1,5,6,7,5,7,8]

f=filter(lambda x : x %2==0, l)

print(f)

for a in f:
    print(a)


print(f)

print("-------------")

from functools import reduce

def sumar(x,y):
    return x+y

l=[1,2,3,4]

l2=reduce(sumar,l)

print(l2)