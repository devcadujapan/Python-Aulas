import requests

link = 'https://minhaapi.cadujapan.repl.co/extrairvendas'

requisicao = requests.get(link)

print(requisicao)

print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['total_vendas'])
