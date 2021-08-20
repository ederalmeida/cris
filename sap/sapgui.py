# Implimentação/port baseada na macro criada por Fabio Mitsueda (https://fabiomitsueda.com.br)
from janelas import janela_info_sessao_aberta as jisa
from janelas import janela_logon as jl
from pathlib import Path
import PySimpleGUI as sg
import subprocess
import sys
import time
import win32com.client as win32

class SapGui(object):
    def __init__(self):
        self.path = 'C:/Program Files (x86)/SAP/FrontEnd/SAPgui/saplogon.exe'
        self.session = ''
        self.nome_ambiente = ''
        self.user = ''
        self.passwd = ''

        # Verifica se o executável do SAP GUI está instalado no computador. Se não estiver, já interrompe
        #   a execução do robô e informa ao usuário.
        executavelSapLogon = Path(self.path)
        
        if not executavelSapLogon.is_file():
            sg.popup('Não foi possível encontrar o arquivo saplogon.exe', title='ERRO')
            exit()

    def logon(self):
        # Verifica se o Sap Logon já está aberto. Se não estiver, já executa uma nova sessão.
        sessao_sap_aberta = self.verifica_sessao_sap_aberta()

        if sessao_sap_aberta == '':
            self.nova_sessao()

        else:
            #Se retornar um objeto SAP, verifica se o Usuário quer utilizar a sessão aberta ou abrir uma nova
            informacoes_sessao_sap_aberta = self.captura_informacoes_sessao_sap_aberta(sessao_sap_aberta)

            if informacoes_sessao_sap_aberta == '':
                self.nova_sessao()
            else:
                self.verifica_se_sera_utilizado_sessao_sap_aberta(informacoes_sessao_sap_aberta)
    
    def verifica_sessao_sap_aberta(self):
        i = 0
        objetoSAP = ''

        while i < 10 and objetoSAP == '':
            i += 1
            try:
                objetoSAP = win32.GetObject('SAPGUI')
            except:
                objetoSAP = ''

        return objetoSAP
    
    def nova_sessao(self):

        informacoes_logon = jl.janela_logon()
        
        self.nome_ambiente = informacoes_logon[0]
        self.user = informacoes_logon[1]
        self.passwd = informacoes_logon[2]
        
        # abrindo o SAPlogon
        process = subprocess.Popen(self.path, stdout=subprocess.PIPE)
        time.sleep(5)

        # Carrengado a varial com as propriedades do SAP LOGON
        SapGuiAuto = win32.GetObject('SAPGUI')
        application = SapGuiAuto.GetScriptingEngine
        connection = application.OpenConnection(self.nome_ambiente, True)
        self.session = connection.Children(0)
        self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = self.user
        self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = self.passwd
        self.session.findById("wnd[0]").sendVKey(0)

    def verifica_se_sera_utilizado_sessao_sap_aberta(self, informacoes_sessao_sap_aberta):
        # Pergunta se o usuário quer utilizar a Instância já aberta
        usar_instancia_aberta = jisa.janela_info_sessao_aberta(informacoes_sessao_sap_aberta[0][1], informacoes_sessao_sap_aberta[0][2])

        if usar_instancia_aberta == True:
            # verifica se a janela SAP está na tela inicial
            if informacoes_sessao_sap_aberta[0][3] == True:
                objConnection = informacoes_sessao_sap_aberta[0][4]
                Session = informacoes_sessao_sap_aberta[0][5]
                # Procurando a janela incial dentro das possíveis janelas abertas nessa conexão
                for Session in objConnection.Children:
                    if Session.Busy == False:
                        if Session.Info.Transaction == 'SESSION_MANAGER':
                            self.session = Session
                            break
                
            # Caso não tenha uma janela na tela iniciar, cria uma nova janela para a transação
            else:
                # Caso o usuário responde que quer reutilizar a conexão existente, verifica se já há 6 janelas abertas
                #   (o que impossibilita a criação de uma nova). Se houver, encerra a execução
                if informacoes_sessao_sap_aberta[0][0] == 6:
                    sg.popup('Este usuário já possui 6 janelas SAP abertas. Impossível abrir uma nova')
                    sys.exit()
                else:
                    objConnection = informacoes_sessao_sap_aberta[0][4]
                    Session = informacoes_sessao_sap_aberta[0][5]
                    # Criando a nova janela
                    Session.createSession()
                    time.sleep(2)
                    for Session in objConnection.Children:
                        if Session.Busy == False:
                            if Session.Info.Transaction == 'SESSION_MANAGER':
                                self.session = Session
                                break
        # Caso o usuário opte por iniciar uma nova instância, abre a tela de Login
        else:
            self.nova_sessao()
    

    def captura_informacoes_sessao_sap_aberta(self, sessao_sap_aberta):
        informacoes_sessao_sap_aberta = []
        i = 0
        l = 0
        # Carrendo a variável que representa a janela do SAP
        objSapAPP = sessao_sap_aberta.GetScriptingEngine

        # Percorrendo todas as janels abertas do SAP e capturando as informações pertinentes
        for objConnect in objSapAPP.Children:

            # Se a conexão caiu não executar o teste para a janela
            if not objConnect.DisabledByServer:
                for objSession in objConnect.Children:

                    # Verifica se a sessão está em excecução
                    if objSession.Busy == False:

                        # Verificando se está logado através da transação S000, que é a tela de login
                        if objSession.info.Transaction != 'S000':
                            strID = objSession.Info.SystemName
                            strUser = objSession.info.user
                            strTransacao = objSession.Info.Transaction
                            
                            # Verifica se existe janelas disponíveis na tela inicial do SAP logado
                            if strTransacao == 'SESSION_MANAGER':
                                fCheck = True
                            else:
                                fCheck = False

                            # Capturando dandos
                            if i == 0:
                                i += 1
                                l += 1
                                # aqui inseri as informações de usuário (login, senha, objetos de conexão) na lista
                                informacoes_sessao_sap_aberta.append(
                                    [l, strID, strUser, fCheck, objConnect, objSession]
                                )
                            else:
                                if strID != informacoes_sessao_sap_aberta[i - 1][1]:
                                    i += 1
                                    l += 1
                                    informacoes_sessao_sap_aberta.append = [
                                    [l, strID, strUser, fCheck, objConnect, objSession]
                                    ]
                                else:
                                    informacoes_sessao_sap_aberta[i - 1][0] = (informacoes_sessao_sap_aberta[i - 1][0] + 1)
                                    if fCheck == True:
                                        informacoes_sessao_sap_aberta[i - 1][3] = fCheck

            l = 0
            fCheck = False

        if i == 0:
            return ''
        else:
            return informacoes_sessao_sap_aberta
