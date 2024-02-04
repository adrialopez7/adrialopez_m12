def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_per_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_per_month[month - 1]
def quadrat(num):
    return num ** 2

def arrel(num):
    return num ** 0.5

def pitagoras(c, a):
    return arrel(quadrat(c) + quadrat(a))

result = pitagoras(3, 4)
print(result)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
def liters_100km_to_miles_gallon(liters):
    miles_per_km = 0.621371
    gallons_per_liter = 0.264172
    return 100 / (liters * miles_per_km * gallons_per_liter)

def miles_gallon_to_liters_100km(miles):
    miles_per_km = 0.621371
    gallons_per_liter = 0.264172
    return 100 / (miles / miles_per_km / gallons_per_liter)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
def total_con_iva(cantidad, porcentaje_iva=21):
    return cantidad + cantidad * porcentaje_iva / 100

print(total_con_iva(100))  # 121
print(total_con_iva(100, 10))  # 110
import math

def area_circulo(radio):
    return math.pi * radio**2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

radio = 3
altura = 5
print("Área del círculo:", area_circulo(radio))
print("Volumen del cilindro:", volumen_cilindro(radio, altura))
def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

num_decimal = 25
num_binario = "11001"

print(f"{num_decimal} en binario: {decimal_a_binario(num_decimal)}")
print(f"{num_binario} en decimal: {binario_a_decimal(num_binario)}")
def es_vocal(letra):
    return letra.lower() in ['a', 'e', 'i', 'o', 'u']

def treu_vocals(paraula):
    return ''.join(letra for letra in paraula if not es_vocal(letra))

def treu_consonants(paraula):
    return ''.join(letra for letra in paraula if es_vocal(letra))

paraula_test = "hello"
print(f"Paraula original: {paraula_test}")
print(f"Sense vocals: {treu_vocals(paraula_test)}")
print(f"Només consonants: {treu_consonants(paraula_test)}")
