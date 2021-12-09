import PySimpleGUI as sg
from janelas import janela_abertura as ja

def exibir():
    sg.theme('LightGrey1')   

    linha1 = [[sg.Text('Robo para Extração de Relatórios FBL5N', size=(32, 1), justification='center', font=("Helvetica", 23))]]

    linha2 = [[sg.Text('_'  * 100, size=(72, 1))],      
              [sg.Text('Seleção de Partidas', font=('Helvetica', 15), justification='left')]
             ]

    linha3_coluna1 = [[sg.Frame('Status',
                        [[sg.Radio('Partidas em Aberto', 'STATUS_PARTIDAS', default=True, size=(18,1), key='-RADIO_PA-', enable_events=True),
                          sg.Radio('Todas as Partidas', 'STATUS_PARTIDAS', size=(18,1), key='-RADIO_TP-', enable_events=True)],
                         [sg.Text('formato da data DDMMAAAA', size=(35, 1), font=('Helvetica', 8), key='-DATA_TEXTO-')],
                         [sg.Text('Em/De', size=(5, 1), key='-DATA_DE_TEXTO-'),
                          sg.InputText('', size=(13,1), key='-DATA_EMDE-', disabled=False, enable_events=True),
                          sg.Text('Até', size=(5, 1), key='-DATA_ATE_TEXTO-'),
                          sg.InputText('', size=(13,1), key='-DATA_ATE-', disabled=True, enable_events=True)]])]
                     ]        

    linha3_coluna2 = [[sg.Frame('Tipo',
                       [[sg.Checkbox('Partidas normais', size=(18, 1), default=True, key='-PN-')],
                        [sg.Checkbox('Oper. Razão Especial', size=(18, 1), default=True, key='-ORE-')],
                        [sg.Checkbox('Partidas pré-editadas', size=(18, 1), default=False, key='-PPE-')]
                        ])]]

    linha4 = [[sg.Text('_'  * 100, size=(72, 1))],
              [sg.Text('Outras Informações', font=('Helvetica', 15), justification='left')]
             ]                 

    linha5_coluna1 = [[sg.Frame('Dados',
                       [[sg.Text('Relação de Contas de Clientes')],
                        [sg.InputText('', key='-ARQUIVO_CONTAS-', size=(40, 1)), sg.FileBrowse('procurar')],
                        [sg.Text('Pasta onde serão salvos os relatórios', size=(40, 1))],
                        [sg.InputText('', key='-PASTA-', size=(40, 1)), sg.FolderBrowse('procurar')]
                       ])
                    ]]

    linha5_coluna2 = [[sg.Frame('Company Code',
                    [[sg.Text('Empresa'),
                        sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')]])],
                     [sg.Frame('Saída',
                    [[sg.Text('Layout'),
                        sg.InputText(default_text='/MD_CO_SECOG', size=(16,1), key='-LAYOUT-', enable_events=True)]])
                    ]]

    linha6 = [[sg.Text('')],
              [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]]

    layout = [linha1,
              linha2,
              [sg.Column(linha3_coluna1), sg.Column(linha3_coluna2)],
              linha4,
              [sg.Column(linha5_coluna1), sg.Column(linha5_coluna2)],
              linha6
            ]      

    janela = sg.Window('Robô para Extrair Relatórios FBL5N', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-RADIO_PA-':
            janela['-DATA_EMDE-'].update(value='')
            janela['-DATA_ATE-'].update(disabled=True, value='')
        
    
        if event == '-RADIO_TP-':
            janela['-DATA_EMDE-'].update(value='')
            janela['-DATA_ATE-'].update(disabled=False, value='')   


        if event == '-EXECUTAR_ROBO-':
            if values['-RADIO_PA-'] == True and values['-DATA_EMDE-'] == '':
                sg.popup('Favor inserir data da posição do relatório', title='Erro')
            elif values['-RADIO_TP-'] == True and (values['-DATA_EMDE-'] == '' or values['-DATA_ATE-'] == ''):
                sg.popup('Favor inserir as datas da posição do relatório', title='Erro')
            elif values['-ARQUIVO_CONTAS-'] == '':
                sg.popup('Favor indicar o arquivo com a relação das contas conciliáveis', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde serão salvos os relatórios', title='Erro')
            elif values['-COMPANY_CODE-'] == '':
                 sg.popup('Favor indicar o Company Code', title='Erro')
            elif values['-LAYOUT-'] == '':
                sg.popup('Favor inserir um layout para visualização dos relatórios', title='Erro')
            elif values['-PN-'] == False and values['-PPE-'] == False:
                sg.popup('Favor selecionar tipo de partida', title='Erro')
            else:
                break
            
    janela.close()

    if values['-RADIO_PA-'] == True:
        return values['-ARQUIVO_CONTAS-'], values['-PASTA-'], 'PA', (values['-DATA_EMDE-'].replace('.','')).replace('/',''), '', values['-LAYOUT-'], values['-PN-'], values['-ORE-'], values['-PPE-'], values['-COMPANY_CODE-']
    else:
        return values['-ARQUIVO_CONTAS-'], values['-PASTA-'], 'TP', (values['-DATA_EMDE-'].replace('.','')).replace('/',''), (values['-DATA_ATE-'].replace('.','')).replace('/',''), values['-LAYOUT-'], values['-PN-'], values['-ORE-'], values['-PPE-'], values['-COMPANY_CODE-']