class Fecha():
    def __init__(self):
        self._dia=1
    @property
    def dia(self):
        return self._dia
    @dia.setter
    def dia(self,dia):
        if dia > 0 and dia < 31:
            self._dia = dia
        else: print ("Error")

f = Fecha()
f.dia = 8
print(f.dia)