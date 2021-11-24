import PySimpleGUI as sg
import sys

def exibir():
    sg.theme('LightGrey1')

    cabecalho = [[sg.Text('Robô para Escriturar AVDs com J1B1N', size=(34, 1), justification='center', font=("Helvetica", 22))],
                 [sg.Text('_'  * 100, size=(72, 1))]]

    linha2_coluna1 = [[sg.Text('Data de Contabilização', size=(20, 1), key='-TXT_DATA_CONTABILIZACAO-')],
                      [sg.InputText('', size=(19,1), key='-DATA_CONTABILIZACAO-', disabled=False, enable_events=True)]]

    linha2_coluna2 = [[sg.Text('Empresa')],
                      [sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')]]

    linha3 = [[sg.Text('Pasta com XMLs a serem importados')],
              [sg.InputText('', key='-PASTA-', size=(40, 1)), sg.FolderBrowse('procurar')]]
    
    
    linha6 = [[sg.Text('')],
              [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]]

    coluna_esquerda = [[sg.Column(linha2_coluna1), sg.Column(linha2_coluna2)],
                       [sg.Column(linha3)],
                       [sg.Column(linha6)]]

    coluna_direita = [[sg.Text('teste')]]

    layout = [cabecalho,
              [sg.Column(coluna_esquerda), sg.Column(coluna_direita)]]

    janela = sg.Window('CRIS - Central de Robôs para Interação com Sistemas', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()

        if event == '-EXECUTAR_ROBO-':
            break

    janela.close()

    return values['-DATA_CONTABILIZACAO-'], values['-COMPANY_CODE-'], values['-PASTA-']