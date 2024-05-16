import _mysql_connector
class BancoDados:
     def __init__(self):
          self.conexao = _mysql_connector.connector(host='127.0.0.1',user='root',passwd = 'root',database = 'poo' )
          self.cursor = self.conexao.cursor()
          #cria a tabela 'clientes' se não existir
          self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    telefone TEXT NOT NULL
               )
          """ )
     def inserir_cliente(self, cliente):
          self.cursor.execute("""
               INSERT INTO clientes (nome, email, telefone)
               VALUES(%s,%s,%s)
          """,(cliente.nome,cliente.email,cliente.telefone))
          self.conexao.commit()
     
     def listar_clientes(self):
          self.cursor.execute("""
               SELECT id, nome,email,telefone FROM clientes
          """)
          return self.cursor.fetchall()
     
     def atualizar_clientes(self,cliente,cliente_id):
          self.cursor.execute("""
          UPDATE clientes SET
               nome= %s,
               email= %s,
               telefone= %s
          where id =%s
          """, (cliente.nome,cliente.email,cliente.telefone,cliente_id))
          self.conexao.commit()
     
     def deletar_cliente(self,cliente_id):
          self.cursor.execute(""" 
               DELETE FROM clientes WHERE id = %s
          """, (cliente_id,))
          self.conexao.commit()