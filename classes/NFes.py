from apoio import obter_relacao_xmls as orx
from apoio import obter_relacao_fornecedores as orf
import untangle as unt


class NFe():
    def __init__ (self):
        
        self.CNPJ = ''                  # CNPJ do emitente da NFe
        self.id_sap = ''                # Código SAP para o emissor da nota fiscal
        self.nNF = ''                   # Número da Nota Fiscal
        self.serie = ''                 # Série da Nota Fiscal
        self.chNFe = ''                 # Chave da Nota Fiscal
        self.tipo_emissao = ''          # Tipo de emissão da Nota Fiscal
        self.data_emissao = ''          # Data de emissão da Nota Fiscal
        self.data_processamento = ''    # Data em que a Nota Fiscal foi recebida pela empresa
        self.hora_processamento = ''    # hora em que a Nota Fiscal foi recebida pela empresa
        self.numero_aleatorio = ''      # Número aleatório gerado pelo emitente
        self.digito_verificador = ''    # dígito verificador da nota fiscal
        self.nProt = ''
        self.itens = []                 # Informaçãoes sobre os itens da nota fiscal
        self.caminho = ''               # Path do XML
        self.arquivo = ''               # Nome do arquivo XML

    def criar(caminho):

        relacao_xml = orx.obter_relacao_xmls(caminho)

        relacao_fornecedores = orf.obter()

        if len(relacao_xml) != 0:

            NFes = ['NFes' + str(i) for i in range(0, len(relacao_xml))]

        i = 0

        for i in range(0, len(relacao_xml)):

            with open(relacao_xml[i][0] + '\\' + relacao_xml[i][1], encoding='utf-8') as arquivo_nfe:
                xml = unt.parse(arquivo_nfe.read())

            NFes[i] = NFe()

            # Armazena CNPJ do emitente
            NFes[i].CNPJ = xml.nfeProc.NFe.infNFe.emit.CNPJ.cdata

            # Armazena o ID SAP para o fornecedor, baseado no CNPJ. Se não tiver, informa '#N/D' e será tratado na hora da escrituração
            NFes[i].id_sap = relacao_fornecedores.get(xml.nfeProc.NFe.infNFe.emit.CNPJ.cdata, '#N/D')

            # Armazena o número da nota fiscal
            NFes[i].nNF = xml.nfeProc.NFe.infNFe.ide.nNF.cdata

            # Armazena a série da nota fiscal
            NFes[i].serie = xml.nfeProc.NFe.infNFe.ide.serie.cdata

            # Armazena a Chave de Emissão da Nota Fiscal
            NFes[i].chNFe = xml.nfeProc.protNFe.infProt.chNFe.cdata
        
            # Armazena o tipo de emissão da Nota Fiscal
            NFes[i].tipo_emissao = xml.nfeProc.protNFe.infProt.chNFe.cdata[34:35]

            # Armazena a data da emissao (no padrão SAP) da nota fiscal
            NFes[i].data_emissao = (str(xml.nfeProc.NFe.infNFe.ide.dhEmi.cdata[8:10]) + \
                                    str(xml.nfeProc.NFe.infNFe.ide.dhEmi.cdata[5:7]) + \
                                    str(xml.nfeProc.NFe.infNFe.ide.dhEmi.cdata[0:4]))

            # Armazena a data de processamento (no padrão SAP) da nota fiscal
            NFes[i].data_processamento = (str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[8:10]) + \
                                        str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[5:7]) + \
                                        str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[0:4]))

            # Armazena a hora de processamento (no padrão SAP) da nota fiscal
            NFes[i].hora_processamento = (str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[11:13]) + \
                                        str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[14:16]) + \
                                        str(xml.nfeProc.protNFe.infProt.dhRecbto.cdata[17:19]))       

            # Armazena o número aleatório gerado pelo emitente
            NFes[i].numero_aleatorio = xml.nfeProc.protNFe.infProt.chNFe.cdata[35:43]

            # Armazena o dígito verificador da Nota Fiscal
            NFes[i].digito_verificador = xml.nfeProc.protNFe.infProt.chNFe.cdata[43:44]

            NFes[i].nProt = xml.nfeProc.protNFe.infProt.nProt.cdata
            NFes[i].caminho = relacao_xml[i][0]
            NFes[i].arquivo = relacao_xml[i][1]

            if type(xml.nfeProc.NFe.infNFe.det) == unt.Element:
                NFes[i].itens = [[1,
                                (xml.nfeProc.NFe.infNFe.det.prod.NCM.cdata[0:4] + '.' + \
                                    xml.nfeProc.NFe.infNFe.det.prod.NCM.cdata[4:6] + '.' + \
                                    xml.nfeProc.NFe.infNFe.det.prod.NCM.cdata[6:8]),
                                str(round(float(xml.nfeProc.NFe.infNFe.det.prod.qCom.cdata),2)).replace('.',','),
                                str(round(float(xml.nfeProc.NFe.infNFe.det.prod.vUnCom.cdata), 6)).replace('.',','),
                                str(round(float(xml.nfeProc.NFe.infNFe.det.prod.vProd.cdata), 2)).replace('.',',')]]
            
            if type(xml.nfeProc.NFe.infNFe.det) == list:
                l = 0
                itens =[]
                for n in range(0, len(xml.nfeProc.NFe.infNFe.det)):
                    itens.append([l+1,
                                (xml.nfeProc.NFe.infNFe.det[l].prod.NCM.cdata[0:4] + '.' + \
                                    xml.nfeProc.NFe.infNFe.det[l].prod.NCM.cdata[4:6] + '.' + \
                                    xml.nfeProc.NFe.infNFe.det[l].prod.NCM.cdata[6:8]),
                                str(round(float(xml.nfeProc.NFe.infNFe.det[l].prod.qCom.cdata),2)).replace('.',','),
                                str(round(float(xml.nfeProc.NFe.infNFe.det[l].prod.vUnCom.cdata), 6)).replace('.',','),
                                str(round(float(xml.nfeProc.NFe.infNFe.det[l].prod.vProd.cdata), 2)).replace('.',',')])
                    l += 1
                NFes[i].itens = itens
        
        return NFes
