import os
import csv

def obter():

    path_atual = os.path.abspath(os.path.dirname(__file__))

    parametros = {}

    with open(path_atual + '\\tabelas\\parametrizacao_avd_j1b1n.csv', encoding='ISO-8859-1') as arquivo:

        tabela = csv.reader(arquivo, delimiter=';')

        for linha in tabela:
            parametros[linha[0]] = linha[1]

    arquivo.close()

    return parametros

def salvar(parametros_salvos):
    
    path_atual = os.path.abspath(os.path.dirname(__file__))

    csv.register_dialect("pv", delimiter=";")

    with open(path_atual + '\\tabelas\\parametrizacao_avd_j1b1n.csv', 'w', encoding='ISO-8859-1', newline='') as arquivo:
        escrever = csv.writer(arquivo, dialect='pv')
        for parametro, valor in parametros_salvos.items():
            escrever.writerow((parametro, valor))

    arquivo.close()
