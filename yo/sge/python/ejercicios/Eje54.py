from Clinica import Clinica
from Gato import Gato
from Perro import Perro
def main():

    clinica=Clinica()
    gato=Gato(1,23,"feliz")

    gato2=Gato(3,1,"torta")

    perro=Perro(2,10,1.4)

    print(clinica.altaMascota(gato))
    print(clinica.altaMascota(gato2))
    print(clinica.altaMascota(perro))
    print(f"{clinica.bajaMascota(3)}")
    print(clinica.pesoMaximoGato())
    print(clinica.listadoPerros())


if __name__ == "__main__":
    main()