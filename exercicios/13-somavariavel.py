def soma_variavel (*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(soma_variavel(1,2,3,4,5))