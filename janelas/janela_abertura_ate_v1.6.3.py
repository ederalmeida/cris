import PySimpleGUI as sg
from imagens import imagens_base64 as imgs
from janelas import janela_avd_j1b1n, janela_fagll03, janela_fbl1n, janela_fbl3n, janela_fbl5n, janela_kob1, janela_inadimplencia_amse
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
                          sg.Button('ONS AMSE', size=(10,1), key='-INADIMPLENCIA_AMSE-')]])],
                       [sg.Text('')],
                       [sg.Frame('AMBIENTAL',
                        [[sg.Button('IBMA', size=(10,1), key='-IBAMA-'),
                         sg.Button('INEA/RJ', size=(10,1), key='-INEARJ-'),
                         sg.Button('CETESB/SP', size=(10,1), key='-CETESB/SP-'),
                         sg.Button('SEMAD/GO', size=(10,1), key='-SEMADGO-')],
                         [sg.Button('SEMAD/MG', size=(10,1), key='-SEMADMG-'),
                         sg.Button('IEMA/ES', size=(10,1), key='-IEMAES-')]])],
                       [sg.Text('')],
                       [sg.Frame('REGULATÓRIO',
                        [[sg.Button('BDIT', size=(10,1), key='-BDIT-'),
                         sg.Button('SGT', size=(10,1), key='-SGT-'),
                         sg.Button('BMP', size=(10,1), key='-BMP-'),
                         sg.Button('SIASE', size=(10,1), key='-SIASE-')],
                         [sg.Button('SINtegre', size=(10,1), key='-SINTEGRE-'),
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

        if event in robos_nao_desenvolvidos:
            sg.popup('Sem autorização para acessar esse robô', title='Aviso')
            continue
        else:
            continue