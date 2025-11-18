class Clinica:
    def __init__(self):
        self.__mascotas=[]

    @property
    def mascotas(self):
        return self.__mascotas
    
    @mascotas.setter
    def mascotas(self,valor):
        self.__mascotas=valor
    
    def altaMascota(self,oMascota):
        for a in self.__mascotas:
            if a.idMascota==oMascota.idMascota:
                return "Mascota repetida"
        self.__mascotas.append(oMascota)
        return "“Alta OK"

    def bajaMascota(self,idMascota):
        for a in self.__mascotas:
            if a.__idMascota==idMascota:
                self.__mascotas.remove(a)
                return "Mascota dada de baja"
        
        return "Mascota no localizada"
    
    def pesoMaximoGato(self):
        pesoMax=-1
        for a in self.__mascotas:
            if a.__class__.__name__=="Gato":
               
                if pesoMax<a.peso:
                    pesoMax=a.peso
        return pesoMax

    def  listadoPerros(self):
        l=""

        for a in self.__mascotas:
            if a.__class__.__name__=="Perro":
                l+=str(a)+"\n"
        return l
    
    def __str__(self):
        return f"Mascotas {self.__mascotas}"