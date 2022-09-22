# Funciones

def holaMundo():
    print("Hola mundo desde una función!")

# holaMundo()

# Refactorizando Convertidor de Moneda

def conversorMoneda(valorDolar):
    pesos = int(input("Ingrese un valor en pesos chilenos (CLP): "))
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    print(str(dolares) + " dolares") 