import csv
def entrada_datos():
    datos=[]
    for a in range(0,3):
       nombre_equipo= input("nombre del equipo: ")
       puntos_favor= int(input("puntos a favor: "))
       puntos_contra= int(input("puntos en contra: ")) 
       num_partidos= int(input("partidos jugados: "))
       datos.append((nombre_equipo,
                 puntos_favor,
                 puntos_contra,
                 num_partidos))
    print(datos)
    return datos

def calculo_estadisticas(lista):
    d={}
    for a in lista:
        diferencia=a[1]-a[2]
        tasa=diferencia/a[3]
        d[a[0]]=(diferencia,tasa)
    print(d)
    return d

def extremos(d):
    l=[]
    mayor=max(d,key=lambda item:d[item][0])
    menor=min(d,key=lambda item:d[item][0])
    l.append(mayor)
    l.append(menor)
    print(l)
    return l

def guardar_datos(d):
    
    #creo la variable que creara el fichero en modo escritura
    with open("baloncesto.csv","w",newline="") as fichero:
        
        #creo una variable que escribira los datos en formato csv
        escritor=csv.writer(fichero)

        #recorro los datos del diccionario y los escribo en cada linea
        
        for nombre,(diferencia,tasa) in d.items():
            escritor.writerow([nombre,diferencia,tasa])

def leer_csv(fichero):
    d={}
    with open(fichero,"r") as archivo:
        lector=csv.reader(archivo)
        
        for fila in lector:
            nombre=fila[0]
            diferencia=fila[1]
            tasa=fila[2]
            d[nombre]=(diferencia,tasa)
    print(d)

def main():
    datos=entrada_datos()
    estadisticas=calculo_estadisticas(datos)
    diccionario=extremos(estadisticas)
    fichero=guardar_datos(estadisticas)
    leer_csv("baloncesto.csv")
    


if __name__=="__main__":
    main()