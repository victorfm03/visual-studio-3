from functools import reduce

def obtenerPasajeros(d):

    #filtro el diccionario que me pasan por parametro el primer paramtro y la primera posision
    ferrys=filter(lambda item:item[0][0]=="ferry",d.items())

    #mapeo el filtrado anterior y creo una tupla del valor del diccionario
    mapa=map(lambda item:tuple(item[1]),ferrys)

    #voy concatenando una tupla sumando a la tupla los valores del diccionario, Si la tupla esta vacia devuelve el valor inicial 
    return reduce(lambda acc,item:acc+(item[1],),mapa,())

def mayorCarga(d):
    #filtro el diccionario que me pasan por parametro el primer paramtro y la primera posision
    mercantes=filter(lambda item:item[0][0]=="mercante",d.items())

    #mapeo el filtro anterior y me quedo el id y la carga
    cargas=map(lambda item:(item[0][1],item[1][0]),mercantes)

    #me quedo con la tupla con la mayor carga
    maximo=reduce(lambda a,b:a if a[1]>b[1] else b,cargas)

    #devuelvo un array con el mayor id
    return [maximo[0]]

def totalCarga(d):

    return [reduce(lambda acc,item:acc+item[1][0],d.items(),0)]

def obtenerCarga(d):
    #filtro el diccionario que me pasan por parametro el primer paramtro y la primera posision
    mercantes=filter(lambda item:item[0][0]=="mercante",d.items())

    #mapeo el filtrado anterior y creo una tupla del valor del diccionario
    mapa=map(lambda item:tuple(item[1]),mercantes)

    #voy concatenando una tupla sumando a la tupla los valores del diccionario, Si la tupla esta vacia devuelve el valor inicial 
    return reduce(lambda acc,item:acc+(item[0],),mapa,())

def main():
    
    # creo un diccionario
    d={
        ("ferry",1):[2500,350],
        ("mercante",2):[120000,6500],
        ("mercante",3):[200000,3200],
        ("ferry",4):[3520,420]
    }
    print(f"pasajeros ferry: {obtenerPasajeros(d)}")
    print(f"maxima carga id : {mayorCarga(d)}")
    print(f"total carga : {totalCarga(d)}")
    print(f"cargas de los mercantes : {obtenerCarga(d)}")
    
if __name__=="__main__":
    main()