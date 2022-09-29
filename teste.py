import webbrowser


web_texto = 'ELETROSUL (TSLE)'
documento = '1153 - ELETROSUL (TSLE)'

if web_texto not in documento:
    print('falhou')
else:
    print('ok')