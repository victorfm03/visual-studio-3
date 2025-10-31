l1=[]
l2=[]
l3=[]
l4=[]

for a in range(0,6):
    numero=int(input("Di un numero "))
    if (a+1)<=3:
        l1.append(numero)
        
    else:
        l2.append(numero)

l3.append(l1)
l4.append(l2)        
l3.sort()
l4.sort()

print(l1)
print(l2)

t=tuple(l3+l4)

print(t)