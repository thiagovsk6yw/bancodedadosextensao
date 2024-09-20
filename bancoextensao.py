import psycopg2
from psycopg2 import Error

# Conexão com o banco de dados
def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname="sistema_pedidos",
            user="seu_usuario",
            password="sua_senha",
            host="localhost",
            port="5432"
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Criar tabelas no banco de dados
def criar_tabelas(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            nome_cliente VARCHAR(50) NOT NULL,
            descricao_pedido TEXT NOT NULL,
            data_pedido DATE NOT NULL,
            status_pedido VARCHAR(20) NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS itens_pedido (
            id SERIAL PRIMARY KEY,
            id_pedido INTEGER NOT NULL,
            descricao_item TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
        );
    """)
    conn.commit()

# Inserir pedido no banco de dados
def inserir_pedido(conn, nome_cliente, descricao_pedido, data_pedido):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO pedidos (nome_cliente, descricao_pedido, data_pedido, status_pedido)
        VALUES (%s, %s, %s, 'em preparo');
    """, (nome_cliente, descricao_pedido, data_pedido))
    conn.commit()

# Inserir item do pedido no banco de dados
def inserir_item_pedido(conn, id_pedido, descricao_item, quantidade):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO itens_pedido (id_pedido, descricao_item, quantidade)
        VALUES (%s, %s, %s);
    """, (id_pedido, descricao_item, quantidade))
    conn.commit()

# Obter pedidos em ordem de preparo
def obter_pedidos_em_preparo(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM pedidos
        WHERE status_pedido = 'em preparo'
        ORDER BY data_pedido ASC;
    """)
    return cur.fetchall()

# Exemplo de uso
conn = conectar_banco()
criar_tabelas(conn)

inserir_pedido(conn, "Rosiane", "Picadinho com legumes", "2023-03-10")
inserir_item_pedido(conn, 1, "Picadinho com legumes", 1)
inserir_item_pedido(conn, 1, "Refrigerante", 2)

pedidos_em_preparo = obter_pedidos_em_preparo(conn)
for pedido in pedidos_em_preparo:
    print(pedido)

conn.close()