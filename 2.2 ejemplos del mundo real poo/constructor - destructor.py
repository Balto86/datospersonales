class Contador:
    # Atributo de clase para contar instancias
    contador_instancias = 0

    def __init__(self):
        """
        Constructor de la clase Contador.
        Incrementa el contador de instancias al crear un nuevo objeto.
        """
        Contador.contador_instancias += 1

    def __del__(self):
        """
        Destructor de la clase Contador.
        Imprime un mensaje al destruir una instancia y decrementa el contador.
        """
        Contador.contador_instancias -= 1
        print(f"Se ha destruido una instancia de Contador. Instancias restantes: {Contador.contador_instancias}")

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos varias instancias de Contador
    c1 = Contador()
    c2 = Contador()

    # Python automáticamente llamará al destructor cuando se destruyan los objetos c1 y c2
