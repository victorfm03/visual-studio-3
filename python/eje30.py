def definiciondeequipos():

    equipos=[]

    for a in range(0,3):
        equipo=input("Di un equipo: ")
        ganado=int(input("partidos ganados: "))
        perdido=int(input("partidos perdidos: "))
        empate=int(input("partidos empatados: "))
        equipos.append((equipo, ganado, perdido, empate))
    return equipos

datos=definiciondeequipos()
res=[]
for equipos in datos:
    puntos=equipos[1]*3+equipos[2]+equipos[3]*1
    res.append((equipos, puntos))

res.sort(key=lambda equipos:equipos[1])
res.revers()

print(res)