import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ca@2528CA',
    database='bdyoutube',
)

cursor = conexao.cursor()

# CRUD

# CREATE
"""
nome_produto = "Chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}",{valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados
cursor.close()
conexao.close()
"""
# READ
"""
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)
cursor.close()
conexao.close()
"""
# UPDATE
"""
nome_produto = "Todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()
"""
# DELETE
"""
nome_produto = "Todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados
cursor.close()
conexao.close()
"""
