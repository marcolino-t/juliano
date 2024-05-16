from class_bancodados import BancoDados
from class_cliente import Cliente
def cadastrar_clientes():
     nome = input('Digite o nome do cliente: ')
     email = input('Digite o email do cliente: ')
     telefone = input('Digite o telefone do cliente: ')
     novo_cliente = Cliente(nome,email, telefone)
     BancoDados.inserir_cliente(novo_cliente)
     print('Cliente cadastrada com sucesso')

def listar_clientes():
     clientes = BancoDados.listar_clientes()
     for cliente in clientes:
          print(f'ID: {cliente[0]} | NOME: {cliente[1]} | EMAIL: {cliente[2]} | TELEFONE: {cliente[3]}')

def atualizar_cliente():
     cliente_id = int(input('Digite o Id do cliente a ser atualizado: '))
     novo_nome = input('Digite o novo nome do cliente: ')
     novo_email = input('Digite o novo email do cliente: ')
     novo_telefone = input('Digite o novo telefone do cliente: ')
     cliente_atualizado  = Cliente(cliente_id,novo_nome,novo_email,novo_telefone)
     Banco_Dados.atualizar_clientes(cliente_atualizado,cliente_id)
     print('Cliente atualizado com sucesso!')

def deletar_cliente():
     cliente_id = int(input('Digite o id do cliente a ser deletado: '))
     BancoDados.deletar_cliente(cliente_id)
     print('Cliente deletado com sucesso!')

# Exemplo de Execução

Banco_Dados = BancoDados()

while True:
     print("\nMenu Principal: ")
     print("1. Cadastrar Cliente")
     print("2. Listar Cliente")
     print("3. Atualizar Cliente")
     print("4. Deletar Cliente")
     print("0. Sair")

     opcao = input("Digite a opção desejada: ")

     if opcao == '1':
          cadastrar_clientes()
     elif opcao == '2':
          listar_clientes()
     elif opcao =='3':
          atualizar_cliente()
     elif opcao =='4':
          deletar_cliente()
     elif opcao =='0':
          break
     else:
          print('Opção inválida.')

