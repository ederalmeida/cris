import PySimpleGUI as sg
from imagens import imagens_base64 as imgs
from janelas import janela_avd_j1b1n, janela_fagll03, janela_fbl1n, janela_fbl3n, janela_fbl5n, janela_kob1,\
     janela_inadimplencia_amse, janela_zwf100
from apoio import versao_atual as versao
import sys

def exibir():

    sg.theme('Reddit')

    coluna_esquerda = [[sg.Text('CRIS', size=(10,1), justification='center', font=("Helvetica", 50))],
                       [sg.Text('Central de Robôs para Interação com Sistemas', size=(20,2), justification='center', font=("Helvetica", 20))],
                       [sg.Text('')],
                       [sg.Frame('CONTÁBIL/FINANCEIRO',
                        [[sg.Button('FBL3N', size=(10,1), key='-FBL3N-'),
                          sg.Button('FBL1N', size=(10,1), key='-FBL1N-'),
                          sg.Button('FBL5N', size=(10,1), key='-FBL5N-'),
                          sg.Button('FAGLL03', size=(10,1), key='-FAGLL03-')],
                         [sg.Button('KOB1', size=(10,1), key='-KOB1-'),
                          sg.Button('AVD J1B1N', size=(10,1), key='-AVDJ1B1N-'),
                          ]])],
                       [sg.Text('')],
                       [sg.Frame('TESOURARIA',
                        [[sg.Button('ONS AMSE', size=(10,1), key='-INADIMPLENCIA_AMSE-'),
                         sg.Button('ZWF100', size=(10,1), key='-ZWF100-')]], size=(435, 62))],
                       [sg.Text('')],
                       [sg.Frame('TRIBUTARIO',
                        [[sg.Button('ZMD_DIRF', size=(10,1), key='-ZMD_DIRF-')]], size=(435, 62))],
                       [sg.Text('')],
                       [sg.Text(versao.v, size=(10,1), justification='center', font=("Helvetica", 7))]
                      ]               

    coluna_direita = [[sg.Image(data=imgs.logo_x_base64, size=(150, 170), key='key1')]]

    layout = [[sg.Column(coluna_esquerda, element_justification='c'), sg.VSeperator(),sg.Column(coluna_direita, element_justification='c')]]

    janela= sg.Window('CRIS', layout, resizable=True)

    while True:

        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
            
        if event == '-FBL3N-':
            janela.close()
            janela_fbl3n.exibir()

        if event == '-FBL1N-':
            janela.close()
            janela_fbl1n.exibir()

        if event == '-FBL5N-':
            janela.close()
            janela_fbl5n.exibir() 

        if event == '-FAGLL03-':
            janela.close()
            janela_fagll03.exibir()

        if event == '-KOB1-':
            janela.close()
            janela_kob1.exibir()
            
        if event == '-AVDJ1B1N-':
            janela.close()
            janela_avd_j1b1n.exibir()

        if event == '-INADIMPLENCIA_AMSE-':
            janela.close()
            janela_inadimplencia_amse.exibir()

        if event == '-ZWF100-':
            janela.close()
            janela_zwf100.exibir()

        else:
            continue