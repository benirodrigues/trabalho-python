
def tabela_multiplicacao(numero):
    print(f"Tabela de multiplicação do {numero}:")
    for i in range(1, 11):  
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


numero = int(input("Digite um número inteiro positivo: "))


if numero > 0:
    tabela_multiplicacao(numero)
else:
    print("Por favor, insira um número inteiro positivo.")
