import os
import shutil
from urllib import request
from zipfile import ZipFile

path = os.getcwd()


if os.path.isdir(os.sep.join([path, 'tmp'])):
    shutil.rmtree(os.sep.join([path, 'tmp']))
else:
    os.makedirs(os.sep.join([path, 'tmp']))

url = 'https://robocris.000webhostapp.com/cris/cris.zip'

file = 'cris.zip'

z = request.urlretrieve(url, file)

extracao_zip = ZipFile(z[0], 'r')
extracao_zip.extractall(os.sep.join([path, 'tmp']))
extracao_zip.close()
shutil.rmtree(os.sep.join([path, 'tmp']))
os.remove(path + '\\cris.zip')
