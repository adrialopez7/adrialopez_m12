import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("¡Listos o no, ahí voy!")
while True:
    palabra = input("Ingresa una palabra: ")
    if palabra.lower() == "chupacabra":
        print("¡Has dejado el bucle con éxito!")
        break
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)
cantidad_invertir = float(input("Cantidad a invertir: "))
interes_anual = float(input("Interés anual (%): "))
num_anios = int(input("Número de años: "))

for i in range(1, num_anios + 1):
    cantidad_invertir *= 1 + (interes_anual / 100)
    print(f"Año {i}: {round(cantidad_invertir, 2)}")
altura = int(input("Ingrese la altura del triángulo: "))

for i in range(1, altura + 1):
    print("*" * i)
num = int(input("Ingrese un número: "))

es_primo = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        es_primo = False
        break

if es_primo and num > 1:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
palabra = input("Ingrese una palabra: ")

for letra in reversed(palabra):
    print(letra)
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0
for caracter in frase:
    if caracter.lower() == letra.lower():
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")
blocks = int(input("Ingresa el número de bloques: "))
height = 0
total_blocks = 0

while total_blocks <= blocks:
    height += 1
    total_blocks += height

print("La altura de la pirámide es:", height - 1)
