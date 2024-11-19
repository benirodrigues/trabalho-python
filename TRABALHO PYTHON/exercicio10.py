
def soma_dos_digitos(numero):
    
    return sum(int(digito) for digito in str(abs(numero)))  

numero = int(input("Digite um número inteiro: "))

resultado = soma_dos_digitos(numero)


print(f"A soma dos dígitos do número {numero} é: {resultado}")
