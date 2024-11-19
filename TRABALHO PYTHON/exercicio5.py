
def contar_letras(frase):

    frase = frase.replace(" ", "").lower()
    
   
    contagem = {}
    
    
    for letra in frase:
        if letra.isalpha():  
            contagem[letra] = contagem.get(letra, 0) + 1
    
    return contagem


frase = input("Digite uma frase: ")


contagem_letras = contar_letras(frase)


for letra, contagem in contagem_letras.items():
    print(f"Letra '{letra}' aparece {contagem} vez(es).")
