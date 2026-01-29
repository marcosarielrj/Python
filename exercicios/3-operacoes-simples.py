#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Specifica a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")
# Realiza a operação com base na escolha do usuário
if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
