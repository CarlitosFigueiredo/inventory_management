import psycopg2

# criar conexão

conexao = psycopg2.connect(
    database="",
    user="",
    password=""
    host="",
    port="",
)

print("Conexão com o Banco de dados aberta com sucess!")

# criação do cursor
meu_cursor = conexao.cursor()