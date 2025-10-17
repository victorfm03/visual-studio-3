class Animal:

    def __init__(self, id_animal, especie):
        self.__id_animal=id_animal
        self.__especie=especie

    @property
    def id_animal(self):
        return self.__id_animal

    @id_animal.setter
    def id_animal(self,id_animal):
        self.__id_animal=id_animal

    @property
    def especie(self):
        return self.__especie

    @id_animal.setter
    def id_animal(self,especie):
        self.__especie=especie

    def __str__(self):
        
        return "Animal [id: "+str(self.__id_animal)+", especie: "+self.__especie+"]"

class Herbivoro(Animal):
    def __init__(self, id_animal, especie, kg_dia):
        Animal.__init__(self, id_animal, especie)
        self.__kg_dia=kg_dia

    def __str__(self){
        return "Herbivoro[id_animal: "+str(self.id_animal)", especie: "+self.especie+" ]"
    }

class Carnivoro(Animal):
    def __init__(self, id_animal, especie, peligroso):
        Animal.__init__(self, id_animal, especie)
        self.__peligroso=peligroso


    @property
    def peligroso():
        return self.__peligroso

    

    def __str__(self){
        return "Herbivoro[id_animal: "+str(self.id_animal)", especie: "+self.especie+" ]"
    }

animal1= Animal(1,"Pez")
animal2= Animal(2,"Ave")
animal1.id_animal=5
animal2.especie="m"