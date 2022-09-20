from cmath import inf
from logging import info
from classes import amse
from janelas import janela_abertura as abertura
from apoio import obter_arquivo_inadimplencia_amse as oaia
from classes import documentos_inadimplente as di


def executar_robo(informacoes_janela_inadimplencia_amse):

    # carregando os documentos a serem cadastrados
    documentos_atrasados = oaia.obter(informacoes_janela_inadimplencia_amse.get('arquivo_inadimplencia'),\
                                      informacoes_janela_inadimplencia_amse.get('ignorar_primeira_linha'))
    
    sistema_amse = amse.amse_site()
    sistema_amse.logon(informacoes_janela_inadimplencia_amse.get('login'), informacoes_janela_inadimplencia_amse.get('passwd'))

    for documento in documentos_atrasados:
        sistema_amse.inserir_documento_inadimplente(documento)



