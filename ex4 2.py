income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)

tax = max(0, round(tax, 0))
print("El impuesto es:", tax, "pesos")
year = int(input("Introduce un año:"))

if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Año Bisiesto")
    else:
        print("Año Común")
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while True:
    guess = int(input("Ingresa tu número: "))
    if guess == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
numero = int(input("Introduce un número entero:"))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuáles son tus ingresos mensuales? "))

if edad > 16 and ingresos >= 1000:
    print("Debes tributar.")
else:
    print("No necesitas tributar.")
nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo? (M/F) ")

if (sexo.upper() == 'M' and nombre.upper() > 'N') or (sexo.upper() == 'F' and nombre.upper() < 'M'):
    print("Perteneces al Grupo A.")
else:
    print("Perteneces al Grupo B.")
renta_anual = float(input("Ingrese su renta anual: "))

if renta_anual < 10000:
    impuesto = renta_anual * 0.05
elif 10000 <= renta_anual < 20000:
    impuesto = renta_anual * 0.15
elif 20000 <= renta_anual < 35000:
    impuesto = renta_anual * 0.20
elif 35000 <= renta_anual < 60000:
    impuesto = renta_anual * 0.30
else:
    impuesto = renta_anual * 0.45

print(f"El tipo impositivo que le corresponde es {int(impuesto / renta_anual * 100)}%.")
puntuacion = float(input("Ingrese la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    salario = 0.0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    salario = 2400 * 0.4
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    salario = 2400 * puntuacion

print(f"El nivel de rendimiento es {nivel} y el salario es {salario}€.")
edad = int(input("¿Cuál es tu edad? "))

if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

print(f"El precio de la entrada es: {precio_entrada}€.")
tipo_pizza = input("¿Quieres una pizza vegetariana? (Sí/No): ").lower()

if tipo_pizza == "sí":
    print("Ingredientes disponibles: Mozzarella, Tomate, Pimiento, Tofu")
else:
    print("Ingredientes disponibles: Mozzarella, Tomate, Peperoni, Jamón, Salmón")

print("Elige un ingrediente adicional.")
ip = input("Ingrese la dirección IP: ")

clase = "No válida"
if ip.startswith("10.") or ip.startswith("172.") or ip.startswith("192.168."):
    clase = "Privada"
elif ip.startswith("2.") or ip.startswith("1.") or ip.startswith("0."):
    clase = "Reservada"
elif 1 <= int(ip.split(".")[0]) <= 126:
    clase = "Clase A"
elif 128 <= int(ip.split(".")[0]) <= 191:
    clase = "Clase B"
elif 192 <= int(ip.split(".")[0]) <= 223:
    clase = "Clase C"

print(f"La dirección IP pertenece a la {clase}.")
