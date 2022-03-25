""""
import os

# Verificando qual sistema operacional estou usando
# posix - para Linux e MacOS, NT - para Windows
print(os.name)
"""

import os

# Verificar se um arquivo existe
print(os.path.exists('texto.py'))
print(os.path.exists('PYTHON/AulaFaces.py'))

# Verifica se um diretorio existe
print(os.path.exists('PYTHON'))
print(os.path.exists('teste'))

"""
# Criando um diretorio
os.mkdir('Testando')

# Criando um arquivo
os.mknod('arquivo.py')
"""
