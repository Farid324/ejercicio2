def raiz():
    try:
        numero = float(input("Ingresa un número para la base: "))
        n = int(input("Ingresa un número positivo para la raíz: "))

        if numero < 0 and n % 2 == 0:
            raise ValueError("No se puede calcular la raíz par de un número negativo.")
        if n <= 0:
            raise ValueError("El índice de la raíz debe ser un número positivo mayor que 0.")

        resultado = pow(numero, 1/n)
        print(f"La raíz {n}-ésima de {numero} es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Ingresa valores numéricos válidos.")

# Ejecutar la función
raiz()
