#importar una clase padre
from Envio import Envio
class Sobre(Envio):
    def __init__(self, id, peso, entregado,urgente):
        super().__init__(id, peso, entregado)
        self.__urgente=urgente
    
    @property
    def urgente(self):
        return self.__urgente
    
    @urgente.setter
    def urgente(self,valor):
        self.__urgente=valor
    
    def __str__(self):
        return f"{super().__str__()} - urgente:{self.urgente}"