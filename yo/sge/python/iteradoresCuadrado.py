def cuadrado(n):
    return n ** 2



l = [1, 2, 3]

l2 = map(lambda x: x+1, l)

print(l2)
print(list(l2))
print(list(l2))

l2 = map(lambda x: x+1, l)

l.append(4)
l.append(5)

elem=next(l2)

print("next: ",elem)

for elem in l2:
    print(elem)