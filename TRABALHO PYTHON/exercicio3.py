
def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = int(input("Solicite o número N para gerar a sequência de Fibonacci: "))


if n <= 0:
    print(" Insira um número positivo.")
else:
    sequencia_fibonacci = fibonacci(n)
    print(f"Sequência de Fibonacci até o {n}º termo: {sequencia_fibonacci}")
