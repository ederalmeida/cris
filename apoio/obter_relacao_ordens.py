# Função que lê o arquivo indicado com a relação de contas, guardando-as em uma lista
def obter_relacao_ordens(caminho_arquivo_ordens):
    relacao_ordens = []
    #abrindo o arquivo txt com a relação de contas
    with open(caminho_arquivo_ordens) as arquivo_ordens:
        #Le o arquivo linha a linha
        for linha in arquivo_ordens:
            # Verifica se a conta já está na lista
            if linha.strip().replace('\n', '') not in relacao_ordens:
                #se não estiver, inseri a conta na relação de contas conciliáveis
                relacao_ordens.append(linha.strip().replace('\n', ''))
    #fecha o arquivo
    arquivo_ordens.close()
    
    return relacao_ordens
