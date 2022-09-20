import datetime

class documento():

    def __init__ (self):
        self.concessao = ''
        self.cliente = ''
        self.competencia = ''
        self.vencimento = ''
        self.montante = ''


    def criar(dados_documentos):
                
        # obter relacao de concessoes
        relacao_concessoes =[]

        # obter relacao de clientes
        relacao_clientes =[]
        
        documentos_inadimplentes = ['documento_inadimplente' + str(i) for i in range(0, len(dados_documentos))]

        i = 0
        for i in range(0, len(documentos_inadimplentes)):
            
            documentos_inadimplentes[i] = documento()
            documentos_inadimplentes[i].concessao = dados_documentos[i][0]
            documentos_inadimplentes[i].cliente = dados_documentos[i][1]
            documentos_inadimplentes[i].competencia = dados_documentos[i][2].strftime('%Y%m')
            documentos_inadimplentes[i].vencimento = dados_documentos[i][3].strftime('%Y%m%d')
            documentos_inadimplentes[i].montante = dados_documentos[i][4]

        return documentos_inadimplentes
        


