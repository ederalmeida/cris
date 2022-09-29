import openpyxl as xlsx

def gravar_log(arquivo, documento, mensagem):
    planilha = xlsx.load_workbook(arquivo)
    aba = planilha.active

    aba.cell(row=documento.linha, column=6).value = mensagem

    planilha.save(arquivo)