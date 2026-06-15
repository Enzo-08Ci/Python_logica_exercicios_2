
def recebe_dados(mensagem):
    return input(f'{mensagem} ')

print(recebe_dados("Qual seu nome?"))
print(int(recebe_dados("Qual sua idade?")))