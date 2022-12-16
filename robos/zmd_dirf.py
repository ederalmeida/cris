import pyautogui as pag
from classes import sapgui
from janelas import janela_abertura as abertura


def executar_robo(informacoes_zmd_dirf):
    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    sap = sapgui.SapGui()
    sap.logon()

    
    # Abrindo a transação ZMD_DIRF
    sap.session.findById('wnd[0]').iconify()
    sap.session.findById('wnd[0]').maximize()
    sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'ZMD_DIRF'
    sap.session.findById('wnd[0]').sendVKey(0)

    # Cóndições de seleção
    sap.session.findById("wnd[0]/usr/ctxtPCOMPANY").text = "ESUL"
    sap.session.findById("wnd[0]/usr/txtPYEAR").text = "2021"
    sap.session.findById("wnd[0]/usr/ctxtPWITHT-LOW").text = "E1"
    
    # Parametros de Execução
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/chkP_PUBLIC").selected = true
  
    # Dados Principais
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtCUR_YEAR").text = "2022"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtPRE_YEAR").text = "2021"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtLAYOUT").text = "XJFSFHB"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpMAIN_DATA/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1001/txtC_CPF").text = "623295109-34"
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
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT").select
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/radAPPLSERV").setFocus
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/radAPPLSERV").select
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/txtFNAMEAPS").text = "\\ELB3420\EP0\ESUL\FI\DIRF\2021\teste01.txt"
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/txtFNAMEAPS").setFocus
    sap.session.findById("wnd[0]/usr/tabsTABSTRIP_TDATA/tabpOUTPUT/ssub%_SUBSCREEN_TDATA:ZJ_1BLFDI:1003/txtFNAMEAPS").caretPosition = 43
    
    
    sap.session.findById("wnd[0]/tbar[1]/btn[8]").press
    sap.session.findById("wnd[0]/tbar[1]/btn[19]").press
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").selected = true
    sap.session.findById("wnd[1]/usr/chkSFPOUTPAR-REQIMM").setFocus
    sap.session.findById("wnd[1]/tbar[0]/btn[86]").press