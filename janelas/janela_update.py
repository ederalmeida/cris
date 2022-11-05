import PySimpleGUI as sg
import time
from apoio import update as up

sg.theme('Reddit')

def exibir():

    lista_eventos = ["Iniciando Atualização", "Baixando nova versão", "Atualizando arquivos locais", "Finalizando Atualização", "Excluindo arquivos temporarios", "Atualização efetuada com sucesso!"]

    progressbar = [[sg.ProgressBar(len(lista_eventos), orientation='h', size=(27, 20), key='progressbar')]]

    outputwin = [[sg.Output(size=(40,10))]]

    layout = [[sg.Frame('Progresso',layout= progressbar)],
            [sg.Frame('Informações', layout = outputwin)]]

    janela = sg.Window('Assistente de Atualização', layout)

    progress_bar = janela['progressbar']

#TODO Refatorar essa parte
    while True:
        event, values = janela.read(timeout=10)
        i=0
        print(lista_eventos[i])
        time.sleep(3)
        progress_bar.UpdateBar(i + 1)
        i += 1
        print(lista_eventos[i])
        time.sleep(3)
        up.download_arquivos()
        progress_bar.UpdateBar(i + 1)
        i += 1
        print(lista_eventos[i])
        up.atualizar_arquivos()
        progress_bar.UpdateBar(i + 1)
        i += 1
        print(lista_eventos[i])
        up.substituir_hash()
        progress_bar.UpdateBar(i + 1)
        i += 1
        print(lista_eventos[i])
        up.excluir_arquivos_tmp()
        progress_bar.UpdateBar(i + 1)
        i += 1
        print(lista_eventos[i])
        progress_bar.UpdateBar(i + 1)
        time.sleep(3)
        janela.close()
        break