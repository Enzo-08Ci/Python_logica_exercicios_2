"""
10. Calculadora com Funções

Crie como funções:

somar ( a , b )
 subtrair ( a , b )
 multiplicar ( a , b )
 dividir ( a , b )

Cada função deve retornar o resultado da operação.

Exemplo:

imprimir ( adicionar ( 10 , 5 ))
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("\n")

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(0, 5))