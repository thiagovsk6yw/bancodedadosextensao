-- Create tables
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(50) NOT NULL,
    descricao_pedido TEXT NOT NULL,
    data_pedido DATE NOT NULL,
    status_pedido VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS itens_pedido (
    id SERIAL PRIMARY KEY,
    id_pedido INTEGER NOT NULL,
    descricao_item TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
);

-- Insert data
INSERT INTO pedidos (nome_cliente, descricao_pedido, data_pedido, status_pedido)
VALUES ('Rosiane', 'Picadinho com ovo', '2023-03-10', 'em preparo');

INSERT INTO itens_pedido (id_pedido, descricao_item, quantidade)
VALUES (1, 'Picadinho', 1);

INSERT INTO itens_pedido (id_pedido, descricao_item, quantidade)
VALUES (1, 'Refrigerante', 2);