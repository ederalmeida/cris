import PySimpleGUI as sg
from janelas import janela_abertura as ja
from robos import fb03

def exibir():
    sg.theme('Reddit')

    linha1 = [[sg.Text('Extração de Informações de Documentos FB03', size=(32, 2), justification='center', font=("Helvetica", 23))]]

    linha2 = [[sg.Text('_'  * 100, size=(72, 1))]]
    
    linha3 = [[sg.Text('Relação dos Documentos')],
              [sg.InputText('', key='-ARQUIVO_DOCUMENTOS-', size=(73, 1)), sg.FileBrowse('procurar')],
              [sg.Text('Pasta onde serão salvos os relatórios')],
              [sg.InputText('', key='-PASTA-', size=(73, 1)), sg.FolderBrowse('procurar')],
              [sg.Text('Empresa'),
               sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')]
             ]
    
    linha4 = [[sg.Text('')],
              [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]]

    layout = [linha1,
              linha2,
              linha3,
              linha4]
    
    janela = sg.Window('Robo para Extração de Informações de Documentos FB03', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-EXECUTAR_ROBO-':
            if values['-ARQUIVO_DOCUMENTOS-'] == '':
                sg.popup('Favor indicar o arquivo com a relação dos documentos desejados', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde serão salvos os relatórios', title='Erro')
            elif values['-COMPANY_CODE-'] == '':
                 sg.popup('Favor indicar o Company Code', title='Erro')
            else:
                janela.close()
                informacoes_fb03 = {
                    'arquivo_documentos': values['-ARQUIVO_DOCUMENTOS-'],
                    'pasta': values['-PASTA-'],
                    'company_code':values['-COMPANY_CODE-']
                }
                fb03.executar_robo(informacoes_fb03)
