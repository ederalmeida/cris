import PySimpleGUI as sg
#from janelas import janela_abertura as ja

def exibir():
    sg.theme('Reddit')

    cabecalho = [[sg.Text('Relação de Pagamento \npor fornecedor', size=(20, 2), justification='center', font=("Helvetica", 22))],
                [sg.Text('_'  * 70, size=(48, 1))]]

    linha1_coluna1 = [[sg.Text('Empresa', size=(8, 1)),
                       sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')],
                       [sg.Text(' ', font=("Helvetica", 2))],
                      [sg.Text('Fornecedor', size=(8, 1), key='-TXT_FORNECEDOR-'), sg.InputText('', size=(16,1), key='-FORNECEDOR-', enable_events=True)]]

    linha1_coluna2 = [[sg.Frame('Data Contabilização',
               [[sg.Text('De', size=(5, 1), key='-DATA_CONT_DE_TEXTO-'),
                sg.InputText('', size=(13,1), key='-DATA_CONT_DE-', enable_events=True)],
               [sg.Text('Até', size=(5, 1), key='-DATA_CONT_ATE_TEXTO-'),
                sg.InputText('', size=(13,1), key='-DATA_CONT_ATE-', enable_events=True)]])]]

    linha2 = [sg.Text('_'  * 70, size=(48, 1))]

    linha3_coluna1 = [[sg.Text('Pasta onde serão salvos os relatórios', size=(27, 1))],
                      [sg.InputText('', key='-PASTA-', size=(25, 1)), sg.FolderBrowse('procurar')]]

    linha3_coluna2 = [[sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]]

    layout = [cabecalho,
             [sg.Column(linha1_coluna1), sg.Column(linha1_coluna2)],
              linha2,
             [sg.Column(linha3_coluna1), sg.VSeperator(), sg.Column(linha3_coluna2, element_justification='rigth')]]

    janela = sg.Window('CRIS - Central de Robôs para Interação com Sistemas', layout, grab_anywhere=False)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
             janela.close()
             ja.exibir()

        if event == '-EXECUTAR_ROBO-':
            if values['-COMPANY_CODE-'] == '':
                sg.popup('Favor inserir um Company Code!', title='Erro')
            elif values['-FORNECEDOR-'] == '':
                sg.popup('Favor inserir cód. SAP para o fornecedor', title='Erro')
            elif values['-DATA_CONT_DE-'] == '':
                sg.popup('Favor inserir data de início', title='Erro')
            elif values['-DATA_CONT_ATE-'] == '':
                sg.popup('Favor inserir data de fim', title='Erro')
            else:
                pass

exibir()