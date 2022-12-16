import pyautogui as pag
from classes import sapgui
from janelas import janela_abertura as abertura
from apoio import ober_relacao_contas as orc


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

    relacao_cod_cat_imposto = orc.obter_relacao_contas(caminho_cod_ctg_imp)

    # Abrindo a transação ZMD_DIRF
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'ZMD_DIRF'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Cóndições de seleção
    sap.session.findById("wnd[0]/usr/ctxtPCOMPANY").text = empresa
    sap.session.findById("wnd[0]/usr/txtPYEAR").text = exercicio

    if relacao_cod_cat_imposto != '':
        sap.session.findById("wnd[0]/usr/btn%_PWITHT_%_APP_%-VALU_PUSH").press()
        contador_numero_cod_cat_imposto_inseridos = 0
        numero_do_print_cod_cat_imposto_inseridos = 0
        screen_cod_ctg_imp = []
        for cod_cat_imposto in relacao_cod_cat_imposto:
            sap.session.findById("wnd[1]/tbar[0]/btn[13]").press()
            sap.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = cod_cat_imposto
            contador_numero_cod_cat_imposto_inseridos += 1
            if (contador_numero_cod_cat_imposto_inseridos % 7 == 0) or contador_numero_cod_cat_imposto_inseridos == len(relacao_cod_cat_imposto):
                            numero_do_print_cod_cat_imposto_inseridos += 1
                            screen_cod_ctg_imp.append([numero_do_print_cod_cat_imposto_inseridos, pag.screenshot()])
        sap.session.findById("wnd[1]/tbar[0]/btn[8]").press()

    # Parametros de Execução
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/chkP_PUBLIC").selected = true
  
    # Dados Principais
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtCUR_YEAR").text = exercicio_corrente
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtPRE_YEAR").text = exercicio_anterior
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtLAYOUT").text = layout
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtC_CPF").text = cpf
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtCOMP_AM").text = ""
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/chkP_PUBLIC").setFocus

    # Dados do contador
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA").select
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_NAME").text = "Sandro Rodrigues da Silva"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_CPF").text = "62329510934"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_DDD").text = "48"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_PHONE").text = "32317133"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_PHONE").setFocus
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpACC_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1002/txtR_PHONE").caretPosition = 8

    # Dados de Saida
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/radAPPLSERV").select
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/txtFNAMEAPS").text = "\\ELB3420\EP0\ESUL\FI\DIRF\2021\teste01.txt"
    
    
    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press
    sap.session.findById("wnd[0]/tbar[1]/btn[19]").press
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").selected = true
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").setFocus
    sap.session.findById("wnd[1]/tbar[0]/btn[86]").press