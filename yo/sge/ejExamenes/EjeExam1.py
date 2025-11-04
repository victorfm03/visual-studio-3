from functools import reduce

def entrada_datos():
    l=[]
    for i in range(1,3):
        nombre =input("Nombre del equipo "+str(i)+" :")
        puntos_favor=input("puntos a favor del equipo "+str(i)+" :")
        puntos_contra=input("puntos en contra del equipo "+str(i)+" :")
        partidos=input("partidos jugados del equipo "+str(i)+" :")
        
        l.append((nombre,puntos_favor,puntos_contra,partidos))
    print(l)

    return l

def calculo_estadisticas(lista_datos):
    d={}
    for equipo in lista_datos:
        diferencia=equipo[1]-equipo[2]
        tasa=diferencia/equipo[3]

        d[equipo[0]]=(diferencia,tasa)
    return d

def extremos(dicc_datos):
    
    equipo_max_diferencia=reduce(lambda item1,item2: item1 if item1[1][0]>item2[1][0] else item2,dicc_datos.items())
    equipo_min_diferencia=reduce(lambda item1,item2: item1 if item1[1][0]<item2[1][0] else item2,dicc_datos.items())
    return [equipo_max_diferencia[0], equipo_min_diferencia[0]]


def guardar_datos(dicc_datos):
    

def main():

    l=[('betis',100,80,3),('Sevilla',40,890,3),('rayo',56,23,3)]
    dicc_datos_estadistica=calculo_estadisticas(1)
    print(dicc_datos_estadistica)
    print(extremos(dicc_datos_estadistica))

if __name__=="__main__":
    main()