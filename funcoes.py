
def Somar(valor1, valor2):
    Soma = int(valor1) + int(valor2)
    print(Soma)
    return Soma
def Subtracao(valor1, valor2):
    Subtracao = int(valor1) - int(valor2)
    print(Subtracao)
    return Subtracao

def Calculadora(valor1,valor2, funcao):
    if(funcao == "+"):
        Resultado = float(valor1) + float(valor2)
    elif(funcao == "-"):
        Resultado = float(valor1) - float(valor2)
    elif(funcao == "*"):
        Resultado = float(valor1) * float(valor2)
    elif(funcao == "/"):
        Resultado = float(valor1) / float(valor2)
    else:
        Resultado = "Funcao Nao cadastrada!"

    return Resultado