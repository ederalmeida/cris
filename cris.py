from janelas import janela_abertura as ja
import logging

while True:
    logging.basicConfig(filename='log_file.txt', \
                        level=logging.DEBUG,\
                        format='%(asctime)s :: %(levelno)s :: %(lineno)d :: %(message)s')
    logging.info('ROBO INICIADO')
    ja.inicializacao()