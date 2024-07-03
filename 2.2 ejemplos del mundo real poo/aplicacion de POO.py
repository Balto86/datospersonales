# -*- coding: utf-8 -*-


#Empezaremos creando una clase base llamada Empleado, que tendrá métodos y atributos comunes a todos los empleados.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        # Método para calcular el pago del empleado
        return self.salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}"

#Ahora, crearemos una clase derivada llamada Gerente, que hereda de la clase Empleado y agrega funcionalidad adicional específica para los gerentes.
class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def calcular_pago(self):
        # Método para calcular el pago del gerente (incluyendo bono)
        return self.salario + self.bono

    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Bono: ${self.bono}"

#Para demostrar encapsulación, podemos modificar la clase Empleado para hacer que salario sea privado y agregar métodos getter y setter para acceder y modificar el salario de manera controlada.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # salario es ahora privado

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario

    def calcular_pago(self):
        return self.__salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: ${self.__salario}"

#Para demostrar polimorfismo, podemos crear una función que procese una lista de empleados y llame al método calcular_pago(), aprovechando que tanto Empleado como Gerente tienen una implementación de este método, pero cada uno realiza cálculos diferentes según el tipo de empleado.
def procesar_pago(empleados):
    for empleado in empleados:
        print(f"{empleado} - Pago: ${empleado.calcular_pago()}")

# Crear algunos empleados y gerentes
empleado1 = Empleado("David", 8000)
gerente1 = Gerente("Yami", 7500, 1000)

# Lista de empleados
empleados = [empleado1, gerente1]

# Procesar y mostrar pagos
procesar_pago(empleados)
