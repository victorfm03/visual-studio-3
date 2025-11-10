#importar una clase padre
from Envio import Envio
class Caja(Envio):
    def __init__(self, id, peso, entregado,fragil):
        super().__init__(id, peso, entregado)
        self.__fragil=fragil
    
    @property
    def fragil(self):
        return self.__fragil
    
    @fragil.setter
    def fragil(self,valor):
        self.__fragil=valor
    
    def __str__(self):
        return f"{super().__str__()} - fragil:{self.fragil}"