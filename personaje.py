
# se realiza la creacion del personaje construyendo con datos numeriocos para dar comiemzo al juego
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def dano(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida = enemigo.vida - dano
        print(self.nombre, "ha realizado", dano, "puntos de dano a", enemigo.nombre)

        if enemigo.esta_vivo():
           print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("elige un arma: (1) Acero Valiryio, dano 8. Mata Dragones, dano 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("espada:", self.espada)

    def dano(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
        
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("libro:", self.libro)

    def dano(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa



poseidon = Guerrero("poseidon", 20, 10, 10, 100, 10)

Oscuro = Mago("0scuro", 15, 20, 25, 100, 40)
mi_personaje = Personaje("DfCl", 10, 4, 20, 100)


print("el nombre es", mi_personaje.nombre)
print("la fuerza es", mi_personaje.fuerza)
print("la inteligencia es", mi_personaje.inteligencia)
print("la defensa es", mi_personaje.defensa)
print("la vida es", mi_personaje.vida)
mi_personaje.atributos()
mi_personaje.subir_nivel(3, 6, 8)
mi_personaje.atributos()
print(mi_personaje.esta_vivo())
mi_personaje.morir()
mi_personaje.atributos()
mi_enemigo = Personaje("SYTC", 3, 5, 3, 5)
print(mi_personaje.dano(mi_enemigo))
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
print(poseidon.esta_vivo())
poseidon.atributos()
print(poseidon.espada)
poseidon.cambiar_arma()
Oscuro.atributos()
print(Oscuro.libro)
mi_personaje.atacar(poseidon)
Oscuro.atacar(mi_personaje)
poseidon.atacar(Oscuro)
poseidon.atributos()
Oscuro.atributos()
mi_personaje.atributos()

