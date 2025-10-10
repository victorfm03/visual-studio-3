listaCuentas={}

importe=0

entrada=input("Di una cuenta( ‘Ventas’, ‘Compras’, ‘Efectivo’, ‘Mercadería’, …): ")

while(entrada!="x"):
    importe=float(input("Di el importe: "))
    if(entrada in listaCuentas):
        listaCuentas[entrada]=listaCuentas[entrada]+(importe, )
    else:
        listaCuentas[entrada]=(importe, )

    entrada=input("Di una cuenta( ‘Ventas’, ‘Compras’, ‘Efectivo’, ‘Mercadería’, …): ")

print(listaCuentas)

lista_tuplas =[]

for (k,v) in listaCuentas.items():
    lista_tuplas.append((k,sum(v)))

print(lista_tuplas)