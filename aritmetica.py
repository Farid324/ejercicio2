import math
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
    
    #Camila Wara Fernandez Sandoval
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

    #Rodrigo Pierre Soliz Cespedes
    def logaritmo(self):
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
    #Melina Alcira Montaño Guzman
    def fibonacci(self):
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

     # Brenda Calizaya
    def fracciones(self):
        print("\n=== Operaciones con Fracciones ===")
        print("1. Suma de fracciones")
        print("2. Resta de fracciones")
        print("3. Multiplicación de fracciones")
        print("4. División de fracciones")
        print("5. Simplificar fracción")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una operación (1-6): ")
        
        if opcion == "1":
            self.suma_fracciones()
        elif opcion == "2":
            self.resta_fracciones()
        elif opcion == "3":
            self.multiplicacion_fracciones()
        elif opcion == "4":
            self.division_fracciones()
        elif opcion == "5":
            self.simplificar_fraccion()
        elif opcion == "6":
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            self.fracciones()
    
    def suma_fracciones(self):
        try:
            print("\n--- Suma de Fracciones ---")
            num1 = int(input("Ingrese el numerador de la primera fracción: "))
            den1 = int(input("Ingrese el denominador de la primera fracción: "))
            
            num2 = int(input("Ingrese el numerador de la segunda fracción: "))
            den2 = int(input("Ingrese el denominador de la segunda fracción: "))
            
            # Verificar denominadores no cero
            if den1 == 0 or den2 == 0:
                print("Error: El denominador no puede ser cero.")
                return
            
            # Calcular suma: (a/b + c/d) = (a*d + b*c)/(b*d)
            nuevo_num = (num1 * den2) + (num2 * den1)
            nuevo_den = den1 * den2
            
            resultado = Fraccion(nuevo_num, nuevo_den)
            print(f"Resultado: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def resta_fracciones(self):
        try:
            print("\n--- Resta de Fracciones ---")
            num1 = int(input("Ingrese el numerador de la primera fracción: "))
            den1 = int(input("Ingrese el denominador de la primera fracción: "))
            
            num2 = int(input("Ingrese el numerador de la segunda fracción: "))
            den2 = int(input("Ingrese el denominador de la segunda fracción: "))
            
            # Verificar denominadores no cero
            if den1 == 0 or den2 == 0:
                print("Error: El denominador no puede ser cero.")
                return
            
            # Calcular resta: (a/b - c/d) = (a*d - b*c)/(b*d)
            nuevo_num = (num1 * den2) - (num2 * den1)
            nuevo_den = den1 * den2
            
            resultado = Fraccion(nuevo_num, nuevo_den)
            print(f"Resultado: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def multiplicacion_fracciones(self):
        try:
            print("\n--- Multiplicación de Fracciones ---")
            num1 = int(input("Ingrese el numerador de la primera fracción: "))
            den1 = int(input("Ingrese el denominador de la primera fracción: "))
            
            num2 = int(input("Ingrese el numerador de la segunda fracción: "))
            den2 = int(input("Ingrese el denominador de la segunda fracción: "))
            
            # Verificar denominadores no cero
            if den1 == 0 or den2 == 0:
                print("Error: El denominador no puede ser cero.")
                return
            
            # Calcular multiplicación: (a/b * c/d) = (a*c)/(b*d)
            nuevo_num = num1 * num2
            nuevo_den = den1 * den2
            
            resultado = Fraccion(nuevo_num, nuevo_den)
            print(f"Resultado: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def division_fracciones(self):
        try:
            print("\n--- División de Fracciones ---")
            num1 = int(input("Ingrese el numerador de la primera fracción: "))
            den1 = int(input("Ingrese el denominador de la primera fracción: "))
            
            num2 = int(input("Ingrese el numerador de la segunda fracción: "))
            den2 = int(input("Ingrese el denominador de la segunda fracción: "))
            
            # Verificar denominadores y numerador de la segunda fracción no cero
            if den1 == 0 or den2 == 0 or num2 == 0:
                print("Error: El denominador no puede ser cero y el numerador de la segunda fracción tampoco puede ser cero para la división.")
                return
            
            # Calcular división: (a/b / c/d) = (a*d)/(b*c)
            nuevo_num = num1 * den2
            nuevo_den = den1 * num2
            
            resultado = Fraccion(nuevo_num, nuevo_den)
            print(f"Resultado: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def simplificar_fraccion(self):
        try:
            print("\n--- Simplificar Fracción ---")
            num = int(input("Ingrese el numerador de la fracción: "))
            den = int(input("Ingrese el denominador de la fracción: "))
            
            # Verificar denominador no cero
            if den == 0:
                print("Error: El denominador no puede ser cero.")
                return
            
            resultado = Fraccion(num, den)
            print(f"Fracción simplificada: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")

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
        print("8. Logaritmo")
        print("9. Fibonacci")
        print("10. Fracciones")
        print("11. Salir")
        
        opcion = input("Seleccione una operación (1-10): ")
        
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
            print("---------Logaritmo---------")
            aritmetica.logaritmo()
        elif opcion == "9":
            print("---------Fibonacci---------")
            aritmetica.fibonacci()
        elif opcion == "10":
             print("---------Fracciones---------")
             aritmetica.fracciones()
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Operación aún no implementada. Intente otra opción.")

if __name__ == "__main__":
    menu()

