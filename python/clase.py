class Guitarra(Instrumento):
    def __init__(self,precio,tipo_cuerda):
        Instrumento.__init__(self,precio)
        self.tipo_cuerda=tipo_cuerda 
    
    def tipo(self):
        print(self.tipo_cuerda)

    g=Guitarra(100,'metal')
    g.tipo()