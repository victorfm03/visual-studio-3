class Zoologico:

    def __init__(self):
        self.__animales=[]

    @property
    def animales(self):
        return self.__animales
    
    @animales.setter
    def animales(self,animales):
        self.__animales=animales
    
    def altaAnimal(self,oAnimal):
        for animal in self.__animales:
            if animal.id_animal==oAnimal.id_animal:
                return "animal repetido"
            
        self.__animales.append(oAnimal)
        return "Alta OK"
    
    def bajaAnimal(self,idAnimal):
        for animal in self.__animales:
            if animal.id_animal==idAnimal:
                self.animales.remove(animal)
                return "Animal dado de baja"
        return "Animal no localizado"
    
    def numKilosPasto(self):
        kilosTotal=0
        for animal in self.__animales:
            if animal.__class__.__name__=="Herbivoro":
                kilosTotal+=animal.kgDia
        return kilosTotal
    
    def listadoPeligrosos(self):
        listaPeligrosos=""

        for animal in self.__animales:
            if animal.__class__.__name__=="Carnivoro" and animal.peligroso:
                listaPeligrosos+=str(animal)+"\n"
        return listaPeligrosos
    
    def __str__(self):
        if not self.__animales:
            return "No hay animales en este zoo"
        
        return "\n".join(str(a) for a in self.__animales)

