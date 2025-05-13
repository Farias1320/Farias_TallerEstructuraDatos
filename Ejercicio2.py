#Crea un programa que convierta una temperatura de **Celsius a Fahrenheit** o de **Fahrenheit a Celsius**,
# dependiendo de la elección del usuario.


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        celsius = float(input("Introduce la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C son {fahrenheit:.2f}°F")
    elif opcion == "2":
        fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}°F son {celsius:.2f}°C")
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()