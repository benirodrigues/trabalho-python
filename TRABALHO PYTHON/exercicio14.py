
def contar_vogais_consoantes(lista):
    vogais = 'aeiouAEIOU'  
    contador_vogais = 0
    contador_consoantes = 0
    
    for char in lista:
        if char.isalpha():  
            if char in vogais:
                contador_vogais += 1  
            else:
                contador_consoantes += 1  

    return contador_vogais, contador_consoantes

entrada = input("Digite uma lista de caracteres, separados por espaço: ").split()

quantidade_vogais, quantidade_consoantes = contar_vogais_consoantes(entrada)

print(f"Quantidade de vogais: {quantidade_vogais}")
print(f"Quantidade de consoantes: {quantidade_consoantes}")
