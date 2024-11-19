
def fatorial(numero):
    resultado = 1  
    for i in range(1, numero + 1):  
        resultado *= i  
    return resultado


numero = int(input("Digite um número inteiro: "))


if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    
    resultado = fatorial(numero)
    
    print(f"O fatorial de {numero} é: {resultado}")
