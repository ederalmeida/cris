from apoio import arquivoInadimplentes as aI

class empresa():

    def __init__ (self):
        self.dado1 = ''
        self.dado2 = ''
        self.dado3 = ''
        self.dado4 = ''
        self.dado5 = ''
        self.dado6 = ''
        self.dado7 = ''
        self.dado8 = ''
        self.dado9 = ''
        self.dado10 = ''

    def criar():
        dados_importados_empresas = aI.importar()
        
        empresas = ['empresa_inadimplente' + str(i) for i in range(0, len(dados_importados_empresas))]

        i = 0
        for i in range(0, len(empresas)):
            
            empresa_inadimplente[i] = empresa()

            empresa_inadimplente[i].dado1 = empresas[i][0]
            empresa_inadimplente[i].dado2 = empresas[i][1]
            empresa_inadimplente[i].dado3 = empresas[i][2]
            empresa_inadimplente[i].dado4 = empresas[i][3]
            empresa_inadimplente[i].dado5 = empresas[i][4]
            empresa_inadimplente[i].dado6 = empresas[i][5]
            empresa_inadimplente[i].dado7 = empresas[i][6]
            empresa_inadimplente[i].dado8 = empresas[i][7]
            empresa_inadimplente[i].dado9 = empresas[i][8]
            empresa_inadimplente[i].dado10 = empresas[i][9]

        print(empresas)


