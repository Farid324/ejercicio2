class Aritmetica:
    # Farid Ramirez Arancibia
    def suma(self):
        total = float(input("Ingrese el primer número: "))
        
        while True:
            numero = input("Ingrese otro número para sumar (o presione Enter para terminar): ")
            if numero == "":
                break
            total += float(numero)
            print(f"Suma actual: {total}")
        
        print(f"Resultado final: {total}")

    # Fernando Alan Peralta Andia
    def resta(self):
        total = float(input("Ingrese el primer número: "))
        
        numero = input("Ingrese otro número para restar: ")      
        total -= float(numero)
        print(f"Resta Total: {total}")
        
        print(f"Resultado final: {total}")

    # Grissell Ingrid Coca Cadima
    def exponenciacion(self, base, exponente):
        resultado = 1
        while exponente > 0:
            if exponente % 2 == 1:
                resultado *= base
            base *= base 
            exponente //=2
        return resultado
    
    # Camila Wara Fernandez Sandoval
    def multiplicacion(self):
        total = float(input("Ingrese el primer número: "))
        
        numero = float(input("Ingrese otro número: "))  
        total *= numero
        print(f"Multiplicación actual: {total}")
        
        while True:
            numero = input("Ingrese otro número o presione Enter para terminar: ")
            if numero == "":
                break
            total *= float(numero)
            print(f"Multiplicación actual: {total}")
        
        print(f"Resultado final: {total}")

    # Jhoswer Eddy Navia Guevara
    def division(self):
        while True:
            try:
                dividendo = float(input("Ingrese el dividendo: "))
                divisor = float(input("Ingrese el divisor: "))
                
                if divisor == 0:
                    print("Error: No se puede dividir por cero. Intente de nuevo.")
                    continue
                
                resultado = dividendo / divisor
                print(f"Resultado: {resultado}")
                break
                
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
    

    # Carla VIllarroel Mendieta
    def radicacion(self):
        total = float(input("Ingrese el número base (radicando): "))
        
        indice = float(input("Ingrese el índice de la raíz: "))  
        total **= (1 / indice)
        print(f"Raíz actual: {total}")
        
        while True:
            indice = input("Ingrese otro índice de raíz o presione Enter para terminar: ")
            if indice == "":
                break
            total **= (1 / float(indice))
            print(f"Raíz actual: {total}")
        
        print(f"Resultado final: {total}")
        
    # Maite Suarez Arraya
    def modulo(self):
        while True:
            try:
                dividendo = float(input("Ingrese el primer número: "))
                divisor = float(input("Ingrese el segundo número: "))
                
                if divisor == 0:
                    print("Error: No se puede calcular el módulo con divisor cero. Intente de nuevo.")
                    continue
                
                resultado = dividendo % divisor
                print(f"Resultado del módulo: {resultado}")
                break
                
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

def menu():
    aritmetica = Aritmetica()
    
    while True:
        print("\n=== Menú de Operaciones Aritméticas ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Exponenciación")
        print("6. Radicación")
        print("7. Módulo")
        print("8. Salir")
        
        opcion = input("Seleccione una operación (1-8): ")
        
        if opcion == "1":
            aritmetica.suma()
        elif opcion == "2":
            aritmetica.resta()
        elif opcion == "3":
            aritmetica.multiplicacion()
        elif opcion == "4":
            aritmetica.division()
        elif opcion == "5":
            print("---------Exponenciación---------")
            base = float(input("Ingrese el número de la base: "))
            exponente = int(input("Ingrese el número del exponente: "))
            resultado = aritmetica.exponenciacion(base, exponente)
            print(f"Resultado: {resultado}")
        elif opcion == "6":
            print("---------Radicación---------")
            aritmetica.radicacion()
        elif opcion == "7":
            print("---------Módulo---------")
            aritmetica.modulo()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Operación aún no implementada. Intente otra opción.")

if __name__ == "__main__":
    menu()

