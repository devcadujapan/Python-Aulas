"""
import os

# Criando um diretorio
os.mkdir('python')

# Caminho Absoluto - Path a partir da raiz
os.mknod('/home/py/Documentos/Python/arquivos/python/olamundo.py')

# Caminho Relativo
os.mknod('./python/compras.txt')

# Exemplo de Forma errada de utilizar o caminho relativo
os.mknod('arquivos/python/compras2.txt')
"""
"""
# Apagando Arquivos
os.remove('teste.txt')
print(os.path.exists('teste.txt'))

# Apagando Diretorio
os.rmdir('pastanova')
"""
"""
# Renomeando Diretorio e Arquivos
import os
os.mknod('olamundo.py')
os.makedirs('nova_pasta')
os.mknod('./nova_pasta/teste.txt')

os.rename('olamundo.py', 'olamundo.txt')
os.rename('olamundo.txt', 'olamundo.psd')
os.rename('nova_pasta', 'documentos')
os.msnod('./documentos/teste.txt')
os.rename('./documentos/teste.txt', './documentos/compras.txt')
"""
