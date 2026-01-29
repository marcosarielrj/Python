def calcular_media (*numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

print(calcular_media(1,2,3,5,6))