#Escribe un programa que permita calcular el **interés compuesto** de un capital inicial, una tasa de interés anual y un número de años.

def calcular_interes_compuesto(capital_inicial, tasa_anual, anios):
    monto_final = capital_inicial * (1 + tasa_anual / 100) ** anios
    return monto_final

def main():
    print("Calculadora de Interés Compuesto")
    
    while True:
            capital_inicial = float(input("Introduce el capital inicial: "))
            tasa_anual = float(input("Introduce la tasa de interés anual (en %): "))
            anios = int(input("Introduce el número de años: "))
            
            monto_final = calcular_interes_compuesto(capital_inicial, tasa_anual, anios)
            print(f"El monto final después de {anios} años será: {monto_final:.2f}")

if __name__ == "__main__":
    main()