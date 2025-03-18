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
    def raiz(self):
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
        print("9. Raiz")
        print("10. Salir")
        
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
            print("---------Raiz n-ésima---------")
            aritmetica.raiz()
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Operación aún no implementada. Intente otra opción.")

if __name__ == "__main__":
    menu()
class Fraccion:
    def _init_(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        
        # Simplificar la fracción al crear
        mcd = self.calcular_mcd(abs(numerador), abs(denominador))
        
        # Manejar el signo
        if denominador < 0:
            numerador = -numerador
            denominador = -denominador
            
        self.numerador = numerador // mcd
        self.denominador = denominador // mcd
        
    def calcular_mcd(self, a, b):
        """Calcula el máximo común divisor usando el algoritmo de Euclides"""
        while b:
            a, b = b, a % b
        return a
    
    def _str_(self):
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"
    
    def _repr_(self):
        return self._str_()


class OperacionesFracciones:
    @staticmethod
    def suma(fraccion1, fraccion2):
        """Suma dos fracciones y devuelve el resultado simplificado"""
        nuevo_numerador = (fraccion1.numerador * fraccion2.denominador + 
                           fraccion2.numerador * fraccion1.denominador)
        nuevo_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    @staticmethod
    def resta(fraccion1, fraccion2):
        """Resta dos fracciones y devuelve el resultado simplificado"""
        nuevo_numerador = (fraccion1.numerador * fraccion2.denominador - 
                           fraccion2.numerador * fraccion1.denominador)
        nuevo_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    @staticmethod
    def multiplicacion(fraccion1, fraccion2):
        """Multiplica dos fracciones y devuelve el resultado simplificado"""
        nuevo_numerador = fraccion1.numerador * fraccion2.numerador
        nuevo_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    @staticmethod
    def division(fraccion1, fraccion2):
        """Divide dos fracciones y devuelve el resultado simplificado"""
        if fraccion2.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con valor cero")
        nuevo_numerador = fraccion1.numerador * fraccion2.denominador
        nuevo_denominador = fraccion1.denominador * fraccion2.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)


def obtener_fraccion():
    """Solicita al usuario los datos de una fracción y la devuelve"""
    while True:
        try:
            numerador = int(input("Ingrese el numerador: "))
            denominador = int(input("Ingrese el denominador: "))
            return Fraccion(numerador, denominador)
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")


def menu_principal():
    """Muestra el menú principal y gestiona la interacción con el usuario"""
    print("\n=== CALCULADORA DE FRACCIONES ===")
    print("1. Suma de fracciones")
    print("2. Resta de fracciones")
    print("3. Multiplicación de fracciones")
    print("4. División de fracciones")
    print("5. Salir")
    
    opcion = input("\nSeleccione una opción (1-5): ")
    
    if opcion == '5':
        return False
    
    if opcion in ['1', '2', '3', '4']:
        print("\nPrimera fracción:")
        fraccion1 = obtener_fraccion()
        
        print("\nSegunda fracción:")
        fraccion2 = obtener_fraccion()
        
        if opcion == '1':
            resultado = OperacionesFracciones.suma(fraccion1, fraccion2)
            print(f"\nResultado de la suma: {fraccion1} + {fraccion2} = {resultado}")
        elif opcion == '2':
            resultado = OperacionesFracciones.resta(fraccion1, fraccion2)
            print(f"\nResultado de la resta: {fraccion1} - {fraccion2} = {resultado}")
        elif opcion == '3':
            resultado = OperacionesFracciones.multiplicacion(fraccion1, fraccion2)
            print(f"\nResultado de la multiplicación: {fraccion1} × {fraccion2} = {resultado}")
        elif opcion == '4':
            try:
                resultado = OperacionesFracciones.division(fraccion1, fraccion2)
                print(f"\nResultado de la división: {fraccion1} ÷ {fraccion2} = {resultado}")
            except ValueError as e:
                print(f"\nError: {e}")
    else:
        print("\nOpción no válida. Por favor, intente nuevamente.")
    
    return True


def main():
    """Función principal del programa"""
    print("Bienvenido a la Calculadora de Fracciones")
    
    continuar = True
    while continuar:
        continuar = menu_principal()
    
    print("\n¡Gracias por usar la Calculadora de Fracciones!")


if _name_ == "_main_":
    main()
