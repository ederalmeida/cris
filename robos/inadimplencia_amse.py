import PySimpleGUI as sg
from classes import amse
from janelas import janela_inadimplencia_amse as jia
from apoio import obter_arquivo_inadimplencia_amse as oaia
from apoio import gravar_log_cadastro_documento_inadimplente as glcdi


def executar_robo(informacoes_janela_inadimplencia_amse):

    login = informacoes_janela_inadimplencia_amse.get('login')
    passwd = informacoes_janela_inadimplencia_amse.get('passwd')
    caminho = informacoes_janela_inadimplencia_amse.get('arquivo_inadimplencia')
    ignorar = informacoes_janela_inadimplencia_amse.get('ignorar_primeira_linha')

    # carregando os documentos a serem cadastrados
    documentos_atrasados = oaia.obter(caminho, ignorar)

    if documentos_atrasados != None:
        sistema_amse = amse.amse_site()
        logon = sistema_amse.logon(login, passwd)
        if logon ==True:
            for documento in documentos_atrasados:
            # TODO - criar ação para caso não exista concessão na tabela de DE-PARA
                if documento.concessao != None:
                    sistema_amse.inserir_documento_inadimplente(documento, caminho)
                else:
                    glcdi.gravar_log(caminho, documento, 'Inadimplência não Cadastrada. Concessão não encontrada.')

            sistema_amse.logoff()
            sg.popup('cadastro de inadimplência efetuado com sucesso!')
    
    jia.exibir()
