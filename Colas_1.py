"""
Created on Monday 14/10/24

@author: Victor Mendoza
"""
import random

class Colas:
    def crear_colas(self, candidad):
        self.Cola1 = [random.randint(1, 100) for _ in range(candidad)]
        self.Cola2 = [random.randint(1, 100) for _ in range(candidad)]
        self.Cola_Suma = []

    def suma_colas(self):
        for i in range(len(self.Cola1)):
            self.Cola_Suma.append(self.Cola1[i] + self.Cola2[i])
        print("\nLa primera Cola es:",self.Cola1)
        print("La segundo Cola es:",self.Cola2)
        print("\nLa suma de cada elemento de la primera y segunda cola es:",self.Cola_Suma)

Cola = Colas()

cantidad = int(input("Ingrese la cantidad de elementos que tendran las dos colas: "))

Cola.crear_colas(cantidad)
Cola.suma_colas()