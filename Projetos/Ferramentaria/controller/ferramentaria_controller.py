import sqlite3

def connect_db():
    """Conecta ao banco de dados SQLite e ativa foreign keys."""
    conn = sqlite3.connect('ferramentaria.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def criar_banco():
    """Cria as tabelas ferramentas, pessoas e emprestimos, seguindo as três formas normais."""
    with connect_db() as conn:
        cursor = conn.cursor()

        # Tabela de ferramentas (1FN e 2FN garantidas)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ferramentas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                codigo TEXT UNIQUE NOT NULL,
                descricao TEXT,
                disponivel INTEGER DEFAULT 1
            )
        ''')

        # Tabela de pessoas (3FN - remoção de dependência transitiva)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')

        # Tabela de empréstimos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_ferramenta INTEGER NOT NULL,
                id_pessoa INTEGER NOT NULL,
                data_emprestimo TEXT NOT NULL,
                data_devolucao TEXT,
                FOREIGN KEY (id_ferramenta) REFERENCES ferramentas(id),
                FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
            )
        ''')

        conn.commit()

if __name__ == '__main__':
    criar_banco()
    print("Banco de dados criado com sucesso, de acordo com as três formas normais.")

