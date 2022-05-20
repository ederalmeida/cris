from classes import NFes, sapgui
from janelas import janela_avd_j1b1n as ja
from janelas import janela_abertura as abertura
from apoio import obter_parametrizacao_avd_j1b1n as opaj
from datetime import datetime
import PySimpleGUI as sg
import os

def executa_robo():
    # Chama a janela de interação do robô
    informacoes_janela_avd_j1b1n = ja.exibir()

    # DATA_CONTABILIZACAO - data para a contabilizacao das NFes
    data_contabilizacao = informacoes_janela_avd_j1b1n.get('data_contabilizacao')

    # COMPANY_CODE - empresa a ser uilizada para extração dos relatórios
    company_code = informacoes_janela_avd_j1b1n.get('company_code')
    
    # XMLS_A_ESCRITURAR - informações sobre as NFes
    NFes_a_escriturar = NFes.NFe.criar(informacoes_janela_avd_j1b1n.get('pasta'))

    # PARAMETRIZACAO - parametrizações para a transação
    parametrizacao = opaj.obter()

    # TABELA_AUX_LOG - tabela auxiliar para gerar logging da escrituração
    tabela_aux_log = []

    # Captura da data e hora para inserção no nome dos relatórios de log
    data_execucao = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    # Abrindo a transação J1B1N
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'J1B1N'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Aqui começa a escrituração para cada das NFe da relação de NFes
    for NFe in NFes_a_escriturar:
    
        # Checando se a NFe possui um código fornecedor SAP válido. Se não tiver, transfere o XML para a pasta "NÃO PROCESSADOS"
        # e passa para a próxima NFe
        if NFe.id_sap == '#N/D':
            tabela_aux_log.append([NFe.chNFe + ' - CNPJ ' + NFe.CNPJ, 'SEM CÓD SAP PARA FORNECEDOR', 'NÃO ESCRITURADA'])
            continue
        
        else:
            ### TELA DE ABERTURA
    
            # Campo "Ctg.nota fiscal"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-NFTYPE").Text = parametrizacao.get('ctg_nota_fiscal')

            # Campo "Empresa"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-BUKRS").Text = company_code
        
            # Campo "Local de negócio"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-BRANCH").Text = parametrizacao.get('local_de_negocios')
            
            # Campo "NF função parceiro"
            sap.session.findById("wnd[0]/usr/cmbJ_1BDYDOC-PARVW").Key = parametrizacao.get('nf_funcao_parceiro')
            
            # Campo "ID Parceiro"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-PARID").Text = NFe.id_sap
            
            # Campo "Entrada de valores"
            sap.session.findById("wnd[0]/usr/chkJ_1BDYLIN-INCLTX").SetFocus()
            
            # Indo para a tela de criação da NFe
            sap.session.findById("wnd[0]").sendVKey(0)

            #### TELA DE CRIAÇÃO
            
            ###### CABEÇALHO
            # Campo "No. 9 posições"
            sap.session.findById("wnd[0]/usr/subNF_NUMBER:SAPLJ1BB2:2002/txtJ_1BDYDOC-NFENUM").Text = NFe.nNF
            
            # Campo "Série" (ao lado do anterior)
            sap.session.findById("wnd[0]/usr/txtJ_1BDYDOC-SERIES").Text = NFe.serie
            
            # Campo "Data Documento"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-DOCDAT").Text = NFe.data_emissao
            
            # Campo "Data Contabilização"
            sap.session.findById("wnd[0]/usr/ctxtJ_1BDYDOC-PSTDAT").Text = data_contabilizacao

            ###### SÍNTESE

            linha_sintese_sap = 0
            for item in NFe.itens:
                
                # Campo "Tipo de Item"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-ITMTYP[1," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('tipo_de_item')

                # Campo "Material"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-MATNR[4," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('material')
                
                # Campo "Centro"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-WERKS[6," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('centro')
                
                # Campo "Quantidade"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/txtJ_1BDYLIN-MENGE[10," + str(linha_sintese_sap) + "]").Text = item[2]
                
                # Campo "Unidade"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-MEINS[11," + str(linha_sintese_sap) + "]").Text = "UN"
                
                # Campo "Preço"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/txtJ_1BDYLIN-NETPR[19," + str(linha_sintese_sap) + "]").Text = item[3]
                
                # Campo "Valor"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/txtJ_1BDYLIN-NETWR[20," + str(linha_sintese_sap) + "]").Text = item[4]
                
                # Campo "CFOP"
                if str(NFe.chNFe[0:2]) == str(parametrizacao.get('regiao_fical_empresa')):
                    sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-CFOP[26," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('CFOP_para_NFe_da_mesma_regiao')
                else:
                    sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-CFOP[26," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('CFOP_para_NFe_de_outra_regiao')
            
                # Campo "Dir.fisc.:ICMS"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-TAXLW1[27," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('dir_fisc_icms')
                
                # Campo "Dir.fisc.:IPI"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-TAXLW2[28," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('dir_fisc_ipi')
            
                # Campo "Lei COFINS"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-TAXLW4[30," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('lei_cofins')
            
                # Campo "Lei Trib PIS"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-TAXLW5[31," + str(linha_sintese_sap) + "]").Text = parametrizacao.get('lei_trib_pis')
            
                # Campo "Origem Material"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/cmbJ_1BDYLIN-MATORG[32," + str(linha_sintese_sap) + "]").Key = parametrizacao.get('origem_material')
            
                # Campo "Utilização Material"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/cmbJ_1BDYLIN-MATUSE[33," + str(linha_sintese_sap) + "]").Key = parametrizacao.get('utilizacao_material')
            
                # Campo "Cód. Controle" (NCM)
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/ctxtJ_1BDYLIN-NBM[34," + str(linha_sintese_sap) + "]").Text = item[1]
            
                # Selecionando a linha da aba que esta sendo preenchida
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL").getAbsoluteRow(linha_sintese_sap).Selected = True
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/txtJ_1BDYLIN-ITMNUM[0,0]").SetFocus
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/tblSAPLJ1BB2ITEM_CONTROL/txtJ_1BDYLIN-ITMNUM[0,0]").caretPosition = 0

                # Selecionando "Detalhes do Item"
                sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB1/ssubHEADER_TAB:SAPLJ1BB2:2100/btn%#AUTOTEXT001").press()
            
                if sap.session.findById("wnd[0]/sbar").messagetype == "W":
                    sap.session.findById("wnd[0]").sendVKey(0)

                # Selecionando a aba "Impostos"
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX").Select()
                
                # Preenchendo coluna com Tipo de Imposto
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/ctxtJ_1BDYSTX-TAXTYP[0,0]").Text = parametrizacao.get('tipo_imposto_1')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/ctxtJ_1BDYSTX-TAXTYP[0,1]").Text = parametrizacao.get('tipo_imposto_2')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/ctxtJ_1BDYSTX-TAXTYP[0,2]").Text = parametrizacao.get('tipo_imposto_3')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/ctxtJ_1BDYSTX-TAXTYP[0,3]").Text = parametrizacao.get('tipo_imposto_4')
                
                # Preenchendo coluna com Taxa de Imposto
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-RATE[4,0]").Text = parametrizacao.get('taxa_imposto_1')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-RATE[4,1]").Text = parametrizacao.get('taxa_imposto_2')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-RATE[4,2]").Text = parametrizacao.get('taxa_imposto_3')
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-RATE[4,3]").Text = parametrizacao.get('taxa_imposto_4')
                
                # Preenchendo coluna com valor de
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-OTHBAS[7,0]").Text = item[4]
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-OTHBAS[7,1]").Text = item[4]
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-OTHBAS[7,2]").Text = item[4]
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL/txtJ_1BDYSTX-OTHBAS[7,3]").Text = item[4]
                
                # Calculando os tributos
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL").getAbsoluteRow(0).Selected = True
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL").getAbsoluteRow(1).Selected = True
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL").getAbsoluteRow(2).Selected = True
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/tblSAPLJ1BB2TAX_CONTROL").getAbsoluteRow(3).Selected = True
                sap.session.findById("wnd[0]/usr/tabsITEM_TAB/tabpTAX/ssubITEM_TABS:SAPLJ1BB2:3200/btnPB_CALCULATOR").press()
                
                # Salvando as informações
                sap.session.findById("wnd[0]/tbar[0]/btn[0]").press()
                sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()
                
                linha_sintese_sap += 1
        
        linha_sintese_sap = 0

        
        # Selecionando tab6 - "DDS. CONTS." ao mesmo tempo que verifica se o SAP apresentou mensagem de advertência
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB6").Select()
        if sap.session.findById("wnd[0]/sbar").messagetype == "W":
            sap.session.findById("wnd[0]").sendVKey(0)
                
        # Campo "Forma de Pagamento"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB6/ssubHEADER_TAB:SAPLJ1BB2:2600/tblSAPLJ1BB2PAYMENT_CONTROL/cmbJ_1BDYPAYMENT-IND_PAG[1,0]").Key = "1"
        
        # Campo "FrmPgto"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB6/ssubHEADER_TAB:SAPLJ1BB2:2600/tblSAPLJ1BB2PAYMENT_CONTROL/cmbJ_1BDYPAYMENT-T_PAG[2,0]").Key = "99"
    
        # Selecionando tab8 - "DadosNF-e"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8").Select()

        # Campo "No. do Log"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subTIMESTAMP:SAPLJ1BB2:2803/txtJ_1BDYDOC-AUTHCOD").Text = NFe.nProt
            
        # Campo "Data procmto"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subTIMESTAMP:SAPLJ1BB2:2803/ctxtJ_1BDYDOC-AUTHDATE").Text = NFe.data_processamento
            
        # Campo "Hora procmto"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subTIMESTAMP:SAPLJ1BB2:2803/ctxtJ_1BDYDOC-AUTHTIME").Text = NFe.hora_processamento
            
        # Campo "Tp. Emissão"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subRANDOM_NUMBER:SAPLJ1BB2:2801/ctxtJ_1BNFE_DOCNUM9_DIVIDED-TPEMIS").Text = NFe.tipo_emissao
        
        # Campo "No. Aleatório"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subRANDOM_NUMBER:SAPLJ1BB2:2801/txtJ_1BNFE_DOCNUM9_DIVIDED-DOCNUM8").Text = NFe.numero_aleatorio
            
        # Campo "Dig. verif"
        sap.session.findById("wnd[0]/usr/tabsTABSTRIP1/tabpTAB8/ssubHEADER_TAB:SAPLJ1BB2:2800/subRANDOM_NUMBER:SAPLJ1BB2:2801/txtJ_1BNFE_ACTIVE-CDV").Text = NFe.digito_verificador
            
        # Salvando a nota fiscal gerada
        sap.session.findById("wnd[0]/tbar[0]/btn[11]").press()
    
        # Se a nota já existir, gera log e passa para a próxima
        if sap.session.findById("wnd[0]/sbar").messagetype == "E":
            tabela_aux_log.append([NFe.chNFe, 'NOTA JÁ ESCRITURADA ' + sap.session.findById("wnd[0]/sbar").Text, 'NÃO ESCRITURADA'])
            sap.session.findById("wnd[0]/tbar[0]/btn[12]").press()
            sap.session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
        else:
            tabela_aux_log.append([NFe.chNFe, sap.session.findById("wnd[0]/sbar").Text, 'NOTA ESCRITURADA COM SUCESSO'])
        
        # transfere o XML para a pasta PROCESSADAS
        if not os.path.isdir(NFe.caminho + '\\PROCESSADAS'):
            os.mkdir(NFe.caminho + '\\PROCESSADAS')
        os.replace(NFe.caminho + '\\' + NFe.arquivo, NFe.caminho + '\\PROCESSADAS\\' + NFe.arquivo ) 
    
        # Verifica se a NFe atual é última da lista de NFes
        if NFes_a_escriturar.index(NFe) != (len(NFes_a_escriturar) - 1):
        
            # Se não for, verifica se o CNPJ da NFe atual é igual o CNPJ da próxima
            if NFe.CNPJ != NFes_a_escriturar[NFes_a_escriturar.index(NFe) + 1].CNPJ:

                # Se for diferente, sai da transação e retorna, para forçar que o SAP limpe o cache
                sap.session.findById("wnd[0]/tbar[0]/btn[12]").press()
                sap.session.findById("wnd[0]/tbar[0]/okcd").setfocus()
                sap.session.findById("wnd[0]/tbar[0]/okcd").text = "J1B1N"
                sap.session.findById("wnd[0]").sendVKey(0)
    
    # Criando arquivo de logging
    arquivo_de_log = open(informacoes_janela_avd_j1b1n[2] + '\\log de execução ' + data_execucao + '.txt', 'w')

    for linha in tabela_aux_log:
        arquivo_de_log.writelines(linha[0] + ' - ' + linha[1] + ' - ' + linha[2] + '\n')
    arquivo_de_log.close()

        # encerrar robo
    sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()
    sg.popup('Execução efetuada com sucesso')
    abertura.inicializacao()

#TODO: melhorar a tela de parametrizacao
        