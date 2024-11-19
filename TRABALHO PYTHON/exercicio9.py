
def contar_palavras_longas(lista):
    contador = 0  
    for palavra in lista:
        if len(palavra) > 5:  
            contador += 1  
    return contador

palavras = input("Digite uma lista de palavras, separadas por espaço: ").split()

quantidade_palavras_longas = contar_palavras_longas(palavras)

print(f"Quantidade de palavras com mais de 5 letras: {quantidade_palavras_longas}")
