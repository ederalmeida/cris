from classes import sapgui
import PySimpleGUI as sg
import pyautogui as pg
from datetime import datetime
from apoio import verifica_cria_subpastas as vcs
from janelas import janela_zwf100 as jzwf


def executar_robo(informacoes_janela_zwf100):
    # Captura da data e hora para inserção no nome dos relatórios e dos prints
    data_execucao = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # Competencia - Baseada na data_comp_de, que vem da janela da transação
    competencia = str(informacoes_janela_zwf100.get('data_comp_de')[4:]) + str(informacoes_janela_zwf100.get('data_comp_de')[2:4])

    # Verificando se existe a subpasta para salvar as informações geradas. Se não existir, cria.
    caminho_pasta_salvar_ipes = vcs.verifica_cria_subpastas(informacoes_janela_zwf100.get('pasta'),\
                                                            informacoes_janela_zwf100.get('fornecedor'))

    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    # Abrindo a transação ZWF100
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'zwf100'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Verificando se o usuário tem acesso a transação desejada
    if sap.session.findById('wnd[0]/sbar').text == "Sem autorização para a transação ZWF100":
        sg.popup("Você não tem acesso a transação ZWF100. A execução do robô será cancelada")
        exit()

    fornecedor = informacoes_janela_zwf100.get('fornecedor')

    sap.session.findById("wnd[0]/usr/ctxtP_BUKRS").text = informacoes_janela_zwf100.get('empresa')
    sap.session.findById("wnd[0]/usr/radRB40").setFocus()
    sap.session.findById("wnd[0]/usr/radRB40").select()
    sap.session.findById("wnd[0]/usr/radRB40CHK3").setFocus()
    sap.session.findById("wnd[0]/usr/radRB40CHK3").select()
    sap.session.findById("wnd[0]/usr/ctxtS_AUGDT-LOW").text = informacoes_janela_zwf100.get('data_comp_de')
    sap.session.findById("wnd[0]/usr/ctxtS_AUGDT-HIGH").text = informacoes_janela_zwf100.get('data_comp_ate')
    sap.session.findById("wnd[0]/usr/ctxtS_LIFNR-LOW").text = fornecedor
    sap.session.findById("wnd[0]/usr/ctxtS_LIFNR-HIGH").setFocus()
    sap.session.findById("wnd[0]/usr/ctxtS_LIFNR-HIGH").caretPosition = 0

    # tirando print da parametrização
    screenParametrizacao = pg.screenshot()

    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").selectColumn("WRBTR")

    # tirando print do topo do relatório
    screen_topo_relatorio = pg.screenshot()

    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").pressToolbarButton("&MB_SUM")
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").currentCellRow = -1
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").selectColumn("WRBTR")
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").contextMenu()
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").selectContextMenuItem("&OPTIMIZE")

    # tirando print do total do relatório
    screen_total_relatorio = pg.screenshot()

    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").pressToolbarContextButton("&MB_EXPORT")
    sap.session.findById("wnd[0]/usr/cntlCCTR_9000/shellcont/shell").selectContextMenuItem("&XXL")
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()
    sap.session.findById("wnd[1]/usr/ctxtDY_PATH").text = caminho_pasta_salvar_ipes + '/relatorios'
    sap.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = ('ZWF100 - ' + competencia + ' - ' + fornecedor +  ' - ' + data_execucao + '.xlsx')
    sap.session.findById("wnd[1]/tbar[0]/btn[0]").press()

    # Salvando os prints
    screenParametrizacao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\ZWF100 - ' + competencia + ' - ' + fornecedor +  ' - ' + data_execucao + ' - 01 parametrizacao.jpg')
    screen_topo_relatorio.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\ZWF100 - ' + competencia + ' - ' + fornecedor +  ' - ' + data_execucao + ' - 02 topo_relatorio.jpg')
    screen_total_relatorio.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\ZWF100 - ' + competencia + ' - ' + fornecedor +  ' - ' + data_execucao + ' - 03 total_relatorio.jpg')

    sg.popup('Execução efetuada com sucesso')
    jzwf.exibir()