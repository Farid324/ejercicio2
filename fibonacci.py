def fibonacci():
    while True:
        try:
            n = int(input("Ingrese la cantidad de números de Fibonacci a calcular: "))
            if n < 0:
                print("Por favor, ingrese un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
        print(fib_sequence)

fibonacci()