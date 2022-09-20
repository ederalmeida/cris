import os
import csv

def obter(caminho_arquivo):

    path_atual = os.path.abspath(os.path.dirname(__file__))
    dados_csv = {}

    with open(path_atual + caminho_arquivo, encoding="utf8") as arquivo:
 
        tabela = csv.reader(arquivo, delimiter=';')

        for linha in tabela:
            dados_csv[linha[0]] = linha[1]

    arquivo.close()
    
    return dados_csv 
