"""
14. Função de Cálculo de IMC

Crie uma função:

calculate_bmi(weight, height)
Retorne:

weight / (height ** 2)
Exemplo:

bmi = calculate_bmi(80, 1.75)
"""

def calculate_bmi(weight, height):
    return weight / (height ** 2)

print('\n')

bmi = calculate_bmi(65, 1.74)

print(f'{bmi:.2f}')

if bmi < 18.5:
    print("Abaixo do peso")
elif bmi < 25:
    print("Peso normal")
elif bmi < 30:
    print("Sobrepeso")
elif bmi < 35:
    print("Obesidade Grau I")
elif bmi < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")