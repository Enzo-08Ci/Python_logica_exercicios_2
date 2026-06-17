"""
4. Verificador de numero

Solicite um numero ao usuário.

Informe se ele é:

Positivo
Negativo
Zero
"""

numero = int(input("Digite um numero:"))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("0")

if numero % 2 == 0:
    print("Par")
else: 
    print("Ímpar")

