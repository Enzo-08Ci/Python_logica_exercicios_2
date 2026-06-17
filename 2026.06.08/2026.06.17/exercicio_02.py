"""
2. Calculadora de Média

Crie um programa que receba três notas e calcule a média.

Exemplo:

Nota 1: 8
Nota 2: 7
Nota 3: 9

Média: 8.0

Média >= 7 → Aprovado
Média >= 5 → Aprovado
Senão      → Reprovado

"""

nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.1f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Aprovado")
else:
    print("Reprovado")