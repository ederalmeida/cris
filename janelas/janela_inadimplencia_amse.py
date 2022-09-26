import PySimpleGUI as sg
from janelas import janela_abertura as ja
from robos import inadimplencia_amse

def exibir():
    sg.theme('Reddit')

    cabecalho = [[sg.Text('Inadimplência ONS - AMSE', size=(25, 1), justification='center', font=("Helvetica", 22))],
                 [sg.Text('_'  * 110, size=(56, 1))]]

    linha1 = [[sg.Frame('Arquivo XLSX',
                       [[sg.InputText('', key='-ARQUIVO_INADIMPLENCIA-', size=(24, 1)), sg.FileBrowse('procurar'),
                        sg.Text(' '),
                        sg.Checkbox('Ignorar primeira linha?', key='-IGNORAR_PRIMEIRA_LINHA-', default=True)]],
                        size=(450, 60))]]

    linha2 = [sg.Text(' ', font=("Helvetica", 2))]

    linha3_coluna1 = [[sg.Frame('Cadastros',
                       [[sg.Button('Cadastrar Concessões', key='-CADASTRAR_CONCESSOES-', size=(21,1), enable_events=True)],
                        [sg.Text(' ', size=(21,1), font=("Helvetica", 2))],
                        [sg.Button('Cadastrar Clientes', key='-CADASTRAR_CLIENTES-', size=(21,1), enable_events=True)],
                        [sg.Text(' ', size=(21,1), font=("Helvetica", 2))]],
                        size=(215, 107), element_justification="center")]]

    linha3_coluna2 = [[sg.Frame('Dados Usuário',
                      [[sg.Text('Login', size=(5, 1), key='-TEXTO_LOGIN_ONS_AMSE-'),
                        sg.InputText('', size=(15,1), key='-LOGIN_ONS_AMSE-', disabled=False, enable_events=True)],
                       [sg.Text('Senha', size=(5,1), key='-TEXTO_SENHA_ONS_AMSE-'),
                        sg.InputText('', size=(15,1), key='-SENHA_ONS_AMSE-', password_char='*')]],size=(215, 107))]]
    
    linha4_coluna1 = [[sg.Text(' ' * 63)]]
    linha4_coluna2 = [[sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', size=(21, 1), enable_events=True)]]
    
    #linha5 = [sg.Text('')]

    layout = [cabecalho,
             [sg.Column(linha1)],
              linha2,
             [sg.Column(linha3_coluna1), sg.Column(linha3_coluna2)],
             [sg.Column(linha4_coluna1), sg.Column(linha4_coluna2, element_justification="right", vertical_alignment="bottom")]
             ]

    janela = sg.Window('Robô para registrar Inadimplência no sistema ONS - AMSE', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-CADASTRAR_CONCESSOES-':
            janela.close()

        if event == '-CADASTRAR_CLIENTES-':
            janela.close()

        if event == '-EXECUTAR_ROBO-':
            if values['-ARQUIVO_INADIMPLENCIA-'] == '':
                sg.popup('Favor indicar o arquivo que contenham a relação de clientes inadimplentes', title='Erro')

            if values['-LOGIN_ONS_AMSE-'] == '':
                sg.popup('Favor informar o login do sistema AMSE')

            if values['-SENHA_ONS_AMSE-'] == '':
                sg.popup('Favor informar a senha do sistema AMSE')

            else:
                informacoes_amse = {
                    'arquivo_inadimplencia': values['-ARQUIVO_INADIMPLENCIA-'],
                    'ignorar_primeira_linha': values['-IGNORAR_PRIMEIRA_LINHA-'],
                    'login': values['-LOGIN_ONS_AMSE-'],
                    'passwd': values['-SENHA_ONS_AMSE-']
                }
                
                janela.close()
                inadimplencia_amse.executar_robo(informacoes_amse)