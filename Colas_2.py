"""
Created on Tuesday 15/10/24

@author: Victor Mendoza
"""
class Cola:
    def crear_colas(self,clientes):
        self.Turnos = list(range(1,clientes + 1))
        self.Servicios = []

    def dar_turno(self):
        for i in range(len(self.Turnos)):
            self.servicio = input("\nIngrese su número de servicio con 3 dígitos sin contar la letra C (C104): ")
            self.Servicios.append(self.servicio)
            print(f"Su número de atención es: {self.Turnos[i]}")
        print("\nLos números de servicios son:")
        for num in self.Servicios:
            print(num)

    def atender_cliente(self):
        self.atencion = input("\nIngrese el número de servicio con 3 dígitos sin contar la letra A (A104): ")
        self.num_atencion = self.atencion[-3:]
        self.cliente = next((elem for elem in self.Servicios if elem[-3:] == self.num_atencion), None)
        print(f"Se atenderá a {self.cliente}")
        self.Resp = input("\n¿Desea atender a otro cliente?(Si/No) ").lower()
        if self.Resp == "si":
            self.atender_cliente()
        else:
            print("Gracias por su visita, vuelva pronto")

S = Cola()
print("Bienvenido a Seguros Mendoza")
S.crear_colas(5)
S.dar_turno()
S.atender_cliente()