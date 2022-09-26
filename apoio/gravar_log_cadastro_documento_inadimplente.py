import openpyxl as xlsx

def gravar_logo(arquivo, documento):
    planilha = xlsx.load_workbook(arquivo)
    aba = planilha.active

    aba.cell(row=documento.linha, column=6).value = 'Inadimplência Cadastrada'

    planilha.save(arquivo)