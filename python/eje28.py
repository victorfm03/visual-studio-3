def entrada_datos():
    l = []
    p = input("Di una palabra: ").strip()
    while p.lower() != 'fin':
        l.append(p)
        p = input("Di una palabra: ").strip()
    return l


l = entrada_datos()

print("\nLista de palabras introducidas:")
print(l)

vocales = set()
consonantes = set()

for i in l:
    if i:
        primeraLetra = i[0].lower()
        if primeraLetra in 'aeiou':
            vocales.add(i)
        else:
            consonantes.add(i)

lista_vocales = list(vocales)
tupla_consonantes = tuple(consonantes)

print("\nPalabras que comienzan por vocal: ",lista_vocales)

print("\nPalabras que comienzan por consonante: ",tupla_consonantes)
