from Animal import Animal

class Herbivoro(Animal):

    def __init__(self, id_animal, especie,kgDia):
        super().__init__(id_animal, especie)
        self.__kgDia=kgDia
    
    @property
    def kgDia(self):
        return self.__kgDia
    
    @kgDia.setter
    def kgDia(self,valor):
        self.__kgDia=valor
    
    def __str__(self):
        return f"Herbivoro -> {super().__str__()}, kilogramos al dia: {self.__kgDia}"