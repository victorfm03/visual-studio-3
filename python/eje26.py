matriz=[[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input("Dime un numero["+str(i)+","+str(j)+"]")))

print(matriz)

matriz_res=[[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz_res[i].append(multiplicar_fila_columna(matriz,matriz,i,j))

def multiplicar_fila_columna(m1,m2,fila,columna):

    valor=0

    for n in range(0,len(m1[f])):
        valor=m1[f][i]*m2[i][c]
    
    return valor