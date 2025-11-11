#a
def registrar_datos(d):
    fila=int(input("di una fila: "))
    columna=int(input("di una columna: "))

    elemento=input("di un elemento")

    if fila in [1,2,3,4,5] and columna in [1,2,3,4,5] and elemento in ['c','s','x','e']:
        d[(fila, columna)]=elemento

#b
def coordenadas_tipo(d):
    tipo_elem=input("di un elemento a buscar: ")

    res_filtro=filter(lambda item:item[1]==tipo_elem, d.items())
    mapa=map(lambda item:item[0],res_filtro)
    print(list(mapa))

def generar_txt(d):
    with open("mapa.txt","w") as f:
        for a in range(1,6):
            fila=""
            for b in range(1,6):
                fila+=d.get((b,a)," ")
            f.write(fila+"\n")

def main():
    d={}

    #entrada de datos
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar datos")
        print("2. Listar coordenadas por tipo")
        print("3. Guardar mapa en fichero")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_datos(d)
        elif opcion == "2":
            coordenadas_tipo(d)
        elif opcion == "3":
            generar_txt(d)
        
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

"""
    opcion=input("introducir un elemento [s/n]: ")
    while opcion != 'n':
        registrar_datos(d)
        opcion=input("introducir otro elemento [s/n]: ")
    
    coordenadas_tipo(d)
    generar_txt(d)
    """


if __name__=="__main__":
    main()