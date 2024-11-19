def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))


if e_primo(numero):
    print(f"{numero} o número digitado é primo.")
else:
    print(f"{numero} o número digitado não é um número primo.")

   