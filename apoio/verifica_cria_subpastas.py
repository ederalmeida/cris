import os
import logging


def winapi_path(dos_path, encoding=None):
    if (not isinstance(dos_path, str) and encoding is not None): 
        dos_path = dos_path.decode(encoding)
    path = os.path.abspath(dos_path)
    if path.startswith(u"\\\\"):
        return u"\\\\?\\UNC\\" + path[2:]
    return u"\\\\?\\" + path


def verifica_cria_subpastas(caminho_pasta, conta):
    pastas = os.listdir(caminho_pasta)

    '''Verfica se existe uma pasta que comece com os 10 dígitos da conta
        Se existir, utilizar ela e verifica se existe as subpastas print e relatórios
        Se não existirem, serão criadas. '''
    for pasta in pastas:
        if  os.path.isdir(os.sep.join([caminho_pasta, pasta])):
            if str(pasta[0:10]) == str(conta):
                if not os.path.isdir(os.sep.join([caminho_pasta, pasta, 'prints'])):
                    os.makedirs(os.sep.join([caminho_pasta, pasta, 'prints']).replace('\\','/'))
                    logging.info(os.sep.join([caminho_pasta, pasta, 'prints']).replace('\\','/'))
                if not os.path.isdir(os.sep.join([caminho_pasta, pasta, 'relatorios'])):
                    os.makedirs(os.sep.join([caminho_pasta, pasta, 'relatorios']).replace('\\','/'))
                    logging.info(os.sep.join([caminho_pasta, pasta, 'relatorios']).replace('\\','/'))
                return os.sep.join([caminho_pasta, pasta]).replace('\\','/')

    ''' Se passou por todas as pastas e não achou nenhuma que comece com os 10 dígitos
        da conta, então cria a pasta e as subpastas print e relatorios'''
    os.makedirs(os.sep.join([caminho_pasta, conta]).replace('\\','/'))
    logging.info(os.sep.join([caminho_pasta, conta]).replace('\\','/'))
    os.makedirs(os.sep.join([caminho_pasta, conta, 'prints']).replace('\\','/'))
    logging.info(os.sep.join([caminho_pasta, conta, 'prints']).replace('\\','/'))
    os.makedirs(os.sep.join([caminho_pasta, conta, 'relatorios']).replace('\\','/'))
    logging.info(os.sep.join([caminho_pasta, conta, 'relatorios']).replace('\\','/'))
    return os.sep.join([caminho_pasta, conta]).replace('\\','/')

def verifica_pasta_print_rels(caminho_pasta, rel):
    if not os.path.isdir(os.sep.join([caminho_pasta, rel, 'prints'])):
        os.makedirs(os.sep.join([caminho_pasta, rel, 'prints']).replace('\\','/'))
    if not os.path.isdir(os.sep.join([caminho_pasta, rel, 'relatorios'])):
        os.makedirs(os.sep.join([caminho_pasta, rel, 'relatorios']).replace('\\','/'))
    return os.sep.join([caminho_pasta, rel]).replace('\\','/')