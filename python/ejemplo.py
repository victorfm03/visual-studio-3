#crear un diccionario vacio
d={}

#crear un diccionario con datos
d1={5: "Bingo","Sevilla": True, False : (2,4)}

#agregar elementos
d["k1"]="v1"
d["k2"]="v2"
d1["k3"]="v3"

#modificar el valor de una clave existente
d1[5]="Linea"

#Agregan claves nuevas y se machacan valores de claves existentes
d.update(d1)

print(" d: ",d)
print(" d1: ",d1)

#Recorridos de diccionarios

print("Recorridos de diccionarios")
print("Recorridos por calves")

for k in d.keys():
    print("Clave: ",k)

print("Recorridos por valores")
for v in d.values():
    print(v)

print("Recorridos por elementos")
for e in d.items():
    print("Elemento: ",e," clave: ",e[0]," Valor: ",e[1])

print("Recorridos por elementos v2")
for (k,v) in d.items():
    print("Clave: ",k," Valor: ",v)

print(d.get(6," no existe"))