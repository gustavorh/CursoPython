# Tarea 1: Crear un conversor de moneda para transformar a dólares USD, de distintas monedas.
# 1) Peso Chileno 2) Peso Argentino 3) Peso Mexicano

moneda = input("Ingrese el tipo de moneda que desea convertir a dólares: ")
mensaje = """
1) Peso Chileno (CLP).
2) Peso Argentino (ARS).
3) Peso Mexicano (MXN).
Ingrese una opción para convertir (1, 2 o 3): """
opcion = int(input(mensaje))

if (moneda == "peso chileno" or opcion == 1):
    cantidad = int(input("Ingrese la cantidad en CLP a convertir: "))
    conversion = round(cantidad / 925, 2)
elif (moneda == "peso argentino" or opcion == 2):
    cantidad = int(input("Ingrese la cantidad en ARS a convertir: "))
    conversion = round(cantidad / 144, 2)
elif (moneda == "peso mexicano" or opcion == 3):
    cantidad = int(input("Ingrese la cantidad en MXN a convertir: "))
    conversion = round(cantidad / 19, 2)

print(f"La conversión de {cantidad}(s) {moneda}(s) a dólares (USD) es: {conversion}")
