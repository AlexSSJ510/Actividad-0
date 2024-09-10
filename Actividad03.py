class Calculadora:
    def calcular(self, multiplicando, multiplicador, sumador):
        result = multiplicando * multiplicador + sumador
        return result
    def potencia(self, base):
        return base ** 2

if __name__ == "__main__":
    calculadora = Calculadora()

    multiplicando = float(input("Ingresa multiplicando: "))
    multiplicador = float(input("Ingresa multiplicador: "))
    sumador = float(input("Ingresa sumador: "))

    resultado = calculadora.calcular(multiplicando, multiplicador, sumador)
    print("El resultado de la operación:")
    print(f"{multiplicando} * {multiplicador} + {sumador} = {resultado}\n")

    print("Calcular Potencia")
    base = float(input("Ingresa la base de la potencia: "))
    resultPot = calculadora.potencia(base)
    print(f"La potencia de {base} al cuadrado es {resultPot}")
