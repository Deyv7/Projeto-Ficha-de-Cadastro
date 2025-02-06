import sqlite3 as lite

# Função para conectar ao banco de dados
def conectar():
    con = lite.connect('banco.db')
    return con

# Função para criar a tabela, se não existir
def criar_tabela():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS formulario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        dia_em DATE,
        estado TEXT,
        assunto TEXT
    )
    """)
    con.commit()
    con.close()

# Função para mostrar as informações da tabela "formulario"
def mostrar_info():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM formulario")
    dados = cur.fetchall()  # Pega todos os registros
    con.close()
    return dados

# Função para inserir dados na tabela "formulario"
def inserir_info(lista):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)", lista)
    con.commit()  # Confirma a inserção no banco
    con.close()

# Função para atualizar os dados na tabela "formulario"
def atualizar_info(lista):
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        UPDATE formulario
        SET nome = ?, email = ?, telefone = ?, dia_em = ?, estado = ?, assunto = ?
        WHERE id = ?
    """, lista[1:] + [lista[0]])  # Passa os valores, incluindo o ID
    con.commit()  # Confirma a atualização no banco
    con.close()

# Função para deletar dados da tabela "formulario"
def deletar_info(valor_id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM formulario WHERE id = ?", valor_id)
    con.commit()  # Confirma a exclusão no banco
    con.close()

# Chame essa função uma vez para garantir que a tabela exista
criar_tabela()


