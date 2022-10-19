import cx_Freeze
from apoio import versao_atual as versao
import hashlib
import os.path

build_exe_options = {
'include_msvcr': True
}

exe = [cx_Freeze.Executable('cris.py',
                            base = 'Win32GUI',
                            target_name = 'cris.exe',
                            icon='imagens\cris.ico')]

cx_Freeze.setup(name = 'cris',
                version=versao.v,
                options = {'build_exe': build_exe_options},
                executables = exe
)

'''
Calculo de Hash para as pastas que não são oriundas do python
para verficação de atualização de versão
'''
BUF_SIZE = 524288
sha1 = hashlib.sha1()
lista_paths_por_pasta = []
lista_path_hash_por_arquivo = []
lista_pastas =['apoio',
               'classes',
               'imagens',
               'janelas',
               'robos',
               ]

for pasta in lista_pastas:
    for address, dirs, files in os.walk(os.path.join('build', 'exe.win-amd64-3.10', 'lib', pasta)):
        for name in files:
            lista_paths_por_pasta.append(os.path.join(address, name))

for path in lista_paths_por_pasta:
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
            lista_path_hash_por_arquivo.append([path, sha1.hexdigest()])
    f.close()

with open(os.path.join('build', 'exe.win-amd64-3.10', 'lib', 'hash_versoes.txt'), 'w') as hash:
    for linha in lista_path_hash_por_arquivo:
        novo_path = linha[0].replace(os.path.join('build', 'exe.win-amd64-3.10', 'lib'), 'lib')
        hash.writelines(novo_path + ";" + linha[1] + '\n')
hash.close()
