import os
import csv

def obter():

    path_atual = os.getcwd()

    relacao_fornecedores = {}

    with open(path_atual + '\\tabelas\\tabela_cnpj_fornecedorsap.csv') as arquivo:

        tabela = csv.reader(arquivo, delimiter=';')

        for linha in tabela:
            relacao_fornecedores[linha[0]] = linha[1]

    arquivo.close()

    return relacao_fornecedores