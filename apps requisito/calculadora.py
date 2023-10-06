class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir por cero."
        return a / b

if __name__ == "__main__":
    calculadora = Calculadora()

    a = int(input("Ingrese el primer valor entero: "))
    b = int(input("Ingrese el segundo valor entero: "))

    suma = calculadora.sumar(a, b)
    resta = calculadora.restar(a, b)
    multiplicacion = calculadora.multiplicar(a, b)
    division = calculadora.dividir(a, b)

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")