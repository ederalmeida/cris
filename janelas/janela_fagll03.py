import PySimpleGUI as sg
from janelas import janela_abertura as ja
from robos import fagll03

def exibir():
    sg.theme('Reddit')   

    linha1 = [[sg.Text('Robô para Extração de Relatórios FAGLL03', size=(34, 1), justification='center', font=("Helvetica", 22))]]

    linha2 = [[sg.Text('_'  * 100, size=(72, 1))],      
              [sg.Text('Seleção de Partidas', font=('Helvetica', 15), justification='left')]
             ]

    linha3_coluna1 = [[sg.Frame('Status',
                       [[sg.Radio('Partidas em Aberto', 'STATUS_PARTIDAS', default=True, size=(18,1), key='-RADIO_PA-', enable_events=True),
                        sg.Radio('Todas as Partidas', 'STATUS_PARTIDAS', size=(18,1), key='-RADIO_TP-', enable_events=True)],
                        [sg.Text('Data Contabilização (DDMMAAAA)', size=(35, 1), font=('Helvetica', 10), key='-DATA_CONT_TEXTO-')],
                        [sg.Text('Em/De', size=(5, 1), key='-DATA_CONT_EMDE_TEXTO-'),
                        sg.InputText('', size=(13,1), key='-DATA_CONT_EMDE-', disabled=False, enable_events=True),
                        sg.Text('Até', size=(5, 1), key='-DATA_CONT_ATE_TEXTO-'),
                        sg.InputText('', size=(13,1), key='-DATA_CONT_ATE-', disabled=True, enable_events=True)],
                       [sg.Text('Data Efetiva (DDMMAAAA)', size=(35, 1), font=('Helvetica', 10), key='-DATA_EFET_TEXTO-')],
                       [sg.Text('Em/De', size=(5, 1), key='-DATA_EFET_EMDE_TEXTO-'),
                        sg.InputText('', size=(13,1), key='-DATA_EFET_EMDE-', disabled=False, enable_events=True),
                        sg.Text('Até', size=(5, 1), key='-DATA_EFET_ATE_TEXTO-'),
                        sg.InputText('', size=(13,1), key='-DATA_EFET_ATE-', disabled=False, enable_events=True)]])]
                    ]        

    linha3_coluna2 = [[sg.Frame('Tipo',
                       [[sg.Text('LEDGER'),
                        sg.Combo(('0L', '1L'), key='-LEDGER-')],
                       [sg.Text('')]])]]

    linha4 = [[sg.Text('_'  * 100, size=(72, 1))],
              [sg.Text('Outras Informações', font=('Helvetica', 15), justification='left')]
             ]                 

    linha5_coluna1 = [[sg.Frame('Dados',
                       [[sg.Text('Relação das Contas Conciliáveis (txt)')],
                        [sg.InputText('', key='-ARQUIVO_CONTAS-', size=(40, 1)), sg.FileBrowse('procurar')],
                        [sg.Text('Pasta onde serão salvos os relatórios', size=(40, 1))],
                        [sg.InputText('', key='-PASTA-', size=(40, 1)), sg.FolderBrowse('procurar')],
                        [sg.Text('Relação de Socidades Parceiras (txt)', size=(40, 1))],
                        [sg.InputText('', key='-ARQUIVO_SOCPAR-', size=(40, 1)), sg.FileBrowse('procurar')]]),
                    ]]

    linha5_coluna2 = [[sg.Frame('Company Code',
                    [[sg.Text('Empresa'),
                        sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-')]])],
                     [sg.Frame('Saída',
                    [[sg.Text('Layout'),
                        sg.InputText(default_text='/MD_CO_SECOG', size=(16,1), key='-LAYOUT-', enable_events=True)]]),
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

    janela = sg.Window('Robô para Extrair Relatórios FAGLL03', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-RADIO_PA-':
            janela['-DATA_CONT_EMDE-'].update(value='')
            janela['-DATA_CONT_ATE-'].update(disabled=True, value='')
        
    
        if event == '-RADIO_TP-':
            janela['-DATA_CONT_EMDE-'].update(value='')
            janela['-DATA_CONT_ATE-'].update(disabled=False, value='')   


        if event == '-EXECUTAR_ROBO-':
            if values['-RADIO_PA-'] == True and values['-DATA_CONT_EMDE-'] == '':
                sg.popup('Favor inserir data da posição do relatório', title='Erro')
            elif values['-RADIO_TP-'] == True and (values['-DATA_CONT_EMDE-'] == '' or values['-DATA_CONT_ATE-'] == ''):
                sg.popup('Favor inserir as datas da posição do relatório', title='Erro')
            elif values['-ARQUIVO_CONTAS-'] == '':
                sg.popup('Favor indicar o arquivo com a relação das contas conciliáveis', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde serão salvos os relatórios', title='Erro')
            elif values['-COMPANY_CODE-'] == '':
                 sg.popup('Favor indicar o Company Code', title='Erro')
            elif values['-LAYOUT-'] == '':
                sg.popup('Favor inserir um layout para visualização dos relatórios', title='Erro')
            elif values['-LEDGER-'] == '':
                sg.popup('Favor inserir o ledger a ser analisado', title='Erro')
            else:
                janela.close()
                informacoes_fagll03 = {
                           'arquivo_contas': values['-ARQUIVO_CONTAS-'],
                           'pasta': values['-PASTA-'],
                           'socidades_parceiras': values['-ARQUIVO_SOCPAR-'],
                           'data_cont_emde': (values['-DATA_CONT_EMDE-'].replace('.','')).replace('/',''),
                           'data_cont_ate': (values['-DATA_CONT_ATE-'].replace('.','')).replace('/',''),
                           'data_efet_emde': (values['-DATA_EFET_EMDE-'].replace('.','')).replace('/',''),
                           'data_efet_ate': (values['-DATA_EFET_ATE-'].replace('.','')).replace('/',''),
                           'partidas_aberta':  values['-RADIO_PA-'],
                           'todas_partidas':  values['-RADIO_TP-'],
                           'layout': values['-LAYOUT-'],
                           'ledger': values['-LEDGER-'],
                           'company_code':values['-COMPANY_CODE-']}
                fagll03.executar_robo(informacoes_fagll03)
