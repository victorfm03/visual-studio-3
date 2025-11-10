from Animal import Animal

class Carnivoro(Animal):

    def __init__(self, id_animal, especie,peligroso):
        super().__init__(id_animal, especie)
        self.__peligroso=peligroso
    
    @property
    def peligroso(self):
        return self.__peligroso
    
    @peligroso.setter
    def peligroso(self,valor):
        self.__peligroso=valor
    
    def __str__(self):
        return f"Carnivoro -> {super().__str__()}, peligroso: {self.__peligroso}"