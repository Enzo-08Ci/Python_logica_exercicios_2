"""
12. Cadastro de Produtos

Crie uma coleção contendo dicionários de produtos.

Exemplo:

produtos  = [ 
    { "nome" : "Mouse" ,
         "preço" : 50 
    }, 
    { "nome" : "Teclado" ,
         "preço" : 120 
    } 
]
        
        
Exiba:

Mouse - R$ 50
Keyboard - R$ 120
"""

produtos  = [ 
    { "nome" : "Mouse" ,
         "preço" : 50 
    }, 
    { "nome" : "Teclado" ,
         "preço" : 120 
    } 
]

print("\n")

total = 0

for produto in produtos:
    total += produto['preço']
    print(f"{produto['nome']} - R${produto['preço']}")

print(f"\nTotal de R${total}")