num1= int(input("Numero 1: "))
num2= int(input("Numero 2: "))
num3= int(input("Numero 3: "))

mayor=0
menor=0

if num1>num2 and num1>num3:
    mayor=num1

    if num2<num3:
        menor=num2
    else:
        menor=num3

elif num2>num3:
    mayor=num2

    if num1<num3:
        menor=num1
    else:
        menor=num3

else:
    mayor=num3
    if num1<num2:
        menor=num1
    else:
        menor=num2

print(mayor,menor)