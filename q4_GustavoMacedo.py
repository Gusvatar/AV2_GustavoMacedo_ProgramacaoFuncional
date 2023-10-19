import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conexao.cursor()

criar_usuarios = """
CREATE TABLE IF NOT EXISTS USUARIOS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    console VARCHAR(255)
)
"""

criar_jogos = """
CREATE TABLE IF NOT EXISTS JOGOS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    data_lancamento DATE
)
"""

criar_database = lambda nome: cursor.execute("CREATE DATABASE " + nome + ";")
usar_database = lambda nome: cursor.execute("USE " + nome + ";")
criar_database("mydatabase")
usar_database("mydatabase")

cursor.execute(criar_usuarios)
cursor.execute(criar_jogos)


inserir_usuario = lambda nome, console: cursor.execute("INSERT INTO USUARIOS (nome, console) VALUES (%s, %s)", (nome, console))
remover_usuario = lambda user_id: cursor.execute("DELETE FROM USUARIOS WHERE id = %s", (user_id,))
consultar_usuarios = lambda: [print(row) for row in cursor.fetchall()]


inserir_jogo = lambda nome, data_lancamento: cursor.execute("INSERT INTO JOGOS (nome, data_lancamento) VALUES (%s, %s)", (nome, data_lancamento))
remover_jogo = lambda jogo_id: cursor.execute("DELETE FROM JOGOS WHERE id = %s", (jogo_id,))
consultar_jogos = lambda: [print(row) for row in cursor.fetchall()]


inserir_usuario("Gustavo", "Gamecube")
conexao.commit()

inserir_usuario("Felipe", "Switch")
conexao.commit()

inserir_jogo("The Legend of Zelda: The Wind Waker", "2002-12-13")
conexao.commit()

inserir_jogo("Pikmin 4", "2023-07-21")
conexao.commit()


cursor.execute("SELECT * FROM USUARIOS")
consultar_usuarios()


cursor.execute("SELECT * FROM JOGOS")
consultar_jogos()

#Terminar a conexão quando terminar de utilizar
conexao.close()