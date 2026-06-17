"""
9. Função de Saudação

Crie uma função chamada:

saudar ()
Ela deve receber um nome como argumento e exibir:

Olá, Maria!
Exemplo de uso:

cumprimentar ( "Maria" )
"""

def greet(name):
    print(f"Olá, {name}!")

print("\n")
greet("Maria")


def greet2(name):
    return f"Olá, {name}!"

greet_out = greet2("Maria")
print(greet2("Maria"))