def leer_tapas():
    l=[]
    for a in range(1,5):
        nombre=input("nombre tapa: ")
        precio= float(input("precio_unitario: "))
        cantidad=int(input("cantidad vendida"))
        l.append((nombre,precio,cantidad))
    return l

def calcular_estadisticas_tapas(lista_ventas):
    d={}
    popularidad=""
    for a in lista_ventas:
        if a[2]>25:
            popularidad="Alta"
        elif a[2]>15:
            popularidad="Media"
        else:
            popularidad="Baja"
        d[a[0]]=((a[1]*a[2]),((a[1]*a[2])*(10/100)),popularidad)
    return d


def analizar_rendimiento_tapas(dicc_estadisticas):

    filtrado=filter(lambda item:item[1][2]=="Alta",dicc_estadisticas.items())
    promedio=sum(map(lambda item:item[1][1],dicc_estadisticas.items()))/len(dicc_estadisticas)
    mayor=max(dicc_estadisticas,key=lambda item:dicc_estadisticas[item][0])
    
    return(dict(filtrado),promedio,mayor)

def main():
    l=leer_tapas()
    d=calcular_estadisticas_tapas(l)
    r=analizar_rendimiento_tapas(d)
    print(l)
    print(d)
    print(r)
    

if __name__=="__main__":
    main()