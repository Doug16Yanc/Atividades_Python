import csv

def carrega_banco(arquivo):
    with open(arquivo, mode='r', newline='', encoding='utf-8') as f:
        conteudo = csv.DictReader(f, delimiter=';')
        clientes = list(conteudo)

        return clientes

def calcula_media_idade(arquivo):
    conteudo = carrega_banco(arquivo)
    soma = 0
    for item in conteudo:
        soma += int(item['idade'])
    return soma / len(conteudo)

def calcula_media_renda(arquivo):
    conteudo = carrega_banco(arquivo)
    soma = 0
    for item in conteudo:
        soma += float(item['renda'])
    return soma / len(conteudo)

def main():

    print("Médias conforme cálculo : ")

    print(f"Media de idade: {calcula_media_idade('clientes.csv'):.2f}")
    print(f"Media de renda: {calcula_media_renda('clientes.csv'):.2f}")

if __name__=="__main__":
    main()
