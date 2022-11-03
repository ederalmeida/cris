from janelas import janela_abertura as ja
from janelas import janela_update as ju
from apoio import update as up

atualizar = up.check_update()

if atualizar == "Yes":
    ju.exibir()

while True:
    ja.exibir()