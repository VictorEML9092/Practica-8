"""
Created on Monday 14/10/24

@author: Victor Mendoza
"""
import random
# Se crea la clase Colas
class Colas:
    def crear_colas(self, candidad): # Método para crear las colas
        self.Cola1 = [random.randint(1, 100) for _ in range(candidad)] # Primera cola con números aleatorios
        self.Cola2 = [random.randint(1, 100) for _ in range(candidad)] # Segunda cola con números aleatorios
        self.Cola_Suma = [] # Tercer cola para sumar los elementos de las dos primeras colas

    def suma_colas(self): # Método para sumar las colas
        for i in range(len(self.Cola1)): # Ciclo para sumar cada elemento
            self.Cola_Suma.append(self.Cola1[i] + self.Cola2[i]) # El resultado se agrega a la tercer cola
        print("\nLa primera Cola es:",self.Cola1) # Se imprime la primer cola
        print("La segundo Cola es:",self.Cola2) # Se imprime la segunda cola
        print("\nLa suma de cada elemento de la primera y segunda cola es:",self.Cola_Suma) # Se imprime la tercer cola

Cola = Colas() # Se crea el objeto de la clase Colas

cantidad = int(input("Ingrese la cantidad de elementos que tendran las dos colas: ")) # Se pide la cantidad de elementos para cada cola
# Se usan los métodos de la clase
Cola.crear_colas(cantidad) 
Cola.suma_colas()
