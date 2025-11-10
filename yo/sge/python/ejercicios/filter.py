def es_par(param):
    return param%2==0

l=[1,2,3]

l2=filter(es_par,l)

print (list(l2))