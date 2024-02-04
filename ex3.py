def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(10)

nombre= input ("Porfavor Introduce tu nombre aquí:")

nombre= input ("Hola Adrià")
juan = 3
maria = 5
adan = 6
print(juan, maria, adan)
total_pomas = juan + maria + adan
print("Número Total de :", total_pomas)
otra_variable = 10
resultado = total_pomas * otra_variable - 7

print("Resultado de la operación:", resultado)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

user_miles = float(input("Ingresa la cantidad de millas a convertir a kilómetros: "))
user_kilometers = float(input("Ingresa la cantidad de kilómetros a convertir a millas: "))

user_miles_to_kilometers = user_miles * 1.61
user_kilometers_to_miles = user_kilometers / 1.61

print(user_miles, "millas son", round(user_miles_to_kilometers, 2), "kilómetros")
print(user_kilometers, "kilómetros son", round(user_kilometers_to_miles, 2), "millas")
x = 2.5
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))
paga = horas_trabajadas * coste_por_hora
print("La paga correspondiente es:", paga)
n = int(input("Ingrese un entero positivo: "))
if n <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    suma = (n * (n + 1)) // 2
    print("La suma de los primeros", n, "enteros positivos es:", suma)
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = peso / (estatura ** 2)
print("Tu índice de masa corporal es:", round(imc, 2))
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años de la inversión: "))
capital_obtenido = cantidad_invertir * (1 + interes_anual / 100) ** num_anios
print("El capital obtenido en la inversión es:", round(capital_obtenido, 2))
byte1 = int(input("Ingrese el primer byte de la dirección IP: "))
byte2 = int(input("Ingrese el segundo byte de la dirección IP: "))
byte3 = int(input("Ingrese el tercer byte de la dirección IP: "))
byte4 = int(input("Ingrese el cuarto byte de la dirección IP: "))
direccion_ip = f"{byte1}.{byte2}.{byte3}.{byte4}"
print("La dirección IP es:", direccion_ip)
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
total_minutos = (hour * 60 + mins + dura) % (24 * 60)
nueva_hora = total_minutos // 60
nuevos_minutos = total_minutos % 60
dia = int(input("Día del mes (1 a 30): "))
print(f"El evento finaliza el día {dia} a las {nueva_hora:02d}:{nuevos_minutos:02d}.")



