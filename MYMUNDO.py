# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado

    # Métodos getter
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    # Método encender (virtual)
    def encender(self):
        print("El vehículo está encendido.")

# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def encender(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está encendido.")

# Clase hija Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def encender(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} está encendida.")

# Clase principal
if __name__ == "__main__":
    mi_auto = Auto("Toyota", "Corolla")
    mi_moto = Motocicleta("Yamaha", "MT-07")

    mi_auto.encender()  # Salida: El auto Toyota Corolla está encendido.
    mi_moto.encender()  # Salida: La motocicleta Yamaha MT-07 está encendida.
