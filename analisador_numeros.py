quantidade = int(input("Quantos números você vai digitar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero % 2 == 0:
        print(numero, "é par")
        pares += 1
    else:
        print(numero, "é ímpar")
        impares += 1

print("\nTotal de números pares:", pares)
print("Total de números ímpares:", impares)
