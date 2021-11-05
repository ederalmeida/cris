import os
import pyautogui as pag
import PySimpleGUI as sg
import time
from datetime import datetime
from apoio import obter_relacao_contas as orc
from apoio import verifica_janelas as vj
from apoio import verifica_cria_subpastas as vcs
from janelas import janela_abertura as abertura
from janelas import janela_fbl3n as ja
from sap import sapgui

sg.theme('LightGrey1')

def executa_robo():
    # Chama a janela de interação do robô
    informacoes_janela_fbl3n = ja.exibir()
    
    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    # CAMINHA_ARQUIVO_CONTAS_CONCILIAVEIS - indica o path e o caminho para obter a relação de contas conciliáveis
    caminho_arquivo_contas_conciliaveis = informacoes_janela_fbl3n[0]

    # CAMINHA_PASTA_RELATORIOS - indica o path onde serão salvos os relatórios
    caminho_pasta_relatorios = informacoes_janela_fbl3n[1]

    # TIPO_DE_PARTIDAS - indica qual o tipo de partidas o usuário deseja visualizar.
    #  PA = Partidas em Aberto e TP = Todas as Partidas
    tipo_de_partidas = informacoes_janela_fbl3n[2]

    # DATA REFERENCIA_1 - data para a posição do relatório. Caso o usuário tenha optado por Todas as Partidas,
    #  essa data se refere ao campo "DE"
    data_referencia_1 = informacoes_janela_fbl3n[3]

    # DATA REFERENCIA_2 - data para a posição do relatório. Caso o usuário tenha optado por Todas as Partidas,
    #  essa data se refere ao campo "ATÉ"
    if tipo_de_partidas == 'TP':
        data_referencia_2 = informacoes_janela_fbl3n[4]

    # MES REFERENCIA - AAAAMM para inserir no inicio do nome do relatório exportado e no nome do screenshot
    mes_referencia = (informacoes_janela_fbl3n[3][4:] + informacoes_janela_fbl3n[3][2:4])

    # LAYOUT - layout que será utilizado para visualizar o relatórios
    layout = informacoes_janela_fbl3n[5]

    # PARTIDAS_NORMAIS
    partidas_normais = informacoes_janela_fbl3n[6]

    # Partidas Pré-editadas
    partidas_pre_editadas = informacoes_janela_fbl3n[7]

    # Company code que será utilizado na extração das informarções
    company_code = informacoes_janela_fbl3n[8]

    # Obtendo contas conciliáveis
    contas_conciliaveis = orc.obter_relacao_contas(caminho_arquivo_contas_conciliaveis)

    # Abrindo a transação FBL3N
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'FBL3N'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Verificando se o usuário tem acesso a transação desejada
    if sap.session.findById('wnd[0]/sbar').text == "Sem autorização para a transação FBL3N":
        sg.popup("Você não tem acesso a transação FBL3N. A execução do robô será cancelada")
        exit()

    # Laço de repetição, executado para cada conta da relação de contas conciliáveis
    for conta in contas_conciliaveis:

        # Verificando se existe a subpasta para salvar as informações geradas. Se não existir, cria.
        caminho_pasta_salvar_ipes = vcs.verifica_cria_subpastas(caminho_pasta_relatorios, conta)

        # Captura da data e hora para inserção no nome dos relatórios e dos prints
        data_execucao = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

        # Insirindo as informações necessárias na tela de Parametros
        sap.session.findById('wnd[0]/usr/ctxtSD_SAKNR-LOW').text = conta
        sap.session.findById('wnd[0]/usr/ctxtSD_BUKRS-LOW').text = company_code
        if tipo_de_partidas == 'PA':
            sap.session.findById("wnd[0]/usr/radX_OPSEL").select()
            sap.session.findById('wnd[0]/usr/ctxtPA_STIDA').text = data_referencia_1
        if tipo_de_partidas == 'TP':
            sap.session.findById("wnd[0]/usr/radX_AISEL").select()
            sap.session.findById("wnd[0]/usr/ctxtSO_BUDAT-LOW").text = data_referencia_1
            sap.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").text = data_referencia_2
        sap.session.findById("wnd[0]/usr/chkX_NORM").selected = partidas_normais
        sap.session.findById('wnd[0]/usr/chkX_PARK').selected = partidas_pre_editadas
        sap.session.findById('wnd[0]/usr/ctxtPA_VARI').text = layout

        # tirando print da parametrização
        screenParametrizacao = pag.screenshot()

        # executa a geração do relatório
        sap.session.findById('wnd[0]').sendVKey(8)

        # Verificando se a execução não teve dados exibidos. Se não houver dados, volta ao inicio do laço
        if sap.session.findById('wnd[0]/sbar').text == 'Nenhuma partida selecionada (ver texto descritivo)' or\
            sap.session.findById('wnd[0]/sbar').text == 'Nenhuma conta preenche as condições de seleção' or\
            sap.session.findById('wnd[0]/sbar').text == ('Sem autorização para empresa ' + company_code):
            # Print resultado
            time.sleep(1)
            screenExecucao = pag.screenshot()
            # Salvando os prints tirados
            screenParametrizacao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + conta +  ' - ' + \
                data_execucao + ' - FBL3N - ' + tipo_de_partidas + ' - 01 parametrizacao.jpg')
            screenExecucao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + conta +  ' - ' + \
                data_execucao + ' - FBL3N - ' + tipo_de_partidas + ' - 02 resultados.jpg')
            continue

        # Capturando informações do razão gerado
        # gerando visão totalizada por conta razão
        #sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
        sap.session.findById("wnd[0]/mbar/menu[1]/menu[10]").select()
        sap.session.findById("wnd[1]/usr/btnAPP_FL_ALL").press()
        sap.session.findById("wnd[1]/usr/btnB_SORT_UP").press()
        sap.session.findById("wnd[1]/usr/btnB_SEARCH").press()
        sap.session.findById("wnd[2]/usr/txtGD_SEARCHSTR").text = "Conta"
        sap.session.findById("wnd[2]/usr/txtGD_SEARCHSTR").caretPosition = 5
        sap.session.findById("wnd[2]/tbar[0]/btn[0]").press()
        sap.session.findById("wnd[1]/usr/tblSAPLSKBHTC_FIELD_LIST_820/txtGT_FIELD_LIST-SELTEXT[0,0]").setFocus
        sap.session.findById("wnd[1]/usr/tblSAPLSKBHTC_FIELD_LIST_820/txtGT_FIELD_LIST-SELTEXT[0,0]").caretPosition = 0
        sap.session.findById("wnd[1]/usr/btnAPP_WL_SING").press()
        sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        sap.session.findById("wnd[0]/mbar/menu[5]/menu[4]/menu[1]").select()
        sap.session.findById("wnd[1]/usr/lbl[1,4]").setFocus()
        sap.session.findById("wnd[1]/usr/lbl[1,4]").caretPosition = 3
        sap.session.findById("wnd[1]").sendVKey(2)

        # Abrindo tela de informações
        sap.session.findById('wnd[0]').sendVKey(35)
              
        # Esperando um segundo, para dar tempo da janela de informações aparecer antes de tirar o print
        time.sleep(1)

        # Abaixando a tela de informação para não cobrir as informações geradas
        pag.press('alt')
        pag.press('m')
        pag.press('down', presses=12)
        time.sleep(0.5)
        pag.press('down', presses=12)
        time.sleep(0.5)
        
        # Print resultado
        screenExecucao = pag.screenshot()
        
        # Fecha a janela de informações
        sap.session.findById('wnd[0]').sendVKey(0)

        #Exportanto para Excel
        sap.session.findById('wnd[0]/mbar/menu[0]/menu[3]/menu[1]').select()
        sap.session.findById('wnd[0]').sendVKey(0)
        sap.session.findById('wnd[1]/usr/ctxtDY_PATH').text = caminho_pasta_salvar_ipes + '/relatorios'
        sap.session.findById('wnd[1]/usr/ctxtDY_FILENAME').text = (mes_referencia + ' - ' + conta +  ' - '
        + data_execucao + ' - FBL3N - ' + tipo_de_partidas + '.xlsx')
        sap.session.findById('wnd[1]').sendVKey(0)

        # mapeando a janela ativa. Quando detectar que é o Excel, mata o processo.
        janela_ativa = ''
        while janela_ativa != 'EXCEL.EXE':
            time.sleep(1)
            janela_ativa = vj.verifica_janela_ativa()

        # neste ponto, foi detectado que o Excel passou a ser a janela ativa, e com isso o processo é encerrado
        os.system('TASKKILL /F /IM EXCEL.EXE')

        # Espera um segundo, para que o processo seja finalizado
        time.sleep(1)

        # Esvazia a variável, para que no próximo laço ele volte a rodar a detecção
        janela_ativa = ''

        # Salvando os prints tirados
        screenParametrizacao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + conta +  ' - ' + \
            data_execucao + ' - FBL3N - ' + tipo_de_partidas + ' - 01 parametrizacao.jpg')
        screenExecucao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + conta +  ' - ' + \
            data_execucao + ' - FBL3N - ' + tipo_de_partidas + ' - 02 resultados.jpg')

        # Volta para a tela de parâmetros
        sap.session.findById('wnd[0]').sendVKey(15)
    
    # encerrar robo
    sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()
    sg.popup('Execução efetuada com sucesso')
    abertura.inicializacao()