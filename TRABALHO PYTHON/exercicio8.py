
def segundo_maior(lista):
    if len(lista) < 2:
        return None 
    
    
    lista_unica = list(set(lista))
    
    if len(lista_unica) < 2:
        return None  
    

    lista_unica.remove(max(lista_unica))
    

    return max(lista_unica)


numeros = input("Digite uma lista de números, separados por espaço: ").split()


numeros = [int(num) for num in numeros]


segundo_maior_numero = segundo_maior(numeros)


if segundo_maior_numero is not None:
    print(f"O segundo maior número é: {segundo_maior_numero}")
else:
    print("A lista não contém números suficientes ou diferentes para determinar o segundo maior.")
