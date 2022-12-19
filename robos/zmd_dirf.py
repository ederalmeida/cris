import pyautogui as pag
from classes import sapgui
from janelas import janela_abertura as abertura
from apoio import obter_relacao_contas as orc
from apoio import verifica_cria_subpastas as vcs
from datetime import datetime

def executar_robo(informacoes_zmd_dirf):
    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    empresa = informacoes_zmd_dirf.get('company_code')
    exercicio = informacoes_zmd_dirf.get('exercicio')
    exercicio_corrente = informacoes_zmd_dirf.get('exercicio_corrente')
    exercicio_anterior = informacoes_zmd_dirf.get('exercicio_anterior')
    layout = informacoes_zmd_dirf.get('layout')
    cpf = informacoes_zmd_dirf.get('ncpf')
    caminho_cod_ctg_imp = informacoes_zmd_dirf.get('cod_imposto')
    caminho_salvar_ipe = informacoes_zmd_dirf.get('local_salvar_ipe')

    relacao_cod_cat_imposto = orc.obter_relacao_contas(caminho_cod_ctg_imp)
    
    caminho_pasta_salvar_ipes = vcs.verifica_pasta_print_rels(caminho_salvar_ipe, 'ZMD_DIRF_-_' + str(exercicio))
    
    data_execucao = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    # Abrindo a transação ZMD_DIRF
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'ZMD_DIRF'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Cóndições de seleção
    sap.session.findById("wnd[0]/usr/ctxtPCOMPANY").text = empresa
    sap.session.findById("wnd[0]/usr/txtPYEAR").text = exercicio
    sap.session.findById("wnd[0]/usr/radP_COMPE").select()
    sap.session.findById("wnd[0]/usr/radPRBACKGR").select()
    
    # Parametros de Execução
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/chkP_PUBLIC").selected = True
  
    # Dados Principais
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtCUR_YEAR").text = exercicio_corrente
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtPRE_YEAR").text = exercicio_anterior
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtLAYOUT").text = layout
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtC_CPF").text = cpf
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtCOMP_AM").text = ""
    
    if relacao_cod_cat_imposto != '':
        contador_numero_cod_cat_imposto_inseridos = 0
        numero_do_print_cod_cat_imposto_inseridos = 0
        screen_cod_ctg_imp = []
        primeira_execucao = True
        for cod_cat_imposto in relacao_cod_cat_imposto:
            if primeira_execucao:
                sap.session.findById("wnd[0]/usr/ctxtPWITHT-LOW").text = cod_cat_imposto
                sap.session.findById("wnd[0]/usr/btn%_PWITHT_%_APP_%-VALU_PUSH").press()
                primeira_execucao = False
            else:
                sap.session.findById("wnd[1]/tbar[0]/btn[13]").press()
                sap.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = cod_cat_imposto
            contador_numero_cod_cat_imposto_inseridos += 1
            if (contador_numero_cod_cat_imposto_inseridos % 7 == 0) or contador_numero_cod_cat_imposto_inseridos == len(relacao_cod_cat_imposto):
                            numero_do_print_cod_cat_imposto_inseridos += 1
                            screen_cod_ctg_imp.append([numero_do_print_cod_cat_imposto_inseridos, pag.screenshot()])
                            
        for screen in screen_cod_ctg_imp:
            screen[1].save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + str(exercicio) + ' - ' + \
                    data_execucao + ' - código categoria impostos - ' + str(screen[0]) + '.jpg')
        sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()

    # Dados do contador
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA").select()
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_NAME").text = "Sandro Rodrigues da Silva"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_CPF").text = "62329510934"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_DDD").text = "48"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_PHONE").text = "32317133"
    
    screen_dados_contador = pag.screenshot()
    screen_dados_contador.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + str(exercicio) + ' - ' + \
                    data_execucao + ' - dados contador.jpg')

    # Dados de Saida
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/").select()
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/radAPPLSERV").select()
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/txtFNAMEAPS").text = r"\\ELB3420\EP0\ESUL\FI\DIRF\2021\teste01.txt"
    
    screen_dados_saida = pag.screenshot()
    screen_dados_saida.save(vcs.winapi_path(caminho_pasta_salvar_ipes) + '\\prints\\' + str(exercicio) + ' - ' + \
                    data_execucao + ' - dados saida.jpg')
    
    
    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press()
    sap.session.findById("wnd[0]/tbar[1]/btn[19]").press()
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").selected = True
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").setFocus()
    sap.session.findById("wnd[1]/tbar[0]/btn[86]").press()