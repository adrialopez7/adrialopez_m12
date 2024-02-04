c0 = int(input("Ingrese un número natural: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)

print(f"Se alcanzó el objetivo en {steps} pasos.")
# Paso 1
beatles = []

# Paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3
for _ in range(2):
    miembro = input("Ingrese un nuevo miembro de los Beatles: ")
    beatles.append(miembro)

# Paso 4
del beatles[3:5]

# Paso 5
beatles.insert(0, "Ringo Starr")

print(beatles)
numbers = []
while True:
    value = input("Ingrese un número (escriba 'fin' para finalizar): ")
    if value.lower() == "fin":
        break
    numbers.append(int(value))

# Ordenar la lista con el método de ordenamiento burbuja
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Lista ordenada:", numbers)
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("La lista con elementos únicos:")
print(unique_list)
ganadores = []
for _ in range(6):
    numero = int(input("Ingrese un número ganador: "))
    ganadores.append(numero)

ganadores.sort()
print("Números ganadores ordenados:", ganadores)
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    if nota < 5.0:
        repetir.append(asignatura)

print("Asignaturas para repetir:", repetir)
palabra = input("Ingrese una palabra: ").lower()

if palabra == palabra[::-1]:
    print("ES palíndromo")
else:
    print("NO es palíndromo")