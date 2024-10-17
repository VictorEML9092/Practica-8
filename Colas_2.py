"""
Created on Tuesday 15/10/24

@author: Victor Mendoza
"""
class Cola: # Se crea la clase base Cola
    def crear_colas(self,clientes): # Método para crear las colas
        self.Turnos = list(range(1,clientes + 1)) # Cola con los turnos del 1 hasta la cantidad de clientes
        self.Servicios = [] # Cola con los números de servicio

    def dar_turno(self): # Método para dar los turnos
        self.servicio = input("\nIngrese su número de servicio con 3 dígitos sin contar la letra C (C104): ")
        self.Servicios.append(self.servicio) # Se agregan los números de servicio a la cola
        print(f"Su número de atención es: {self.Turnos[0]}") # Se imprime el turno para el cliente
        self.Turnos.pop(0) # Se elimina de la cola el turno que se le dio al cliente

    def atender_cliente(self):
        print("\nLos números de servicios son:") # Se imprimen los números de servicio
        for num in self.Servicios:
            print(num)

        self.atencion = input("\nIngrese el número de servicio con 3 dígitos sin contar la letra A (A104): ") # Se pide el número de servicio para atender
        self.num_atencion = self.atencion[-3:] # Se guardan sólo los dígitos
        while self.num_atencion != self.Servicios[0][-3:]: # Ciclo para comprobar que atienda al primero en la cola
            print("Debe ingresar el número de servicio que esta primero en la cola")
            self.atencion = input("\nIngrese el número de servicio con 3 dígitos sin contar la letra A (A104): ")
            self.num_atencion = self.atencion[-3:]

        cliente = self.Servicios.pop(0) # Se elimina de la cola al cliente que se atenderá
        print(f"Se atenderá a {cliente}") # Se imprime a quien se atenderá

        if self.Servicios: # Concicial if si la cola tiene clientes, se hace la llama recursiva del método
            self.atender_cliente()
        else:
            print("\nYa no quedan clientes para atender") # Condicional else con mensaje para avisar que ya no hay clientes

class Servicios(Cola): # Se crea la clase variante
    def servicio1(self): # Método para el primer servicio
        super().dar_turno() # Se usa el método heredado

    def servicio2(self): # Método para el primer servicio
        super().dar_turno() # Se usa el método heredado

    def servicio3(self): # Método para el primer servicio
        super().dar_turno() # Se usa el método heredado

S = Servicios() # Objeto de la clase variante

print("Bienvenido a Seguros Mendoza") # Mensaje de bienvenida
Clientes = int(input("\nIngrese la cantidad de clientes: ")) # Se pide la cantidad de clientes
S.crear_colas(Clientes) # Se usa el método de la clase base
for i in range(Clientes): # Ciclo para preguntar que servicio necesita el cliente
    Resp = input("\n¿Que servicio desea usar? (Vida, Vehículos, Médico) ").lower()
    if Resp == "vida":
        S.servicio1() # Se usa el método de la clase variante
    elif Resp == "vehículos":
        S.servicio2() # Se usa el método de la clase variante
    else:
        S.servicio3() # Se usa el método de la clase variante
S.atender_cliente() # Se usa el método de la clase base
