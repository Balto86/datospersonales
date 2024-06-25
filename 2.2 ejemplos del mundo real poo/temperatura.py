def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a grados Fahrenheit.
    :param celsius: float, temperatura en grados Celsius.
    :return: float, temperatura en grados Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicita al usuario la temperatura en grados Celsius
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convierte a grados Fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Imprime el resultado
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f}")
