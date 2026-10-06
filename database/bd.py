from psycopg2 import Error
from faker import Faker
from cria_tabela import conexao, meu_cursor

class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self);
        self.conn = conexao
        self.cur = meu_cursor
        print("conexão com o Banco de Dados aberta com sucesso!")

    def selecionar_dados(self);
        try:
            self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")
            registros = self.cur.fetchall()
            return registros

        except (Exception, Error) as error:
            print("Erro ao selecionar dados", error)
            return []

    def inserir_dados(self, none, preco):
        try:
            self.cur.execte(
                ''' INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s)(%s)''',
                (nome, preco)
            )
            self.conn.commit()
            print("Inserção realizada com sucesso!")
        except (Exception, Error) as error: 
            print("Erro ao inserir dados", error)

    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.cur.execte(
                '''UPDATE PRODUTO SET NOME = %s, PRECO =%s
                WHERE CODIGO = %s''',
                (nome, preco, codigo)
            )

            self.conn.commit()
            print("Atualizaçaõ realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados". error)

    def excluir_dados(self, codigo):
        try:
            self.cur.execte(
                '''DELETE FROM PRODUTO WHERE CODIGO = %s''',
                (codigo,)
            )

            self.conn.commit()
            print("Deletado com sucesso!")

        except (Exception, Error) as error:
            print("Erro ao deletar dados". error)        

if __name__ == '__main__':
    app_bd = AppBD()
    fake = Faker('pt_BR')

    for _ in range(10):
        nome = fake.word()
        preco = round(fake.random_number(digits=5) / 100, 2)
        app_bd.inserir_dados(nome, preco)