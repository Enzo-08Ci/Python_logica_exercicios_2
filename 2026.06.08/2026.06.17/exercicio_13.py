"""
13. Sistema de login simplificado

Crie duas:

nome de usuário 
senha
Verificar:

Usuário: admin
Senha: 1234
Se ambos estiverem corretos:

Acesso permitido
Caso contrário:

Acesso negado
"""

datauser = [
    "admin", "1234"
]

autorized = False

triers = 1
while True:
    print("\n------------------------------")
    username = input("Usuário: ")
    password = input("Senha: ")
    if username == datauser[0] and password == datauser[1]:
        autorized = True
        break

    if triers == 3:
        print("Tentativas esgotadas")
        break

    triers += 1
    print("Dados inválidos. Tente novamente.")


if autorized:
    print("Acesso permitido")
else:    
    print("Acesso negado")
