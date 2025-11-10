num1= int(input("Di el primer numero: "))
num2= int(input("Di el segundo numero: "))

res=""
menor=0
mayor=0

if num1>num2:
    mayor=num1
    menor=num2
elif num1<num2:
    mayor=num2
    menor=num1
else:
    print("Son iguales")

for a in range(menor+1,mayor):
    if a%7==0:
        res+=str(a)+" "
if res=="":
    print("No hay numero divisibles")
else:
    print(res)