def inserir(cursor,nome,valor):
    comando = "INSERT INTO vendas (nome_produto,valor) VALUES(%s,%s)"
    cursor.execute(comando,(nome,valor))
def listar(cursor):
    cursor.execute("SELECT * FROM vendas")
    return cursor.fetchall()
def atualizar(cursor,nome,valor):
    comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"
    cursor.execute(comando,(valor,nome))
def deletar(cursor,idvenda):
    comando = "DELETE FROM vendas WHERE idvendas = %s"
    cursor.execute(comando,(idvenda,))