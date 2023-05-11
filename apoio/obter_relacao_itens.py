# Função que lê o arquivo indicado com a relação de itens, guardando-os em uma lista
def obter_relacao_itens(caminho_arquivo_itens):
    relacao_itens = []
    #abrindo o arquivo txt com relação de itens
    with open(caminho_arquivo_itens) as arquivo_itens:
        #Le o arquivo linha a linha
        for linha in arquivo_itens:
            # Verifica se o item já está na lista
            if linha.strip().replace('\n', '') not in relacao_itens:
                #se não estiver, inseri o item na relação de itens
                relacao_itens.append(linha.strip().replace('\n', ''))
    #fecha o arquivo
    arquivo_itens.close()
    
    return relacao_itens
