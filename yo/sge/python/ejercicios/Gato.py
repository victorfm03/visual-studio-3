from Mascota import Mascota

class Gato(Mascota):
    
    def __init__(self, idMascota, peso,raza):
        super().__init__(idMascota, peso)
        self.__raza=raza
    
    @property
    def raza(self):

       return self.__raza
    
    @raza.setter
    def raza(self,valor):

        self.__raza=valor
    
    def __str__(self):
        return f"{super().__str__()}, Raza: {self.__raza}"