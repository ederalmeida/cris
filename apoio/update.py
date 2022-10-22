import urllib3
import PySimpleGUI as sg
import os
import shutil
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
    shutil.rmtree(os.sep.join([path, 'tmp']))
    os.remove(path + '\\cris.zip')
    
def update_files():
    pass
    
    