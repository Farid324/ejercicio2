import math

def logaritmo():
    try:
        numero = float(input("Ingrese el número: "))
        base = float(input("Ingrese la base: "))

        if numero <= 0:
            print("Error: El número debe ser mayor que 0")
            return
        if base <= 0 or base == 1:
            print("Error: La base debe ser mayor que 0 y diferente de 1")
            return
        
        resultado = math.log(numero, base)
        print(f"El logaritmo de {numero} en base {base} es: {resultado}")

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# Llamamos a la función para que se ejecute
logaritmo()
