import json

def carrega_banco():
    f = open("clientes.txt", "r")
    conteudo = f.read()
    conteudoJson = json.loads(conteudo)
    f.close()  
    return conteudoJson

def calcula_media_idade():
    conteudo = carrega_banco()
    soma = 0
    for item in conteudo:
        soma += item['idade']
    return soma / len(conteudo)

def calcula_media_renda():
    conteudo = carrega_banco()
    soma = 0
    for item in conteudo:
        soma += item['renda']
    return soma / len(conteudo)

print(f"Media de Idade: {calcula_media_idade():.2f}")
print(f"Media de Renda: {calcula_media_renda():.2f}")
