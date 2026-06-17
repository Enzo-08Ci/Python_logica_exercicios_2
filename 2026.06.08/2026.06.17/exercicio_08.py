"""
8. Contador de Vogais

Peça uma palavra ao usuário.

Conte quanto vogais existem nela.

Exemplo:

Digite uma palavra: computador

Quantidade de vogais: 4
"""

palavra = input("Digite uma palavra:")

cont = 0

vogais = "aeiou"

for letra in palavra:
    if letra.lower() in vogais:
        cont += 1
   
print (cont)