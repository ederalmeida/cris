import PySimpleGUI as sg
import sys
from janelas import janela_abertura as ja
from janelas import janela_update as ju
from apoio import update as up

atualizar = up.check_update()

if atualizar == "Yes":
    ju.exibir()
    sg.popup('Seu software foi atualizado e irá se encerrar. Por favor, abra-o novamente.')
    sys.exit()

while True:
    ja.exibir()