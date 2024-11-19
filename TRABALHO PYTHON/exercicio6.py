import random

def contar_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return len(impares), impares


numeros_aleatorios = [random.randint(1, 50) for _ in range(20)]


quantidade_impares, lista_impares = contar_impares(numeros_aleatorios)


print(f"Números aleatórios: {numeros_aleatorios}")
print(f"Números ímpares: {lista_impares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
