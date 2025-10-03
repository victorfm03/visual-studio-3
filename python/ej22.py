vocal=input("Di una letra ")

numVocales=0

numNoVocales=0

while vocal !=" ":
    if vocal=="a" or vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u":
        
        numVocales+=1
        print(f"{vocal} es vocal")

    else:
        numNoVocales+=1
        print(f"{vocal} es no vocal")
    
    vocal=input("Di una letra ")

print(numVocales," vocal/es")
print(numNoVocales," no vocal/es")