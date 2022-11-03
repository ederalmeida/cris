import PySimpleGUI as sg
import time
from apoio import update as up

sg.theme('Reddit')

def exibir():

    lista_eventos = ["Baixando nova versão", "Atualizando arquivos locais", "Finalizando Atualização", "Excluindo arquivos temporarios", "Atualização efetuada com sucesso!"]

    progressbar = [[sg.ProgressBar(len(lista_eventos), orientation='h', size=(27, 20), key='progressbar')]]

    outputwin = [[sg.Output(size=(40,10))]]

    layout = [[sg.Frame('Progresso',layout= progressbar)],
            [sg.Frame('Informações', layout = outputwin)],
            [sg.Submit('Iniciar Atualização')]]

    janela = sg.Window('Assistente de Atualização', layout)

    progress_bar = janela['progressbar']

#TODO Refatorar essa parte
    while True:
        event, values = janela.read(timeout=10)
        if event == 'Cancel'  or event is None:
            break
        elif event == 'Iniciar Atualização':
            janela['Iniciar Atualização'].update(disabled=True)
            i=0
            print(lista_eventos[i])
            up.download_arquivos()
            progress_bar.UpdateBar(i + 1)
            i += 1
            print(lista_eventos[i])
            up.atualizar_arquivos()
            i += 1
            print(lista_eventos[i])
            up.substituir_hash()
            i += 1
            print(lista_eventos[i])
            up.excluir_arquivos_tmp()
            i += 1
            print(lista_eventos[i])
            janela['Iniciar Atualização'].update(disabled=False)
            time.sleep(3)
            break