from Conjunto import Conjunto


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self,op, A, B):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3':
            func(A, B)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')
    def opcion1(self,A, B):
        C = (A+B)
        print(C)
    def opcion2(self,A, B):
      C = (A-B)
      print(C)
    def opcion3(self,A, B):
        if(A == B):
            print("Ambos conjuntos son iguales")
        else:
            print("Los conjuntos no son iguales")
       
    


