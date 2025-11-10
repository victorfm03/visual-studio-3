#importar una clase a la main
from Caja import Caja
from Sobre import Sobre



def main():

    sobre1=Sobre(1,0.1,True,True)
    caja=Caja(2,3,False,True)

    print(sobre1)
    print(caja)

#comando de python para ejecutar la main
if __name__=="__main__":
    main()
