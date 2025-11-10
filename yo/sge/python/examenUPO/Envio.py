class Envio:
    def __init__(self,id,peso,entregado):
        self.__id=id
        self.__peso=peso
        self.__entregado=entregado
    
    #defino los getters
    @property
    def id(self):
        return self.__id
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def entregado(self):
        return self.__entregado
    
    #defino los setters
    @id.setter
    def id(self,valor):
        self.__id=valor
    
    @peso.setter
    def peso(self,valor):
        self.__peso=valor

    @entregado.setter
    def entregado(self,valor):
        self.__entregado=valor

    #defino el toString
    def __str__(self):
        return f"ID: {self.__id} – Peso: {self.__peso} – Entregado: {self.__entregado}"
    