# Função que lê o arquivo indicado com a relação de contas, guardando-as em uma lista
def obter_relacao_contas(caminho_arquivo_contas_conciliaveis):
    contas_conciliaveis = []
    #abrindo o arquivo txt com a relação de contas
    with open(caminho_arquivo_contas_conciliaveis) as arquivo_contas:
        #Le o arquivo linha a linha
        for linha in arquivo_contas:
            # Verifica se a conta já está na lista
            if linha.strip().replace('\n', '') not in contas_conciliaveis:
                #se não estiver, inseri a conta na relação de contas conciliáveis
                contas_conciliaveis.append(linha.strip().replace('\n', ''))
    #fecha o arquivo
    arquivo_contas.close()
    
    return contas_conciliaveis
