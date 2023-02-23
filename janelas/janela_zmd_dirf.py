import PySimpleGUI as sg
from janelas import janela_abertura as ja
from robos import zmd_dirf

def exibir():
    sg.theme('Reddit')

    linha1 = [[sg.Text('Robô para Extração de ZMD_DIRF', size=(34, 1), justification='center', font=("Helvetica", 22))],
              [sg.Text('_'  * 100, size=(72, 1))]]

    linha2 = [[sg.Frame('Condições de Seleção', 
                [[
                    sg.Text('Empresa'), sg.Combo(('ESUL', 'CHSF', 'CPEL', 'ELET', 'ENOR', 'ENUC', 'EPAR', 'FCE1'), key='-COMPANY_CODE-'),
                    sg.Text('Exercício'), sg.InputText(default_text='', size=(16,1), key='-EXERCICIO-', enable_events=True)
                 ],
                 [
                    sg.Text('Relação de Categoria de Impostos Retidos na Fonte (txt)')
                 ],
                 [
                    sg.InputText('', key='-REL_CTG_IMP_RET_FONTE-', size=(68, 1)), sg.FileBrowse('procurar')
                 ],
                 [
                    sg.Radio('Lançamento', 'APURACAO', key='-APURACAO_LANCAMENTO-'),
                    sg.Radio('Compensados', 'APURACAO', key='-APURACAO_COMPENSADOS-')
                 ]], size=(580,110)
                 )]]
    
    linha3 = [[sg.Frame('Parâmetros de Execução',
                [[
                    sg.Radio('Gerar Dados Background', 'PAREXEC', key='-PAREXEC_BACKGROUND-', enable_events=True),
                    sg.Radio('Exibir Dados Gerados', 'PAREXEC', key='-PAREXEC_EXIBIR-', enable_events=True),
                ]], size=(580,50)
                )]]

    linha4 = [[sg.Frame('Local para salvar arquivo Execução Background',
                [[
                    sg.InputText('', key='-LOCAL_SALVAR_REL_BACK-',enable_events=True , size=(68, 1)), sg.FolderBrowse('procurar')
                ]], size=(580,50)
                )]]   
   
    linha5 = [
                [sg.Frame('Dados Principais',
                    [
                        [
                            sg.Text('Exercício Corrente', size=(18,1)), sg.InputText(default_text='', size=(16,1), key='-EXERCICIO_CORRENTE-', enable_events=True),
                            sg.Text('Exercício Anterior', size=(18,1)), sg.InputText(default_text='', size=(16,1), key='-EXERCICIO_ANTERIOR-', enable_events=True)
                        ],
                        [
                            sg.Text('Identificação do Layout', size=(18,1)), sg.InputText(default_text='', size=(16,1), key='-ID_LAYOUT-', enable_events=True),
                                sg.Text('Número CPF', size=(18,1)), sg.InputText(default_text='', size=(16,1), key='-NCPF-', enable_events=True)
                            ]
                        
                    ], size=(580,80)
                )]]

    linha6 = [[[
                    sg.Text('Local para salvar relatórios e IPE')
                 ],
                 [
                    sg.InputText('', key='-LOCAL_SALVAR_REL_IPE-', size=(68, 1)), sg.FolderBrowse('procurar')
                 ]]]

    linha7 = [[sg.Text('')],
              [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]]
    
    layout = [linha1,
              linha2,
              linha3,
              linha4,
              linha5,
              linha6,
              linha7]
    
    janela = sg.Window('Robô para Extração de ZMD_DIRF', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            ja.exibir()

        if event == '-EXECUTAR_ROBO-':
            if values['-COMPANY_CODE-'] == '':
                sg.popup('Favor inserir uma empresa', title='Erro')

            elif values['-EXERCICIO-'] == '':
                sg.popup('Favor inserir um ano no campo exercício', title='Erro')

            elif values['-REL_CTG_IMP_RET_FONTE-'] == '':
                sg.popup('Favor selecionar o arquivo coma lista de Códigos de Imposto', title='Erro')

            elif values['-APURACAO_LANCAMENTO-'] == False and values['-APURACAO_COMPENSADOS-'] == False:
                sg.popup('Favor selecionar um tipo de apuração: Lançamento ou Compensado', title='Erro')
            
            elif values['-PAREXEC_BACKGROUND-'] == False and values['-PAREXEC_EXIBIR-'] == False:
                sg.popup('Favor selecionar um tipo de execução', title='Erro')
            
            elif values['-PAREXEC_BACKGROUND-'] == True and values['-LOCAL_SALVAR_REL_BACK-'] == '':
                sg.popup('Favor indicar um local para salvar o arquivo gerado em background', title='Erro')

            elif values['-EXERCICIO_CORRENTE-'] == '':
                sg.popup('Favor inserir um ano para o exercício corrente', title='Erro')

            elif values['-EXERCICIO_ANTERIOR-'] == '':
                sg.popup('Favor inserir um ano para o exercício anterior', title='Erro')

            elif values['-ID_LAYOUT-'] == '':
                sg.popup('Favor inserir um layout', title='Erro')

            elif values['-NCPF-'] == '':
                sg.popup('Favor inserir um número de CPF', title='Erro')
                
            elif values['-LOCAL_SALVAR_REL_IPE-'] == '':
                sg.popup('Favor inserir local para salva os IPEs', title='Erro')

            else:
                janela.close()
                informacoes_zmd_dirf= {
                    'company_code':values['-COMPANY_CODE-'],
                    'exercicio': values['-EXERCICIO-'],
                    'cod_imposto': values['-REL_CTG_IMP_RET_FONTE-'],
                    'exercicio_corrente': values['-EXERCICIO_CORRENTE-'],
                    'exercicio_anterior': values['-EXERCICIO_ANTERIOR-'],
                    'layout': values['-ID_LAYOUT-'],
                    'ncpf': values['-NCPF-'],
                    'local_salvar_ipe': values['-LOCAL_SALVAR_REL_IPE-'],
                    'gerar_dados_background': values['-PAREXEC_BACKGROUND-'],
                    'exibir_dados_gerados': values['-PAREXEC_EXIBIR-'],
                    'apuracao_lancamento': values['-APURACAO_LANCAMENTO-'],
                    'apuracao_compensado': values['-APURACAO_COMPENSADOS-'],
                    'local_salvar_rel_back': values['-LOCAL_SALVAR_REL_BACK-']
                    }
                zmd_dirf.executar_robo(informacoes_zmd_dirf)