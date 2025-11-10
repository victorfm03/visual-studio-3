from Zoologico import Zoologico
from Herbivoro import Herbivoro
from Carnivoro import Carnivoro

def main():

    zoo=Zoologico()
    herb=Herbivoro(1,"koala",20)
    herb2=Herbivoro(2,"ciervo",30)

    carn1=Carnivoro(3,"Leon",True)
    carn2=Carnivoro(4,"pinguino",False)

    print(zoo.altaAnimal(herb))
    print(zoo.altaAnimal(herb))
    print(zoo.altaAnimal(herb2))
    print(zoo.altaAnimal(carn1))
    print(zoo.altaAnimal(carn2))

    print(zoo)

    print(f"nº de kilogramos necesarios al dia: {zoo.numKilosPasto()}")
    print(f"listado de animales peligrosos: {zoo.listadoPeligrosos()}")

    print(f"baja animal(2): {zoo.bajaAnimal(2)}")
    print(f"baja animal(7): {zoo.bajaAnimal(7)}")
    


if __name__ == "__main__":
    main()