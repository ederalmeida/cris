import PySimpleGUI as sg
import sys
from apoio import cadastrar_fornecedor_avd_j1b1n as cfaj
from janelas import janela_avd_j1b1n as jaj

def exibir():
    sg.theme('LightGrey1')

    cabecalho = [[sg.Text('Cadastro de Fornecedor', size=(20, 1), justification='center', font=("Helvetica", 22))],
                 [sg.Text('_'  * 100, size=(50, 1))]]

    linha2_coluna1 = [[sg.Text('CNPJ do Fornecedor', size=(20, 1), key='-TXT_CNPJ_FORNECEDOR-')],
                      [sg.Text('(apenas números)', font=("Helvetica", 8), size=(25, 1), key='-DICA_CNPJ_FORNECEDOR-')],
                      [sg.InputText('', size=(25,1), key='-DADO_CNPJ_FORNECEDOR-', disabled=False, enable_events=True)]]

    linha2_coluna2 = [[sg.Text('Cód. SAP do Fornecedor', size=(20, 1), key='-TXT_COD_FORNECEDOR-')],
                      [sg.Text('(até 8 caracteres)',font=("Helvetica", 8), size=(20, 1), key='-DICA_COD_FORNECEDOR-')],
                      [sg.InputText('', size=(15,1), key='-DADO_COD_FORNECEDOR-', disabled=False, enable_events=True)]]

    linha2 = [[sg.Column(linha2_coluna1), sg.Column(linha2_coluna2)]]

    linha3 = [[sg.Button('Cadastrar', key='-CADASTRAR-', size=(15,1), enable_events=True)]]

    layout = [cabecalho,
              linha2,
              linha3]

    janela = sg.Window('CRIS - Central de Robôs para Interação com Sistemas', layout, element_justification='c', default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
             janela.close()
             jaj.exibir()

        if event == '-CADASTRAR-':
            if values['-DADO_CNPJ_FORNECEDOR-'] == '':
                sg.popup('Favor inserir CNPJ do fornecedor', title='Erro')
            elif values['-DADO_COD_FORNECEDOR-'] == '':
                sg.popup('Favor inserir cód. SAP para o fornecedor', title='Erro')
            else:
                cfaj.cadastrar(values['-DADO_CNPJ_FORNECEDOR-'], values['-DADO_COD_FORNECEDOR-'])
    
   
    