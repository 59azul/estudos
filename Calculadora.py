def calculadora():
    num1 = input("Digite um numero: ")
    if not eh_int(num1):
        return "Não é um número"
    num1 = int(num1)
    operacao = input("Digite a operação: ")
    if not op_valida(operacao):
        return "Operação inválida"
    num2 = input("Digite o segundo numero: ")
    if not eh_int(num2):
        return "Não é um número"
    num2 = int(num2)
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return float(num1) / float(num2)
    return "Erro"


def eh_int(entrada):
    try:
        val = int(entrada)
        return True
    except ValueError:
        return False


def op_valida(entrada):
    if entrada == "+" or entrada == "-" or entrada == "*" or entrada == "/":
        return True
    else:
        return False


print(calculadora())
