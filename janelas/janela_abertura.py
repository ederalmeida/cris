# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #
import PySimpleGUI as sg
from imagens import imagens_base64 as imgs
from robos import fagll03, fbl3n, kob1
from apoio import versao_atual as versao
import sys

def inicializacao():

    sg.theme('LightGrey1')

    coluna_esquerda = [[sg.Text('CRIS', size=(10,1), justification='center', font=("Helvetica", 50))],
                       [sg.Text('Central de Robôs para Interação com Sistemas', size=(20,2), justification='center', font=("Helvetica", 20))],
                       [sg.Text('')],
                       [sg.Frame('CONTÁBIL/FINANCEIRO',
                        [[sg.Button('FBL3N', size=(10,1), key='-FBL3N-'),
                         sg.Button('FAGLL03', size=(10,1), key='-FAGLL03-'),
                         sg.Button('KOB1', size=(10,1), key='-KOB1-')]])],
                       [sg.Text('')],
                       [sg.Frame('AMBIENTAL',
                        [[sg.Button('IBMA', size=(10,1), key='-IBAMA-'),
                         sg.Button('INEA/RJ', size=(10,1), key='-INEARJ-'),
                         sg.Button('CETESB/SP', size=(10,1), key='-CETESB/SP-')],
                         [sg.Button('SEMAD/GO', size=(10,1), key='-SEMADGO-'),
                         sg.Button('SEMAD/MG', size=(10,1), key='-SEMADMG-'),
                         sg.Button('IEMA/ES', size=(10,1), key='-IEMAES-')]])],
                       [sg.Text('')],
                       [sg.Frame('REGULATÓRIO',
                        [[sg.Button('BDIT', size=(10,1), key='-BDIT-'),
                         sg.Button('SGT', size=(10,1), key='-SGT-'),
                         sg.Button('BMP', size=(10,1), key='-BMP-')],
                         [sg.Button('SIASE', size=(10,1), key='-SIASE-'),
                         sg.Button('SINtegre', size=(10,1), key='-SINTEGRE-'),
                         sg.Button('Dutonet', size=(10,1), key='-DUTONET-')]])],
                       [sg.Text('')],
                       [sg.Text(versao.v, size=(10,1), justification='center', font=("Helvetica", 7))]
                      ]               

    coluna_direita = [[sg.Image(data=imgs.logo_x_base64, size=(150, 200), key='key1')]]

    layout = [[sg.Column(coluna_esquerda, element_justification='c'), sg.VSeperator(),sg.Column(coluna_direita, element_justification='c')]]

    janela= sg.Window('CRIS', layout, resizable=True)

    while True:

        robos_nao_desenvolvidos = ['-IBAMA-', '-INEARJ-', '-CETESB/SP-', '-SEMADGO-', '-SEMADMG-', '-IEMAES-',
                                   '-BDIT-', '-SGT-', '-BMP-', '-SIASE-', '-SINTEGRE-', '-DUTONET-']

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
        if event in robos_nao_desenvolvidos:
            sg.popup('Sem autorização para acessar esse robô', title='Aviso')
            continue
        else:
            continue
                
        janela.close()