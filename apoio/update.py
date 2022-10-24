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

    if os.path.isdir(os.sep.join([path, 'lib,' 'tmp'])):
        shutil.rmtree(os.sep.join([path, 'lib', 'tmp']))
    else:
        os.makedirs(os.sep.join([path, 'lib', 'tmp']))

    r = request.urlretrieve(url, file)

    extracao_zip = ZipFile(r[0], 'r')
    extracao_zip.extractall(os.sep.join([path, 'lib', 'tmp']))
    extracao_zip.close()
    
    update_files()
    
    # Excluindo o arquivo baixado
    shutil.rmtree(os.sep.join([path, 'tmp']))
    os.remove(path + '\\cris.zip')
    
def update_files():
    path = os.getcwd()
    tabela_aux_log = []
    # HAL = hash_arquivos_local
    with open(os.sep.join([path, 'lib', 'hash_arquivos_versao.csv']), 'r') as hal:
        csv_reader_hal = csv.reader(hal, delimiter=';')
        lista_hal = {linha[0]: linha[1] for linha in csv_reader_hal}
    hal.close()

    # HAR = hash_arquivos_remoto
    with open(os.sep.join([path, 'lib', 'tmp', 'lib', 'hash_arquivos_versao.csv']), 'r') as har:
        csv_reader_har = csv.reader(har, delimiter=';')
        lista_har = {linha[0]: linha[1] for linha in csv_reader_har}
    har.close()

    for key in lista_hal.keys():

        hash_hal = lista_hal.get(key)
        hash_har = lista_har.get(key)

        # se o caminho existir no local, mas não no remoto, apagar o local
        if hash_har == None:
            tabela_aux_log.append([hash_hal, hash_har, 'Excluir arquivo'])
        
        # se o caminho existir no local e no remoto, comparar hash
        if hash_hal == hash_har:
            tabela_aux_log.append([hash_hal, hash_har, 'Manter arquivo'])
        else:
            # se forem diferentes, copiar aquivo remoto para local
            tabela_aux_log.append([hash_hal, hash_har, 'Atualizar'])

    # se o caminho existir no remoto e não no local, copiar para local
    for key in lista_har.keys():
        hash_hal = lista_hal.get(key)
        if hash_hal == None:
            tabela_aux_log.append([hash_hal, hash_har, 'Transferir'])

        # Criando arquivo de logging
    arquivo_de_log = open(os.sep.join([path, 'lib', 'log de execução.txt']), 'w')
    
    for linha in tabela_aux_log:
        arquivo_de_log.writelines(linha[0] + ' - ' + linha[1] + ' - ' + linha[2] + '\n')
    arquivo_de_log.close()
        
            
        
        