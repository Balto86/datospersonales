#Esta línea le dice a Python que el archivo está codificado en UTF-8 y evita problemas al interpretar caracteres especiales.
# -*- coding: utf-8 -*-

class Empleado:
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

# Define una plantilla para crear objetos de tipo empleado.
 #son atributos de cada objeto Empleado.
 #Calcula el salario anual multiplicando el salario mensual por 12.
    def calcular_salario_anual(self):
        return self.salario_mensual * 12

# Crear instancias de la clase Empleado
empleado1 = Empleado("Juan", 3000)
empleado2 = Empleado("María", 4000)

# Acceder a los atributos y métodos de los empleados
print(f"{empleado1.nombre} tiene un salario anual de {empleado1.calcular_salario_anual()} dólares.")
print(f"{empleado2.nombre} tiene un salario anual de {empleado2.calcular_salario_anual()} dólares.")

