# Coleção de Robôs para Geração de IPEs

##### Desenvolvido por Éder Almeida (eder.almeida@cgteletrosul.com.br - eder.almeida@gmail.com)
##### Apoio e colaboração de Thiago Paes (https://github.com/mrprompt - mrprompt@gmail.com)


## Apresentação
Este robô foi criado com o intuíto de extrarir, em formato xlsx. relatórios do ERP SAP via transção FBL3N, ao mesmo tempo em que faz screenshots do processo.

## Utilização do robô

Para utilizar, basta baixar o arquivo compactado (".zip") no menu "Releases" ao lado, extrair em uma pasta, e dar um duplo clique no arquivo executável (".exe").

Caso queira gerar seu próprio executável, clonar o repositório (ou baixar o Source code) e executar os comandos abaixo (é necessário ter o python instalado).

```console
pip install -r requirements.txt
python setup.py build
```

## Agradecimento
Agradeço ao Fabio Mitsueda (https://fabiomitsueda.com.br) pela liberação da macro criada em VBA por ele, que auxilia no processo de conexão com o SAP, a qual fiz um port para esse projeto.
