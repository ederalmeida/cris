# SGPMR Carga

Carga automática de dados no SGPMR.

## Configuração
Crie um ".env" contendo:
```
LOGIN_PAGE=
BASE_PAGE=
USERNAME=
PASSWORD=
EXCEL_FOLDER=
```
Onde:
* LOGIN_PAGE: página de login do SGPMR
* BASE_PAGE: página inicial da listagem de obras
* USERNAME: login válido na plataforma
* PASSWORD: senha do login
* EXCEL_FOLDER: pasta local onde estão armazenadas as planilhas com os dados

## Requisitos
Os requisitos estão no arquivo "requirements.txt". Instale com:
```
pip install -r requirements.txt
```

## Execução
O pacote "sgpmr" contem tudo necessário para fazer
as cargas. Existe um arquivo básico "base.py" e para cada
tipo de equipamento (pasta "tipos") você pode criar uma classe
herdando da básica e customizando onde necessitar.

Você pode, então, alterar o arquivo "start.py" para rodar a
carga.