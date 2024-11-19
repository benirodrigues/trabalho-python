
def filtrar_multiplos(lista):
    return [num for num in lista if num % 3 == 0 or num % 5 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 21, 25, 30]


multiplos = filtrar_multiplos(numeros)


print(f"Números múltiplos de 3 ou 5: {multiplos}")
