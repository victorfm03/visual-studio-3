d={}

for (a in range(0,5)):
    nombreActual=String(input("Di un nombre"))
    dia=String(input("Di un dia de trabajo"))

    if(nombreActual in d.keys()):
        print("Trabajador ya registrado")
    elif dia not in ['Lunes','Martes','Miercoles','Jueves','Viernes']:
        print("Dia no valido")
    elif(dia in d.values()):
        print("Dia ya ocupado")
    