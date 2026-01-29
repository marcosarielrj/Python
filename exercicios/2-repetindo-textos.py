# solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicita ao usuário que insira uma string
texto = input("Por favor, insira uma string: ")
# Solicita ao usuário que insira um número inteiro
vezes = int(input("Por favor, insira um número inteiro: "))
# Repete a string o número de vezes informado
texto_repetido = (texto + " ") * vezes
# Exibe o resultado
print("String repetida:", texto_repetido)
# Fim do código
