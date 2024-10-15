"""
Created on Tuesday 15/10/24

@author: Victor Mendoza
"""
class Cola: # Se crea la clase Cola
    def crear_colas(self,clientes): # Método para crear las colas
        self.Turnos = list(range(1,clientes + 1)) # Cola con los turnos del 1 hasta la cantidad de clientes
        self.Servicios = [] # Cola con los números de servicio

    def dar_turno(self): # Método para dar los turnos
        for i in range(len(self.Turnos)): # Ciclo para pedir los números de servicio
            self.servicio = input("\nIngrese su número de servicio con 3 dígitos sin contar la letra C (C104): ")
            self.Servicios.append(self.servicio) # Se agregan los números de servicio a la cola
            print(f"Su número de atención es: {self.Turnos[i]}") # Se imprime el turno para el cliente

    def atender_cliente(self):
        print("\nLos números de servicios son:") # Se imprimen los números de servicio
        for num in self.Servicios:
            print(num)
        self.atencion = input("\nIngrese el número de servicio con 3 dígitos sin contar la letra A (A104): ") # Se pide el número de servicio para atender
        self.num_atencion = self.atencion[-3:] # Se guardan sólo los dígitos
        self.cliente = next((elem for elem in self.Servicios if elem[-3:] == self.num_atencion), None) # Se buscan en la lista de Servicios
        print(f"Se atenderá a {self.cliente}") # Se imprime a quien se atenderá
        self.Resp = input("\n¿Desea atender a otro cliente?(Si/No) ").lower() # Se pregunta si quieren atender a alguien más
        if self.Resp == "si": # Concicial if si la respuesta es si, se hace la llama recursiva del método
            self.Servicios.remove(self.cliente) # Se elimina al cliente atendido de la lista Servicios
            self.atender_cliente()
        else:
            print("\nGracias por su visita, vuelva pronto") # Condicional else con mensaje de despedida

S = Cola() # Se crea el objeto de la clase Cola
print("Bienvenido a Seguros Mendoza") # Mensaje de bienvenida
# Se usan los métodos de la clase
S.crear_colas(5)
S.dar_turno()
S.atender_cliente()
