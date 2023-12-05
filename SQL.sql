-- Criar tabela CONTATO
DROP TABLE IF EXISTS CONTATO;

CREATE TABLE CONTATO (
  CONTATO_ID VARCHAR(5) NOT NULL PRIMARY KEY,
  TELEFONE_1 VARCHAR (11) NOT NULL,
  EMAIL VARCHAR(50) NULL,
  BAIRRO VARCHAR(50) NULL,
  TELEFONE_2 VARCHAR(11) NULL
);

INSERT INTO CONTATO (CONTATO_ID, TELEFONE_1, EMAIL, BAIRRO, TELEFONE_2) VALUES
('00001', '12345678901', 'email1@example.com', 'Bairro 1', '12345678901'),
('00002', '23456789012', 'email2@example.com', 'Bairro 3', '23456789012'),
('00003', '34567890123', 'email3@example.com', 'Bairro 3', '34567890123'),
('00004', '45678901234', 'email4@example.com', 'Bairro 4', '45678901234'),
('00005', '56789012345', 'email5@example.com', 'Bairro 2', '56789012345'),
('00006', '67890123456', 'email6@example.com', 'Bairro 2', '67890123456'),
('00007', '78901234567', 'email7@example.com', 'Bairro 7', '78901234567'),
('00008', '89012345678', 'email8@example.com', 'Bairro 8', '89012345678'),
('00009', '90123456789', 'email9@example.com', 'Bairro 9', '90123456789'),
('00010', '01234567890', 'email10@example.com', 'Bairro 6', '01234567890'),
('00011', '12345678901', 'email11@example.com', 'Bairro 8', '12345678901'),
('00012', '23456789012', 'email12@example.com', 'Bairro 8', '23456789012'),
('00013', '34567890123', 'email13@example.com', 'Bairro 4', '34567890123'),
('00014', '45678901234', 'email14@example.com', 'Bairro 6', '45678901234'),
('00015', '56789012345', 'email15@example.com', 'Bairro 6', '56789012345'),
('00016', '67890123456', 'email16@example.com', 'Bairro 8', '67890123456'),
('00017', '78901234567', 'email17@example.com', 'Bairro 7', '78901234567'),
('00018', '89012345678', 'email18@example.com', 'Bairro 7', '89012345678'),
('00019', '90123456789', 'email19@example.com', 'Bairro 5', '90123456789'),
('00020', '01234567890', 'email20@example.com', 'Bairro 7', '01234567890');

-- criar tabela PRODUTOS
DROP TABLE IF EXISTS PRODUTO;

CREATE TABLE PRODUTO (
  PRODUTO_ID VARCHAR(5) NOT NULL PRIMARY KEY,
  NOME VARCHAR(50) NOT NULL,
  TIPO VARCHAR(50) NOT NULL,
  VALOR FLOAT NOT NULL
);

INSERT INTO PRODUTO (PRODUTO_ID, NOME, TIPO, VALOR) VALUES
('00001', 'Produto 1', 'Tipo A', 10.0),
('00002', 'Produto 2', 'Tipo B', 7.0),
('00003', 'Produto 3', 'Tipo A', 15.0),
('00004', 'Produto 4', 'Tipo B', 3.0),
('00005', 'Produto 5', 'Tipo B', 20.0);

-- Criar tabela CLIENTES
DROP TABLE IF EXISTS CLIENTES;

CREATE TABLE CLIENTES (
  CPF VARCHAR(11) NOT NULL PRIMARY KEY,
  CONTATO_ID VARCHAR(5) NOT NULL,
  NOME VARCHAR(50) NOT NULL,
  IDADE INT NULL,
  SEXO VARCHAR(1) NULL,
  FOREIGN KEY(CONTATO_ID) REFERENCES CLIENTES(CONTATO_ID)
);

