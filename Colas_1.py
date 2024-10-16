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
        print("\nLa primera Cola es:",self.Cola1) # Se imprime la primer cola
        print("La segundo Cola es:",self.Cola2) # Se imprime la segunda cola
        while self.Cola1 and self.Cola2:  # Se ejecuta hasta que ambas colas estén vacías
            self.Cola_Suma.append(self.Cola1[0] + self.Cola2[0])  # Sumar y agregar los primeros elementos de cada cola
            # Eliminar el primer elemento de cada cola
            self.Cola1.remove(self.Cola1[0])
            self.Cola2.remove(self.Cola2[0])
        print("\nLa suma de cada elemento de la primera y segunda cola es:",self.Cola_Suma) # Se imprime la tercer cola

Cola = Colas() # Se crea el objeto de la clase Colas

cantidad = int(input("Ingrese la cantidad de elementos que tendran las dos colas: ")) # Se pide la cantidad de elementos para cada cola
# Se usan los métodos de la clase
Cola.crear_colas(cantidad) 
Cola.suma_colas()
