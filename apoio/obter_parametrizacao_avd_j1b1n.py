import os
import csv

def obter():

    #path_atual = os.getcwd()
    path_atual = os.path.abspath(os.path.dirname(__file__))

    parametros = {}

    with open(path_atual + '\\tabelas\\parametrizacao_avd_j1b1n.csv') as arquivo:

        tabela = csv.reader(arquivo, delimiter=';')

        for linha in tabela:
            parametros[linha[0]] = linha[1]

    arquivo.close()

    return parametros