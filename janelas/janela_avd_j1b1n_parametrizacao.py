import PySimpleGUI as sg
from janelas import janela_avd_j1b1n as jaj
from apoio import parametrizacao_avd_j1b1n as paj

def exibir():
    sg.theme('LightGrey1')

    parametros = paj.obter()

    cabecalho = [[sg.Text('Parâmetros da transação J1B1N', size=(34, 1), justification='center', font=("Helvetica", 22))],
                 [sg.Text('_'  * 100, size=(72, 1))]]

    linha1 = [[sg.Text('Abertura', size=(34, 1), justification='center', font=("Helvetica", 22))],
              [sg.Text(''  * 100, size=(72, 1))]]

    linha2_coluna1 = [[sg.Text('Ctg. Nota Fiscal', size=(20, 1), key='-TXT_CTG_NOTA_FISCAL-'),
                      sg.InputText(parametros.get('ctg_nota_fiscal'), size=(19,1), key='-CTG_NOTA_FISCAL-', disabled=False, enable_events=True)],
                     [sg.Text('Local de negócios', size=(20, 1), key='-TXT_LOCAL_DE_NEGOCIOS-'),
                      sg.InputText(parametros.get('local_de_negocios'), size=(19,1), key='-LOCAL_DE_NEGOCIOS-', disabled=False, enable_events=True)]]

    linha2_coluna2 = [[sg.Text('NF função parceiro', size=(20, 1), key='-TXT_NF_FUNCAO_PARCEIRO-'),
                      sg.InputText(parametros.get('nf_funcao_parceiro'), size=(19,1), key='-NF_FUNCAO_PARCEIRO-', disabled=False, enable_events=True)],
                     [sg.Text('Incl. ICMS/ISS', size=(20, 1), key='-TXT_INCL_ICMS_ISS-'),
                      sg.InputText(parametros.get('incl.ICMS/ISS'), size=(19,1), key='-INCL_ICMS_ISS-', disabled=False, enable_events=True)]]
    

    linha3 = [[sg.Text(''  * 100, size=(72, 1))],
              [sg.Text('Síntese', size=(34, 1), justification='center', font=("Helvetica", 22))],
              [sg.Text(''  * 100, size=(72, 1))]]

    linha4_coluna1 = [[sg.Text('Tipo de Item', size=(20, 1), key='-TXT_TIPO_DE_ITEM-'),
                       sg.InputText(parametros.get('tipo_de_item'), size=(19,1), key='-TIPO_DE_ITEM-', disabled=False, enable_events=True)],
                      [sg.Text('Material', size=(20, 1), key='-TXT_MATERIAL-'),
                       sg.InputText(parametros.get('material'), size=(19,1), key='-MATERIAL-', disabled=False, enable_events=True)],
                      [sg.Text('Centro', size=(20, 1), key='-TXT_CENTRO-'),
                       sg.InputText(parametros.get('centro'), size=(19,1), key='-CENTRO-', disabled=False, enable_events=True)],
                      [sg.Text('Unidade', size=(20, 1), key='-TXT_UNIDADE-'),
                       sg.InputText(parametros.get('unidade'), size=(19,1), key='-UNIDADE-', disabled=False, enable_events=True)],
                      [sg.Text('Reg. Fiscal (RFB)', size=(20, 1), key='-TXT_REGIAO_FISCAL_EMPRESA-'),
                       sg.InputText(parametros.get('regiao_fiscal_empresa'), size=(19,1), key='-REGIAO_FISCAL_EMPRESA-', disabled=False, enable_events=True)],
                      [sg.Text('CFOP da MESMA região', size=(20, 1), key='-TXT_CFOP_MESMA_REGIAO-'),
                       sg.InputText(parametros.get('CFOP_para_NFe_da_mesma_regiao'), size=(19,1), key='-CFOP_MESMA_REGIAO-', disabled=False, enable_events=True)],
                      [sg.Text('CFOP de OUTRA região', size=(20, 1), key='-TXT_CFOP_OUTRA_REGIAO-'),
                       sg.InputText(parametros.get('CFOP_para_NFe_de_outra_regiao'), size=(19,1), key='-CFOP_OUTRA_REGIAO-', disabled=False, enable_events=True)],
                      [sg.Text('Dir. Fisc. ICMS', size=(20, 1), key='-TXT_DIR_FISC_ICMS-'),
                       sg.InputText(parametros.get('dir_fisc_icms'), size=(19,1), key='-DIR_FISC_ICMS-', disabled=False, enable_events=True)],
                      [sg.Text('Dir. Fisc. IPI', size=(20, 1), key='-TXT_DIR_FISC_IPI-'),
                       sg.InputText(parametros.get('dir_fisc_ipi'), size=(19,1), key='-DIR_FISC_IPI-', disabled=False, enable_events=True)]]

    linha4_coluna2 = [[sg.Text('Lei COFINS', size=(20, 1), key='-TXT_LEI_COFINS-'),
                       sg.InputText(parametros.get('lei_cofins'), size=(19,1), key='-LEI_COFINS-', disabled=False, enable_events=True)],
                      [sg.Text('Lei Trib PIS', size=(20, 1), key='-TXT_LEI_TRIB_PIS-'),
                       sg.InputText(parametros.get('lei_trib_pis'), size=(19,1), key='-LEI_TRIB_PIS-', disabled=False, enable_events=True)],
                      [sg.Text('Origem Material', size=(20, 1), key='-TXT_ORIGEM_MATERIAL-'),
                       sg.InputText(parametros.get('origem_material'), size=(19,1), key='-ORIGEM_MATERIAL-', disabled=False, enable_events=True)],
                      [sg.Text('Utilizção Material', size=(20, 1), key='-TXT_UTILIZACAO_MATERIAL-'),
                       sg.InputText(parametros.get('utilizacao_material'), size=(19,1), key='-UTILIZACAO_MATERIAL-', disabled=False, enable_events=True)],
                      [sg.Text('Situação Tribut ICMS', size=(20, 1), key='-TXT_SITUACAO_TRIBUT_ICMS-'),
                       sg.InputText(parametros.get('situacao_tribut_icms'), size=(19,1), key='-SITUACAO_TRIBUT_ICMS-', disabled=False, enable_events=True)],
                      [sg.Text('Situação Tribut IPI', size=(20, 1), key='-TXT_SITUACAO_TRIBUT_IPI-'),
                       sg.InputText(parametros.get('situacao_tribut_ipi'), size=(19,1), key='-SITUACAO_TRIBUT_IPI-', disabled=False, enable_events=True)],
                      [sg.Text('Situação Fiscal COFINS', size=(20, 1), key='-TXT_SITUACAO_FISCAL_COFINS-'),
                       sg.InputText(parametros.get('situacao_fis_cofins'), size=(19,1), key='-SITUACAO_FISCAL_COFINS-', disabled=False, enable_events=True)],
                      [sg.Text('Situação Fiscal PIS', size=(20, 1), key='-TXT_SITUACAO_FISCAL_PIS-'),
                       sg.InputText(parametros.get('situacao_fis_pis'), size=(19,1), key='-SITUACAO_FISCAL_PIS-', disabled=False, enable_events=True)],
                      [sg.Text(''),sg.Text('')]]

    linha5 = [[sg.Text(''  * 100, size=(72, 1))],
              [sg.Text('Detalhes', size=(34, 1), justification='center', font=("Helvetica", 22))],
              [sg.Text(''  * 100, size=(72, 1))]]

    linha6_coluna1 = [[sg.Text('Tipo de Imposto 1', size=(20, 1), key='-TXT_TIPO_IMPOSTO_1-'),
                       sg.InputText(parametros.get('tipo_imposto_1'), size=(19,1), key='-TIPO_IMPOSTO_1-', disabled=False, enable_events=True)],
                      [sg.Text('Tipo de Imposto 2', size=(20, 1), key='-TXT_TIPO_IMPOSTO_2-'),
                       sg.InputText(parametros.get('tipo_imposto_2'), size=(19,1), key='-TIPO_IMPOSTO_2-', disabled=False, enable_events=True)],
                      [sg.Text('Tipo de Imposto 3', size=(20, 1), key='-TXT_TIPO_IMPOSTO_3-'),
                       sg.InputText(parametros.get('tipo_imposto_3'), size=(19,1), key='-TIPO_IMPOSTO_3-', disabled=False, enable_events=True)],
                      [sg.Text('Tipo de Imposto 4', size=(20, 1), key='-TXT_TIPO_IMPOSTO_4-'),
                       sg.InputText(parametros.get('tipo_imposto_4'), size=(19,1), key='-TIPO_IMPOSTO_4-', disabled=False, enable_events=True)]]

    linha6_coluna2 = [[sg.Text('Taxa de Imposto 1', size=(20, 1), key='-TXT_TAXA_IMPOSTO_1-'),
                       sg.InputText(parametros.get('taxa_imposto_1'), size=(19,1), key='-TAXA_IMPOSTO_1-', disabled=False, enable_events=True)],
                      [sg.Text('Taxa de Imposto 2', size=(20, 1), key='-TXT_TAXA_IMPOSTO_2-'),
                       sg.InputText(parametros.get('taxa_imposto_2'), size=(19,1), key='-TAXA_IMPOSTO_2-', disabled=False, enable_events=True)],
                      [sg.Text('Taxa de Imposto 3', size=(20, 1), key='-TXT_TAXA_IMPOSTO_3-'),
                       sg.InputText(parametros.get('taxa_imposto_3'), size=(19,1), key='-TAXA_IMPOSTO_3-', disabled=False, enable_events=True)],
                      [sg.Text('Taxa de Imposto 4', size=(20, 1), key='-TXT_TAXA_IMPOSTO_4-'),
                       sg.InputText(parametros.get('taxa_imposto_4'), size=(19,1), key='-TAXA_IMPOSTO_4-', disabled=False, enable_events=True)]]

    linha7 = [[sg.Text(''  * 100, size=(72, 1))],
              [sg.Text('Dados Contábeis', size=(34, 1), justification='center', font=("Helvetica", 22))],
              [sg.Text(''  * 100, size=(72, 1))]]

    linha8_coluna1 = [[sg.Text('Forma de Pagamento', size=(20, 1), key='-TXT_FORMA_PAGAMENTO-'),
                       sg.InputText(parametros.get('forma_de_pagamento'), size=(19,1), key='-FORMA_PAGAMENTO-', disabled=False, enable_events=True)]]

    linha8_coluna2 = [[sg.Text('FrmPgto', size=(20, 1), key='-TXT_FRMPGTO-'),
                       sg.InputText(parametros.get('frm_pgto'), size=(19,1), key='-FRMPGTO-', disabled=False, enable_events=True)]]

    linha9 = [[sg.Text(''  * 100, size=(72, 1))],
              [sg.Button('Salvar Parametrização', key='-SALVAR-', size=(18,1), enable_events=True)],
              [sg.Text(''  * 100, size=(72, 1))]]

    layout = [cabecalho,
              linha1,
              [sg.Column(linha2_coluna1), sg.Column(linha2_coluna2)],
              linha3,
              [sg.Column(linha4_coluna1), sg.Column(linha4_coluna2)],
              linha5,
              [sg.Column(linha6_coluna1), sg.Column(linha6_coluna2)],
              linha7,
              [sg.Column(linha8_coluna1), sg.Column(linha8_coluna2)],
              linha9]

    janela = sg.Window('CRIS - Central de Robôs para Interação com Sistemas', layout, element_justification='c', default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            janela.close()
            jaj.exibir()

        if event == '-SALVAR-':
            parametros_salvos = {
                'ctg_nota_fiscal': values['-CTG_NOTA_FISCAL-'],
                'local_de_negocios': values['-LOCAL_DE_NEGOCIOS-'],
                'nf_funcao_parceiro': values['-NF_FUNCAO_PARCEIRO-'],
                'incl.ICMS/ISS': values['-INCL_ICMS_ISS-'],
                'tipo_de_item': values['-TIPO_DE_ITEM-'],
                'material': values['-MATERIAL-'],
                'centro': values['-CENTRO-'],
                'unidade': values['-UNIDADE-'],
                'regiao_fiscal_empresa': values['-REGIAO_FISCAL_EMPRESA-'],
                'CFOP_para_NFe_da_mesma_regiao': values['-CFOP_MESMA_REGIAO-'],
                'CFOP_para_NFe_de_outra_regiao': values['-CFOP_OUTRA_REGIAO-'],
                'dir_fisc_icms': values['-DIR_FISC_ICMS-'],
                'dir_fisc_ipi': values['-DIR_FISC_IPI-'],
                'lei_cofins': values['-LEI_COFINS-'],
                'lei_trib_pis': values['-LEI_TRIB_PIS-'],
                'origem_material': values['-ORIGEM_MATERIAL-'],
                'utilizacao_material': values['-UTILIZACAO_MATERIAL-'],
                'situacao_tribut_icms': values['-SITUACAO_TRIBUT_ICMS-'],
                'situacao_tribut_ipi': values['-SITUACAO_TRIBUT_IPI-'],
                'situacao_fis_cofins': values['-SITUACAO_FISCAL_COFINS-'],
                'situacao_fis_pis': values['-SITUACAO_FISCAL_PIS-'],
                'tipo_imposto_1': values['-TIPO_IMPOSTO_1-'],
                'tipo_imposto_2': values['-TIPO_IMPOSTO_2-'],
                'tipo_imposto_3': values['-TIPO_IMPOSTO_3-'],
                'tipo_imposto_4': values['-TIPO_IMPOSTO_4-'],
                'taxa_imposto_1': values['-TAXA_IMPOSTO_1-'],
                'taxa_imposto_2': values['-TAXA_IMPOSTO_2-'],
                'taxa_imposto_3': values['-TAXA_IMPOSTO_3-'],
                'taxa_imposto_4': values['-TAXA_IMPOSTO_4-'],
                'forma_de_pagamento': values['-FORMA_PAGAMENTO-'],
                'frm_pgto': values['-FRMPGTO-']
            }

            paj.salvar(parametros_salvos)
            sg.popup('Parâmetros salvos com sucesso!')
            janela.close()
            jaj.exibir()
