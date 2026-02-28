from database import conectar
import crud

conexao = conectar()
cursor = conexao.cursor()

while True:
    print("\n====Menu Vendas===")
    print("1 - inserir venda")
    print("2- Listar venda")
    print("3 - Atualizar Venda")
    print("4- Deletar Venda")
    print("5 - sair")

    opcao = input("Digite uma opção: ")
    

    if opcao == "1":
        nome = input("Nome do produto: ")
        valor = int(input("Valor do produto (inteiro) : "))
        crud.inserir(cursor,nome,valor)
        conexao.commit()
        print("Venda Inserida")
    elif opcao == "2":
        vendas = crud.listar(cursor)
        for venda in vendas:
            print(venda)
    elif opcao == "3":
        nome = input("Nome do produto para atualizar: ")
        valor = int(input("Novo valor: "))
        crud.atualizar(cursor,nome,valor)
        conexao.commit()
        print("Atualizado com sucesso!")
    elif opcao == "4":
        idvenda = int(input("Id da venda: "))
        crud.deletar(cursor,idvenda)
        conexao.commit()
        print("Venda deletada!")
    elif opcao == "5":
        print("Fechando..")
        break
    else:
        print("opcao invalida")

cursor.close()
conexao.close()