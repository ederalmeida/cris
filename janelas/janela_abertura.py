# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #
import PySimpleGUI as sg
from imagens import imagens_base64 as imgs
from robos import fagll03, fbl3n, kob1
import sys

def inicializacao():

    sg.theme('LightGrey1')

    coluna_esquerda = [[sg.Text('CRIS', size=(10,1), justification='center', font=("Helvetica", 50))],
                       [sg.Text('Central de Robôs para Interação com o SAP', size=(20,2), justification='center', font=("Helvetica", 25))],
                       [sg.Text('')],
                       [sg.Button('FBL3N', size=(10,1), key='-FBL3N-'),
                        sg.Button('FAGLL03', size=(10,1), key='-FAGLL03-'),
                        sg.Button('KOB1', size=(10,1), key='-KOB1-')],
                       [sg.Button(' --- ', size=(10,1), key='-FBL5N_PA-'),
                        sg.Button(' --- ', size=(10,1), key='-FBL1N_PA-'),
                        sg.Button(' --- ', size=(10,1), key='-FS10N-')],
                       [sg.Text('')]
                      ]               

    coluna_direita = [[sg.Image(data=imgs.logo_x_base64, size=(150, 200), key='key1')]]

    layout = [[sg.Column(coluna_esquerda, element_justification='c'), sg.VSeperator(),sg.Column(coluna_direita, element_justification='c')]]

    janela= sg.Window('CRIS', layout, resizable=True)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
        if event == '-FBL3N-':
            janela.close()
            fbl3n.executa_robo()
        if event == '-FAGLL03-':
            janela.close()
            fagll03.executa_robo()
        if event == '-KOB1-':
            janela.close()
            kob1.executa_robo()
        else:
            continue
                
        janela.close()