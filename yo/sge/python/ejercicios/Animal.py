class Animal:
    def __init__(self,id_animal,especie):
        self.__id_animal=id_animal
        self.__especie=especie
    
    @property
    def id_animal(self):
        return self.__id_animal
    
    @id_animal.setter
    def id_animal(self,valor):
        self.__id_animal=valor
    
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self,valor):
        self.__especie=valor
    
    def __str__(self):
        return f"id: {self.__id_animal}, especie: {self.__especie}"
    
    
    