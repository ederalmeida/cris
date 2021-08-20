# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #
import PySimpleGUI as sg
from imagens import logo as imgs
from robo import kob1
import sys

def inicializacao():

    #sg.theme('DarkGrey14')

    coluna_esquerda = [[sg.Text('CRIS', size=(25,1), justification='center', font=("Helvetica", 25))],
                       [sg.Text('Central de Robôs para Interação com o SAP', size=(30,2), justification='center', font=("Helvetica", 15))],
                       [sg.Text('')],
                       [sg.Button('KOB1', size=(10,1), button_color='black on white', key='-KOB1-'),
                        sg.Button('FBL3N', size=(10,1), button_color='black on white', key='-FAGLL03-'),
                        sg.Button('KS03', size=(10,1), button_color='black on white', key='-FC10N-')],
                       [sg.Button('FC10N', size=(10,1), button_color='black on white', key='-FBL5N_PA-'),
                        sg.Button('FS10N', size=(10,1), button_color='black on white', key='-FBL1N_PA-'),
                        sg.Button('KOC4', size=(10,1), button_color='black on white', key='-FS10N-')],
                       [sg.Text('')]
                      ]               

    coluna_direita = [[sg.Image(data=imgs.logo_x_base64, size=(150, 200), key='key1')]]

    layout = [[sg.Column(coluna_esquerda, element_justification='c'), sg.VSeperator(),sg.Column(coluna_direita, element_justification='c')]]

    janela= sg.Window('CRIS', layout, resizable=True)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
        if event == '-KOB1-':
            janela.close()
            kob1.executa_robo()
        else:
            continue
                
        janela.close()