# Função que lê o arquivo indicado com a relação de sociedades_parceiras, guardando-as em uma lista
def obter_relacao_sociedades_parceiras(caminho_arquivo_sociedades_parceiras):
    sociedades_parceiras = []
    #abrindo o arquivo txt com a relação de sociedades_parceiras
    with open(caminho_arquivo_sociedades_parceiras) as arquivo_sociedades_parceiras:
        #Le o arquivo linha a linha
        for linha in arquivo_sociedades_parceiras:
            # Verifica se a sociedades_parceiras já está na lista
            if linha.strip().replace('\n', '') not in sociedades_parceiras:
                #se não estiver, inseri a sociedade parceira a relação de sociedades parceiras
                sociedades_parceiras.append(linha.strip().replace('\n', ''))
    #fecha o arquivo
    arquivo_sociedades_parceiras.close()
    
    return sociedades_parceiras
