import os
import csv
import PySimpleGUI as sg
from janelas import janela_avd_j1b1n_cadastro_fornecedor as jajcf

def cadastrar(CNPJ, CODIGO):

    #path_atual = os.getcwd()
    path_atual = os.path.abspath(os.path.dirname(__file__))

    with open(path_atual + '\\tabelas\\tabela_cnpj_fornecedorsap.csv', 'a', newline='') as arquivo:
 
        escrever = csv.writer(arquivo)
        escrever.writerow('\n')
        escrever.writerow([CNPJ + ';' + CODIGO])

    arquivo.close()

    sg.popup('Fornecedor cadastrado com sucesso.')

    jajcf.exibir()