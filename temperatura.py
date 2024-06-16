# programacion tradicional
def ingresar_temperaturas_diarias():
    """
    Solicita al usuario ingresar las temperaturas diarias durante una semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio semanal de temperaturas.
    Recibe una lista de temperaturas diarias.
    Retorna el promedio.
    """
    total_temperaturas = sum(temperaturas)
    promedio = total_temperaturas / len(temperaturas)
    return promedio

def main():
    temperaturas_semana = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_semana)
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} °C")

if __name__ == "__main__":
    main()

    # utilizando POO
class RegistroClima:
    def __init__(self):
        """
        Constructor de la clase. Inicializa los atributos necesarios.
        """
        self.temperaturas_diarias = []  # Lista para almacenar las temperaturas diarias

    def ingresar_temperatura(self, temperatura):
        """
        Método para ingresar una temperatura diaria.
        """
        self.temperaturas_diarias.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        total_temperaturas = sum(self.temperaturas_diarias)
        promedio = total_temperaturas / len(self.temperaturas_diarias)
        return promedio

def main():
    registro = RegistroClima()

    # Ingresar temperaturas diarias (ejemplo: 7 días)
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        registro.ingresar_temperatura(temperatura)

    # Calcular y mostrar el promedio semanal
    promedio_semanal = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} °C")

if __name__ == "__main__":
    main()
