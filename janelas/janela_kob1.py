import PySimpleGUI as sg
import sys

def exibir():
    #sg.theme('DarkGrey14')   

    linha1 = [[sg.Text('Extrair Custos Reais de OI - KOB1', size=(32, 1), justification='center', font=("Helvetica", 23), relief=sg.RELIEF_RIDGE)]]

    linha2 = [[sg.Text('_'  * 100, size=(72, 1))],      
              [sg.Text('Informações', font=('Helvetica', 15), justification='left')]
             ]

    linha3_coluna1 = [[sg.Frame('Data',
                        [[sg.Text('formato da data DDMMAAAA', size=(35, 1), font=('Helvetica', 8), key='-DATA_TEXTO-')],
                        [sg.Text('De', size=(5, 1), key='-DATA_DE_TEXTO-'),
                        sg.InputText('', background_color='grey', size=(16,1), key='-DATA_DE-', enable_events=True),
                        sg.Text('Até', size=(5, 1), key='-DATA_ATE_TEXTO-'),
                        sg.InputText('', background_color='grey', size=(16,1), key='-DATA_ATE-', enable_events=True)]], size=(20,1))]
                    ]        
     
    linha5_coluna1 = [[sg.Frame('Dados',
                       [[sg.Text('Relação das Ordens')],
                        [sg.InputText('', background_color='grey', key='-ARQUIVO_ORDENS-', size=(40, 1)), sg.FileBrowse('procurar', button_color='black on white')],
                        [sg.Text('Pasta onde serão salvos os relatórios', size=(40, 1))],
                        [sg.InputText('', background_color='grey', key='-PASTA-', size=(40, 1)), sg.FolderBrowse('procurar', button_color='black on white')]
                       ], size=(40,1))
                    ]]

    linha5_coluna2= [[sg.Frame('Saída',
                    [[sg.Text('Layout'),
                        sg.InputText(default_text='/1SAP1', background_color='grey', size=(16,1), key='-LAYOUT-', enable_events=True)]])
                    ]]

    linha6 = [[sg.Text('')],
              [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', button_color='black on white', enable_events=True)]]

    layout = [linha1,
              linha2,
              linha3_coluna1,
              linha5_coluna1,
              linha5_coluna2,
              linha6
            ]      

    janela = sg.Window('Extrair Custos Reais de OI - KOB1', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()

        if event == '-EXECUTAR_ROBO-':
            if values['-DATA_DE-'] == '' or values['-DATA_ATE-'] == '':
                sg.popup('Favor inserir data da posição do relatório', title='Erro')
            elif values['-ARQUIVO_ORDENS-'] == '':
                sg.popup('Favor indicar o arquivo com a relação das ordens', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde serão salvos os relatórios', title='Erro')
            elif values['-LAYOUT-'] == '':
                sg.popup('Favor inserir um layout para visualização dos relatórios', title='Erro')
            else:
                break
            
    janela.close()

    return values['-ARQUIVO_ORDENS-'], values['-PASTA-'], values['-DATA_DE-'], values['-DATA_ATE-'], values['-LAYOUT-']
    