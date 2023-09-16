
def readInstances(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            valores_texto = conteudo.split(',')
            vetor = [float(valor.strip()) for valor in valores_texto]
            return vetor
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []