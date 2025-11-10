from ejemplo_modulo_datos import datos

print("__name__propio de ejemplo_modulo",__name__)

datos()

if __name__ == "__main__":
    print("soy el programa principal --> ejemplo_modulo")


from ejemplo_paquete.modulo1 import saludo
saludo()
if __name__ == "__main__":
    print("soy el programa principal --> ejemplo_modulo")