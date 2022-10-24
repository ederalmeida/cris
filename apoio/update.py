import urllib3
import PySimpleGUI as sg
import os
import shutil
import csv
from urllib import request
from zipfile import ZipFile
from apoio import versao_local as vl

def check_update():
    versao_local = vl.v
    url_update = 'https://robocris.000webhostapp.com/cris/version.txt'
    
    http = urllib3.PoolManager()
    
    try:
        r = http.request('GET', url_update, timeout=5.0)
        versao_remota = r.data.decode('utf-8')
        
        if versao_local != versao_remota:
            atualizar = sg.popup_yes_no('Existe uma nova versão para a CRIS!\n Você gostaria de atualizar?',
                                        title = 'Atualização')
            
    except:
        atualizar = 'No'
        
    if atualizar == 'Yes':
        update()

def update():
    url = 'https://robocris.000webhostapp.com/cris/cris.zip'
    file = 'cris.zip'

    path = os.getcwd()

    if os.path.isdir(os.sep.join([path, 'tmp'])):
        shutil.rmtree(os.sep.join([path, 'tmp']))
    else:
        os.makedirs(os.sep.join([path, 'tmp']))

    r = request.urlretrieve(url, file)

    extracao_zip = ZipFile(r[0], 'r')
    extracao_zip.extractall(os.sep.join([path, 'tmp']))
    extracao_zip.close()
    
    update_files()
    
    # Excluindo o arquivo baixado
    #shutil.rmtree(os.sep.join([path, 'tmp']))
    #os.remove(path + '\\cris.zip')
    
def update_files():
    hash_arquivos_local = {}
    hash_arquivos_remoto = {}
    
    with open('', 'r') as hal:
        entradas = csv.reader(hal, delimiter=';')
        for linha in entradas:
            hash_arquivos_local[linha[0]] = linha[1]
    hal.close()
    
    with open('', 'r') as har:
        entradas = csv.reader(har, delimiter=';')
        for linha in entradas:
            hash_arquivos_remoto[linha[0] = linha[1]]
    har.close()
    
    # se o caminho existir no local, mas não no remoto, apagar o local
    # se o caminho existir no local e no remoto, comparar hash
        # se os hash forem iguais, fazer nada
        # se forem diferentes, copiar aquivo remoto para local
    # se o caminho existir no remoto e não no local, copiar para local
    if 
        
    
    