import os
import pyautogui as pag
import PySimpleGUI as sg
import time
from datetime import datetime
from apoio import obter_relacao_itens as ori
from apoio import verifica_janelas as vj
from apoio import verifica_cria_subpastas as vcs
from janelas import janela_abertura as abertura
from classes import sapgui

def executar_robo(informacoes_janela_fb03):
    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    # CAMINHA_ARQUIVO_DOCUMENTOS - indica o path e o caminho para obter a relação de contas conciliáveis
    caminho_arquivo_documentos = informacoes_janela_fb03.get('arquivo_documentos')

    # CAMINHA_PASTA_RELATORIOS - indica o path onde serão salvos os relatórios
    caminho_pasta_relatorios = informacoes_janela_fb03.get('pasta')

    # COMPANY_CODE - empresa a ser uilizada para extração dos relatórios
    company_code = informacoes_janela_fb03.get('company_code')

    # Obtendo relação de documentos
    relacao_documentos = ori.obter_relacao_itens(caminho_arquivo_documentos)

    # Abrindo a transação FB03
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'FB03'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Verificando se o usuário tem acesso a transação desejada
    if sap.session.findById('wnd[0]/sbar').text == "Sem autorização para a transação FB03":
        sg.popup("Você não tem acesso a transação FB03. A execução do robô será cancelada")
        exit()
    
    for documento in relacao_documentos:
        # Verificando se existe a subpasta para salvar as informações geradas. Se não existir, cria.
        caminho_pasta_salvar_ipes = vcs.verifica_cria_subpastas(caminho_pasta_relatorios, documento)

        # Inserindo o número do documento e o company code
        sap.session.findById("wnd[0]/usr/txtRF05L-BELNR").text = documento
        sap.session.findById("wnd[0]/usr/ctxtRF05L-BUKRS").text = company_code
        sap.session.findById("wnd[0]/usr/txtRF05L-GJAHR").text = ''
        sap.session.findById('wnd[0]').sendVKey(0)

        # abrindo janela de cabeçalho do documento
        sap.session.findById("wnd[0]/tbar[1]/btn[5]").press()
        
        # colocando a tela de informação para o lado para não cobrir as informações geradas
        time.sleep(1)
        pag.press('alt')
        pag.press('m')
        for i in range(0, 11):
            pag.press('right', presses=15)
            time.sleep(0.5)
        pag.click()
        i = 0

        # Gerando IPE do documento
        screen_cabecalho = pag.screenshot()
        
        # fechando tela de cabeçalho
        sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()

        # Abrindo relação de lançamentos do documento
        sap.session.findById("wnd[0]/mbar/menu[0]/menu[5]").select()
        screen_relacao_lancamentos = pag.screenshot()

        # Exportando em excel
        sap.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[1]").select()
        caminho_para_arquivo_excel = str(vcs.winapi_path(caminho_pasta_salvar_ipes) + '/relatorios/' + documento + '.xlsx')
        pag.press('enter')
        #sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        pag.write(caminho_para_arquivo_excel)        
        pag.press('enter')

        # mapeando a janela ativa. Quando detectar que é o Excel, mata o processo.
        janela_ativa = ''
        while janela_ativa != 'EXCEL.EXE':
            time.sleep(1)
            janela_ativa = vj.verifica_janela_ativa()


        # Salvando os IPEs
        screen_cabecalho.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '/prints/' + documento + ' - cabecalho.jpg')
        screen_relacao_lancamentos.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '/prints/' + documento + ' - lancamentos.jpg')

        # Retornando para o início da transação
        sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()
        sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()