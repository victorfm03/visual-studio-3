from Mascota import Mascota

class Perro(Mascota):
    
    def __init__(self, idMascota, peso,altura):
        super().__init__(idMascota, peso)
        self.__altura=altura
    
    @property
    def altura(self):

       return self.__altura
    
    @altura.setter
    def altura(self,valor):

        self.__altura=valor
    
    def __str__(self):
        return f"{super().__str__()}, altura: {self.__altura}"