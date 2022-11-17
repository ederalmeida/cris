from classes import sapgui

# Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
sap = sapgui.SapGui()
sap.logon()

# Abrindo a transação FAGLL03
sap.session.findById('wnd[0]').iconify()
sap.session.findById('wnd[0]').maximize()
sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'FAGLL03'
sap.session.findById('wnd[0]').sendVKey(0)

# Insirindo as informações necessárias na tela de Parametros
sap.session.findById('wnd[0]/usr/ctxtSD_SAKNR-LOW').text = '2110130003'
sap.session.findById('wnd[0]/usr/ctxtSD_BUKRS-LOW').text = 'ESUL'

sap.session.findById("wnd[0]/usr/radX_AISEL").select()
sap.session.findById("wnd[0]/usr/ctxtSO_BUDAT-LOW").text = '01102022'
sap.session.findById("wnd[0]/usr/ctxtSO_BUDAT-HIGH").text = '01102022'

# executa a geração do relatório
sap.session.findById('wnd[0]').sendVKey(8)

for i in range(0, sap.session.findById("wnd[0]/usr").Children.Count -1):
    print(sap.session.findById("wnd[0]/usr").Children.Item(i).Tooltip)
    print('item ', i)

