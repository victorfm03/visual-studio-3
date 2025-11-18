class Mascota():
    def __init__(self,idMascota,peso):
        self.__idMascota=idMascota
        self.__peso=peso
    
    @property
    def idMascota(self):
        return self.__idMascota
    
    @idMascota.setter
    def idMascota(self,valor):
        self.__idMascota=valor
    
    def __str__(self):
        return f"ID: {self.__idMascota}, Peso: {self.__peso}"