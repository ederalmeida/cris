import os
import PySimpleGUI as sg
import sys


def obter_relacao_xmls(caminho):
    # lista que irá receber todos os caminhos para os xmls na pasta que foi indicada
    enderecos_arquivos_xml = []

    # Lendo a pasta indicada
    listar_objetos_diretorio = os.listdir(caminho)
    
    # Percorrendo todos os objetos encontrados na pasta
    for objeto in listar_objetos_diretorio:
        
        # se o final do arquivo for .xml adiciona na lista
        if objeto[-4:] == '.xml':
            enderecos_arquivos_xml.append([caminho, objeto])

    # Se a lista não for vazia, retorna a lista
    if len(enderecos_arquivos_xml) != 0:
        return enderecos_arquivos_xml
    
    # Se for, informa
    #TODO melhorar para que não feche o robô. De preferência, voltar para a tela de interação que chamou a função
    else:
        sg.popup('Não existem arquivos .XML no diretório indicado', title='ERRO!')
        sys.exit()
