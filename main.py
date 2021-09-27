# 1 - imports - bibliotecas
import pytest
# 2 - class - classe

# 3 - definitions - definicoes

def print_hello(name):
    print(f'Hello, {name}')

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Não há divisão por zero'

# Testes Unitarios

 # teste da funcao de somar
def test_somar_didatico():

    # 1 - Configura / Configure
    num1 = 2                    #imput
    num2 = 1                    #input
    resultado_esperado = 3      #output

    # 2 - Executa / Execute (Chamar a funcao a ser testada)
    resultado_obtido = somar(num1,num2)

    # 3 - Valida / Check
    assert resultado_obtido == resultado_esperado

@pytest.mark.parametrize('num1, num2, resultado',[
    # valores
    (5, 4, 9),    # teste 1
    (10, 10, 20), # teste 2
    (6, 9, 15),   # teste 3
])

def test_somar(num1, num2, resultado):
    assert somar(num1, num2) == resultado

def test_somar_numeros_negativo():
    assert somar(-1000,-2000) == -3000

def test_subtrair():
    assert subtrair(2,1) == 1

def test_multiplicar():
    assert multiplicar(2,1) == 2

if __name__ == '__main__':
    print_hello('Bea')

    # soma entre 2 numeros
    resultado = somar(1, 2)
    print(f'O resultado da soma: {resultado}')

    # subtracao entre 2 numeros
    resultado = subtrair(5, 4)
    print(f'O resultado da subtração: {resultado}')

    # multiplicacao entre 2 numeros
    resultado = multiplicar(5, 4)
    print(f'O resultado da multiplicação: {resultado}')

    # divisao entre 2 numeros
    resultado = dividir(9, 3)
    print(f'O resultado da divisão: {resultado}')
