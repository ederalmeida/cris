import os
import pyautogui as pag
import PySimpleGUI as sg
import time
from datetime import datetime
from apoio import obter_relacao_ordens as oro
from apoio import verifica_janelas as vj
from apoio import verifica_cria_subpastas as vcs
from janelas import janela_abertura as abertura
from janelas import janela_kob1 as ja
from sap import sapgui

def executa_robo():

    informacoes_janela_kob1 = ja.exibir()

    sap = sapgui.SapGui()
    sap.logon()

    caminho_arquivo_ordens = informacoes_janela_kob1[0]
    caminho_pasta_relatorios = informacoes_janela_kob1[1]
    data_referencia_de = informacoes_janela_kob1[2]
    data_referencia_ate = informacoes_janela_kob1[3]
    mes_referencia = (informacoes_janela_kob1[3][4:] + informacoes_janela_kob1[3][2:4])
    layout = informacoes_janela_kob1[4]
    relacao_ordens = oro.obter_relacao_ordens(caminho_arquivo_ordens)

    # Abrindo a transação KOB1
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'KOB1'
    sap.session.findById('wnd[0]').sendVKey(0)

    for ordem in relacao_ordens:
        # Verificando se existe a subpasta para salvar as informações geradas. Se não existir, cria.
        caminho_pasta_salvar_ipes = vcs.verifica_cria_subpastas(caminho_pasta_relatorios, ordem)
        data_execucao = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        sap.session.findById("wnd[0]/usr/ctxtAUFNR-LOW").text = ordem
        sap.session.findById("wnd[0]/usr/ctxtP_DISVAR").text = layout
        sap.session.findById("wnd[0]/usr/ctxtR_BUDAT-LOW").text = data_referencia_de
        sap.session.findById("wnd[0]/usr/ctxtR_BUDAT-HIGH").text = data_referencia_ate
        
        screenParametrizacao = pag.screenshot()

        sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()

        # Verificando se a execução não teve dados exibidos. Se não houver dados, volta ao inicio do laço
        if sap.session.findById('wnd[0]/sbar').text == 'Não foi selecionada nenhuma part.indiv.custos reais':
            # Print resultado
            time.sleep(1)
            screenExecucao = pag.screenshot()
            # Salvando os prints tirados
            screenParametrizacao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + ordem +  ' - ' + \
                data_execucao + ' - KOB1 - 01 parametrizacao.jpg')
            screenExecucao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + ordem +  ' - ' + \
                data_execucao + ' - KOB1 - 02 resultados.jpg')
            continue

        screenExecucao = pag.screenshot()

        sap.session.findById('wnd[0]/mbar/menu[0]/menu[3]/menu[1]').select()
        sap.session.findById('wnd[0]').sendVKey(0)
        sap.session.findById('wnd[1]/usr/ctxtDY_PATH').text = caminho_pasta_salvar_ipes + '/relatorios'
        sap.session.findById('wnd[1]/usr/ctxtDY_FILENAME').text = (mes_referencia + ' - ' + ordem +  ' - '
        + data_execucao + ' - KOB1.xlsx')
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

        screenParametrizacao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + ordem +  ' - ' + \
            data_execucao + ' - KOB1 - 01 parametrizacao.jpg')
        screenExecucao.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + mes_referencia + ' - ' + ordem +  ' - ' + \
            data_execucao + ' - KOB1 - 02 resultados.jpg')

        # Volta para a tela de parâmetros
        sap.session.findById('wnd[0]').sendVKey(15)
    
    # encerrar robo
    sap.session.findById("wnd[0]/tbar[0]/btn[3]").press()

    sg.popup('Execução efetuada com sucesso')
    abertura.inicializacao()
