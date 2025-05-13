#Escribe un programa que calcule el **área** y el **perímetro** de un círculo, dado el valor de su radio.
# El programa debe validar que el radio sea un valor positivo.

import math

def CalcularAreaPerimetro_circulo():
    try:
        radio = float(input("Introduce el radio del círculo: "))
        if radio <= 0:
            print("El radio debe ser un valor positivo.")
            return
        
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Llamar a la función
CalcularAreaPerimetro_circulo()