INSERT into CLIENTES(CPF, contato_id, nome, idade, sexo) VALUES 
('16761498724', '00001', 'Patrick', 26, 'm'),('16761498725', '00003', 'Maria', 22, 'f'),
('16761498726', '00004', 'João', 35, 'm'),('16761498727', '00005', 'Ana', 28, 'f'),
('16761498728', '00006', 'Lucas', 19, 'm'),('16761498729', '00007', 'Julia', 31, 'f'),
('16761498730', '00008', 'Pedro', 24, 'm'),('16761498731', '00009', 'Mariana', 27, 'f'),
('16761498732', '00010', 'Rafael', 29, 'm'),('16761498733', '00011', 'Camila', 23, 'f'),
('16761498734', '00012', 'Guilherme', 32, 'm'),('16761498735', '00013', 'Larissa', 25, 'f'),
('16761498736', '00014', 'Fernando', 21, 'm'),('16761498737', '00015', 'Isabela', 33, 'f'),
('16761498738', '00016', 'Thiago', 26, 'm'),('16761498739', '00017', 'Carla', 30, 'f'),
('16761498740', '00018', 'Vinicius', 28, 'm'),('16761498741', '00019', 'Amanda', 24, 'f'),
('16761498742', '00020', 'Gabriel', 31, 'm');

-- criar tabela COMPRAS
DROP TABLE IF EXISTS COMPRAS;

create table COMPRAS (
  COMPRA_ID VARCHAR(5) NOT NULL PRIMARY KEY,
  CPF VARCHAR(11) NOT NULL,
  PRODUTO_ID VARCHAR(5) NOT NULL,  
  QUANTIDADE INT NOT NULL,
  FOREIGN KEY(CPF) REFERENCES CLIENTES(CPF)
  FOREIGN KEY(PRODUTO_ID) REFERENCES PRODUTOS(PRODUTO_ID)
);

INSERT INTO COMPRAS (COMPRA_ID, CPF, PRODUTO_ID, QUANTIDADE) VALUES
('00001', '16761498724', '00001', 1),('00002', '00000000001', '00005', 2),
('00003', '16761498725', '00003', 1),('00004', '16761498726', '00004', 4),
('00005', '16761498727', '00005', 5),('00006', '16761498728', '00003', 6),
('00007', '16761498729', '00004', 2),('00008', '16761498730', '00003', 8),
('00009', '16761498731', '00003', 4),('00010', '16761498732', '00001', 1),
('00011', '16761498733', '00002', 2),('00012', '16761498734', '00002', 2),
('00013', '16761498735', '00001', 4),('00014', '16761498736', '00004', 4),
('00015', '16761498737', '00002', 1),('00016', '16761498738', '00001', 6),
('00017', '16761498739', '00002', 1),('00018', '16761498740', '00001', 8),
('00019', '16761498741', '00003', 1),('00020', '16761498742', '00002', 2);

------------------------------------------------------------------PERGUNTAS INICIAIS

-- Qual produto mais vendido?

select p.nome as 'Produto mais vendido', sum(c.quantidade) as QntTotal
from PRODUTO as p 
inner join COMPRAS as c
on p.PRODUTO_ID = c.produto_id
GROUP by p.produto_id 
order by QntTotal DESC
LIMIT 1;


-- Produto que deu mais renda
select 
	p.nome as 'Produto Com Maior Renda', 
    sum(c.quantidade) AS 'Quantidade Vendida', 
    p.valor as 'Valor Unitario', 
    sum((p.valor*c.quantidade)) as ValorTotal
from PRODUTO as p 
inner join COMPRAS as c
on c.produto_id = p.produto_id
group by c.produto_id
order by ValorTotal DESC
limit 1;

