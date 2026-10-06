from conectar import conexao, meu_cursor

if __name__ == '__main__': 

    meu_cursor.execte('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
            CODIGO SERIAL PRIMARY KEY,
            NOME VARCHAR(100) NOT NULL,
            PRECO NUMERIC(10, 2) NOT NULL
        );
    ''')

    #just in case
    conexao.commit()
    print("Tabela criada com sucesso")

    meu_cursor.close
    conexao.close