num=int(input("Di un numero: "))

for a in range(num):

    for b in range(num):
        print(f"{(a+1)+(b+1)}",end=" ")
    print()
