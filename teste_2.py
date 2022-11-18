from urllib.request import urlopen
import json
import csv

url_datetime = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
response = urlopen(url_datetime)
data_json = json.loads(response.read())

print(data_json['datetime'])  

with open ('teste.csv', 'a', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow([data_json['datetime'] + ';' + 'teste'])
arquivo.close()