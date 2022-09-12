import PySimpleGUI as sg
from janelas import janela_avd_j1b1n_cadastro_fornecedor as jajcf
from janelas import janela_avd_j1b1n_parametrizacao as jajp
from janelas import janela_abertura as ja
from robos import avd_j1b1n

def exibir():
    sg.theme('Reddit')

    cabecalho = [[sg.Text('Robô para Escriturar AVDs com J1B1N', size=(34, 1), justification='center', font=("Helvetica", 22))],
                 [sg.Text('_'  * 100, size=(72, 1))]]

    linha2_coluna1 = [[sg.Text('Data de Contabilização', size=(20, 1), key='-TXT_DATA_CONTABILIZACAO-')],
                      [sg.InputText('', size=(19,1), key='-DATA_CONTABILIZACAO-', disabled=False, enable_events=True)]]

    linha2_coluna2 = [[sg.Text('Empresa')],
                      [sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')]]

    linha3 = [[sg.Text('Pasta com XMLs a serem importados')],
              [sg.InputText('', key='-PASTA-', size=(40, 1)), sg.FolderBrowse('procurar')]]

    coluna_esquerda = [[sg.Column(linha2_coluna1), sg.Column(linha2_coluna2)],
                       [sg.Column(linha3)]]

    coluna_direita = [[sg.Button('Parametrização', key='-PARAMETRIZACAO-', size=(20,1), enable_events=True)],
                      [sg.Button('Cadastrar Fornecedores', key='-CADASTRAR_FORNECEDOR-', size=(20,1), enable_events=True)],
                      [sg.Text('_'  * 26 ,justification='center', size=(23, 1))],
                      [sg.Button('Executar Robô ', key='-EXECUTAR_ROBO-', size=(20,1), enable_events=True)]]

    layout = [cabecalho,
              [sg.Column(coluna_esquerda), sg.VSeperator(), sg.Column(coluna_direita, element_justification='c')]]

    janela = sg.Window('CRIS - Central de Robôs para Interação com Sistemas', layout, element_justification='c', default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-CADASTRAR_FORNECEDOR-':
            janela.close()
            jajcf.exibir()

        if event == '-PARAMETRIZACAO-':
            janela.close()
            jajp.exibir()

        if event == '-EXECUTAR_ROBO-':
            if values['-DATA_CONTABILIZACAO-'] == '':
                sg.popup('Favor inserir data para contabilização das NFe', title='Erro')
            elif values['-COMPANY_CODE-'] == '':
                sg.popup('Favor indicar o Company Code', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde estão as NFe', title='Erro')
            else:
                janela.close()
                informacoes_avd_j1b1n = {'data_contabilizacao': values['-DATA_CONTABILIZACAO-'],
                             'company_code': values['-COMPANY_CODE-'],
                             'pasta': values['-PASTA-']}
                avd_j1b1n.executar_robo(informacoes_avd_j1b1n)
                break

