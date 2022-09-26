import PySimpleGUI as sg
from classes import amse
from janelas import janela_inadimplencia_amse as jia
from apoio import obter_arquivo_inadimplencia_amse as oaia
from apoio import gravar_log_cadastro_documento_inadimplente as glcdi


def executar_robo(informacoes_janela_inadimplencia_amse):

    # carregando os documentos a serem cadastrados
    documentos_atrasados = oaia.obter(informacoes_janela_inadimplencia_amse.get('arquivo_inadimplencia'),\
                                      informacoes_janela_inadimplencia_amse.get('ignorar_primeira_linha'))
    
    if documentos_atrasados != '':
        sistema_amse = amse.amse_site()
        sistema_amse.logon(informacoes_janela_inadimplencia_amse.get('login'), informacoes_janela_inadimplencia_amse.get('passwd'))

<<<<<<< HEAD
    for documento in documentos_atrasados:
        # TODO - criar ação para caso não exista concessão na tabela de DE-PARA
        sistema_amse.inserir_documento_inadimplente(documento)
        glcdi.gravar_logo(informacoes_janela_inadimplencia_amse.get('arquivo_inadimplencia'), documento)

    sg.popup('cadastro de inadimplência efetuado com sucesso!')
=======
        for documento in documentos_atrasados:
            # TODO - criar ação para caso não exista concessão na tabela de DE-PARA
            sistema_amse.inserir_documento_inadimplente(documento)
>>>>>>> 939958924149951706357c726a49784e95d8f486

        sg.popup('cadastro de inadimplência efetuado com sucesso!')
    
    jia.exibir()