-- Qual bairro trouxe mais renda
SELECT
	Cont.bairro as 'Bairro com maior Renda',
    Prod.nome as 'Nome do Produto',
    Prod.valor as 'Valor Unitario',
    sum(Comp.quantidade) as 'Quantidade de Vendas',
    sum(Prod.valor * Comp.quantidade) as 'ValorTotal'
 from COMPRAS as Comp
 inner JOIN CLIENTES as Clie 
 	on Comp.cpf = Clie.cpf
 inner join CONTATO as Cont 
 	on Cont.contato_id = Clie.contato_id
 inner join PRODUTO as Prod
 	on Comp.produto_id = Prod.produto_id
 group by bairro
 order by ValorTotal desc
 LIMIT 1;

 
 ------------------------------------------------------------------CRIANDO TABELA
 
 -- Criar uma tabela Produto_desconto.
 	-- Sera copia da Tabela PRODUTOS.
    -- Produtos com valor acima de 10 ganharão 20% de desconto.
    -- Exibir comparação do Produto com valor antigo e novo.
    
 DROP TABLE IF EXISTS PRODUTO_DESCONTO;
 
 CREATE TABLE PRODUTO_DESCONTO AS 
 SELECT produto_id, nome, tipo, 
    case 
    	when valor>10 
        then valor*-0.2+valor
        else valor 
    end as valor
 from PRODUTO;
 
 
 select P.nome, p.valor as ValorOriginal, pd.valor as ValorDesconto from PRODUTO p 
 inner join PRODUTO_DESCONTO as pd
 on p.PRODUTO_ID = pd.PRODUTO_ID;
 
 
 
 -- Qual produto teve o maior desconto ?
 select 
 	P.nome, 
 	p.valor as ValorOriginal, 
    pd.valor as ValorDesconto, 
    p.valor-pd.valor as Economia
 from PRODUTO p 
 inner join PRODUTO_DESCONTO as pd
 	on p.PRODUTO_ID = pd.PRODUTO_ID
 order by Economia desc
 limit 1;
 
 
 -- Criar Tabela Produtos_2
 	-- Sera uma copia da tabela produto
    -- a nomeclatura dos tipos sera diferente
drop table if EXISTS PRODUTO_2;

create table PRODUTO_2 AS 
SELECT 
	produto_id, 
    nome, 
	CASE tipo
    	WHEN 'Tipo A' THEN 'BEBIDA'
        WHEN 'Tipo B' THEN 'COMIDA'
        ELSE 'OUTROS'
     END as tipo,
     valor
from PRODUTO;

-- Realizar INSERT de + 3 itens no Produto 2
insert into PRODUTO_2 values 
('00006', 'Produto 6', 'BEBIDA', 10.0),
('00007', 'Produto 7', 'BEBIDA', 7.0),
('00008', 'Produto 8', 'COMIDA', 15.0);

-- Realizar UPDATE EM 2 PRODUTOS do produto_2
UPDATE PRODUTO_2 set valor=15 WHERE produto_id in ('00001','00005','00008');

SELECT * FROM PRODUTO;


-- inserir Valores que existe no produto_2 e nao existe no produto
insert into PRODUTO
  select a.* from PRODUTO_2 as a
    inner join(
      SELECT produto_id FROM PRODUTO_2
      EXCEPT
      SELECT produto_id FROM PRODUTO
    ) as b 
    on a.produto_id = b.produto_id;

 
SELECT * FROM PRODUTO;
 
 
 -- Utilizar Triiger 
   -- Criar uma tabela de ações
   -- A cada nova compra de valor acima de 20 reais
   		-- Adicionar Uma ação na tabela 
        	-- "Mandar um E-mail" 
            
drop table if EXISTS ACOES;

Create TABLE ACOES (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  COMPRA_ID VARCHAR(5) NOT NULL,
  STATUS VARCHAR(10) DEFAULT 'Pendente',
  ACAO VARCHAR(50) not NULL
);

CREATE TRIGGER DEFINIR_ACOES AFTER INSERT ON COMPRAS
FOR EACH ROW 
	WHEN (SELECT VALOR FROM PRODUTO WHERE PRODUTO_ID = new.PRODUTO_ID) * new.quantidade > 50 
BEGIN
	INSERT INTO ACOES (COMPRA_ID, ACAO) VALUES (new.PRODUTO_ID, 'ENVIAR EMAIL');
END;


INSERT INTO COMPRAS (COMPRA_ID, CPF, PRODUTO_ID, QUANTIDADE) VALUES
('10001', '16761498724', '00004', 5), ('20001', '16761498727', '00003', 2), ('30001', '16761498725', '00005', 3);

SELECT * FROM ACOES;





