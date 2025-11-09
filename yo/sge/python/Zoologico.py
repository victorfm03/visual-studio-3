class zoologico:

    def __init__(self,animales):
        self.__animales=[]

    def get_animales(self):
        return self.__animales
    
    def set_animales(self,animales):
        self.__animales=animales
    
    def altaAnimal(self,oAnimal):
        self.animales.append(oAnimal)
    
    def altaAnimal(self,idAnimal):
        self.animales.remove(idAnimal)
    
    def __str__(self):
        return "Animales: {self.__animales}"

