def registrar_datos(d):
    fila=int(input("di una fila: "))
    columna=int(input("di una columna: "))

    elemento=input("di un elemento")

    if fila in [1,2,3,4,5] and columna in [1,2,3,4,5] and elemento in ['c','s','x','e']:
        d[(fila, columna)]=elemento

def coordenadas_tipo(d):
    tipo_elem=input("di un elemento a buscar: ")

    res_filtro=filter(lambda item:item[1]==tipo_elem, d.items())
    mapa=map(lambda item:item[0],res_filtro)
    print(list(mapa))

def main():
    d={}

    #entrada de datos
    opcion=input("introducir un elemento [s/n]: ")
    while opcion != 'n':
        registrar_datos(d)
        opcion=input("introducir otro elemento [s/n]: ")
    
    coordenadas_tipo(d)

if __name__=="__main__":
    main()