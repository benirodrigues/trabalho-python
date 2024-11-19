
def ordenar_lista(lista):
    
    for i in range(len(lista)):
        
        menor_indice = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
    
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista


numeros = input("Digite uma lista de números, separados por espaço: ").split()


numeros = [int(num) for num in numeros]

lista_ordenada = ordenar_lista(numeros)

print(f"Lista em ordem crescente: {lista_ordenada}")
