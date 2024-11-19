
def calcular_estatisticas(lista):
    if len(lista) == 0:
        return None, None, None  
    
    media = sum(lista) / len(lista)  
    maior = max(lista)  
    menor = min(lista)  
    
    return media, maior, menor


entrada = input("Digite uma lista de números, separados por espaço: ").split()


numeros = [int(num) for num in entrada]


media, maior, menor = calcular_estatisticas(numeros)


if media is not None:
    print(f"Média: {media}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
