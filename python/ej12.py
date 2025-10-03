import math
num1= int(input("Numero 1: "))
num2= int(input("Numero 2: "))
num3= int(input("Numero 3: "))

res=0
discriminante=num2**2-4*num1*num3

if discriminante<0:
    print("No hay solucion")
else:
    sol1=(-num2+math.sqrt(discriminante))/num1*2
    sol2=(-num2-math.sqrt(discriminante))/num1*2

    print(sol1)

    print(sol2)