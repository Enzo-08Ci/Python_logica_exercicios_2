"""
11. Função com Argumentos Nomeados

Crie uma função:

criar_usuário ( nome , idade , cidade )
Escândalo de chamada:

create_user (
     nome = "Maria" ,
     idade = 22 ,
     cidade = "Rio de Janeiro" 
)
eu:

Nome: Maria
Idade: 22
Cidade: Rio de Janeiro
"""

def create_user(name, age, city):
    print(f'''
- Nome: {name}
- Idade: {age}
- Cidade: {city}
         ''')
    
create_user(
    age = 17,
    name = "Enzo",
    city = "Palmares",
)

print("\nArgumentos ordenados")
create_user("Maria", 22, "Rio de Janeiro")
