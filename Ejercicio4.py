# Crea un programa que calcule la **potencia de un número**, dados una base y un exponente ingresados por el usuario.
# El programa debe permitir al usuario realizar múltiples cálculos sin reiniciar.

def calcular_potencia(base, exponente):
    return base ** exponente

def main():
    print("Cálculo de Potencias")
    
    while True:
        try:
            base = float(input("Introduce la base: "))
            exponente = float(input("Introduce el exponente: "))
            
            resultado = calcular_potencia(base, exponente)
            print(f"{base} elevado a la {exponente} es: {resultado:.2f}")
        except ValueError:
            print("Error: Por favor, introduce valores numéricos válidos.")
        
        continuar = input("¿Quieres realizar otro cálculo? (y/n): ").strip().lower()
        if continuar != 'y':
            print("Gracias por usar el programa.")
            break

if __name__ == "__main__":
    main()