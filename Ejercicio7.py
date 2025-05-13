# Crea un programa que permita ingresar un número indefinido de **notas**, y al finalizar, calcule el **promedio** de todas ellas.


def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def main():
    print("Calculadora de Promedio de Notas")
    notas = []
    
    while True:
            entrada = input("Introduce una nota (o escribe 'fin' para terminar): ").strip().lower()
            if entrada == 'fin':
                break
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("Por favor, introduce una nota válida entre 0 y 10.")
            else:
                notas.append(nota)
    
    promedio = calcular_promedio(notas)
    if len(notas) > 0:
        print(f"El promedio de las {len(notas)} notas ingresadas es: {promedio:.2f}")
    else:
        print("No se ingresaron notas.")

if __name__ == "__main__":
    main()