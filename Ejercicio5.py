# Desarrolla un programa que convierta una cantidad dada en **millas** a su equivalente en **kilómetros** y **metros**.


def Convertidor(millas):
    kilometros = millas * 1.60934  # 1 milla = 1.60934 kilómetros
    metros = kilometros * 1000    # 1 kilómetro = 1000 metros
    return kilometros, metros

def main():
    print("Conversor de Millas a Kilómetros y Metros")
    
    while True:
            millas = float(input("Introduce la cantidad en millas: "))
            
            kilometros, metros = Convertidor (millas)
            print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros o {metros:.2f} metros.")
        
if __name__ == "__main__":
    main()