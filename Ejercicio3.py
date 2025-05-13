#Escribe un programa que calcule el **perímetro** y el **área** de un rectángulo, dados su largo y ancho. 
#El programa debe validar que ambos valores sean positivos.

def calcular_perimetro(largo, ancho):
    return 2 * (largo + ancho)

def calcular_area(largo, ancho):
    return largo * ancho

def main():
    print("Cálculo del Perímetro y Área de un Rectángulo")
    
    try:
        largo = float(input("Introduce el largo del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
        
        if largo <= 0 or ancho <= 0:
            print("Error: El largo y el ancho deben ser valores positivos.")
        else:
            perimetro = calcular_perimetro(largo, ancho)
            area = calcular_area(largo, ancho)
            
            print(f"El perímetro del rectángulo es: {perimetro:.2f}")
            print(f"El área del rectángulo es: {area:.2f}")
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()