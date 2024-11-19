
numeros = []
while True:
    entrada = input("Solicite um número (ou 'parar' para encerrar): ")
    
    if entrada.lower() == "parar":
        break  
    
    try:
        
        numero = int(entrada)
        numeros.append(numero)  
    except ValueError:
        
        print(" Digite um número ou 'parar'.")

print(f"Números digitados: {numeros}")


soma = sum(numeros)
print(f"Soma dos números digitados: {soma}")