-- =====================================================================
-- BANCO DE DADOS: SISTEMA DE BIBLIOTECA UNIVERSITÁRIA
-- =====================================================================
-- 
-- PASSO 1: No PostgreSQL (pgAdmin ou terminal psql), crie o banco:
-- CREATE DATABASE biblioteca_universitaria;
-- 
-- PASSO 2: Conecte-se ao banco 'biblioteca_universitaria' e rode o código abaixo:
-- =====================================================================

-- 1. Criação da Tabela AUTOR
-- Guarda quem escreveu os livros (id, nome, nacionalidade)
CREATE TABLE IF NOT EXISTS autor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(100) NOT NULL
);

-- 2. Criação da Tabela LIVRO
-- Guarda as informações do livro e quem o escreveu (id_autor)
-- id_autor se conecta com a tabela autor(id)
CREATE TABLE IF NOT EXISTS livro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    ano_publicacao INT NOT NULL,
    id_autor INT NOT NULL,
    CONSTRAINT fk_livro_autor FOREIGN KEY (id_autor) REFERENCES autor(id) ON DELETE CASCADE
);

-- =====================================================================
-- DADOS DE TESTE (OPCIONAL): Se quiser testar o sistema já com dados
-- =====================================================================
-- INSERT INTO autor (nome, nacionalidade) VALUES ('Machado de Assis', 'Brasileira');
-- INSERT INTO autor (nome, nacionalidade) VALUES ('George Orwell', 'Britânica');
-- INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES ('Dom Casmurro', 1899, 1);
-- INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES ('1984', 1949, 2);
