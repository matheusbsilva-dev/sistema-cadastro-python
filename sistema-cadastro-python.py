usuarios = []


def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    usuario = {"nome": nome, "idade": idade}
    usuarios.append(usuario)

    print("Usuário cadastrado!")


def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, u in enumerate(usuarios):
        print(f"{i} - Nome: {u['nome']} | Idade: {u['idade']}")


def deletar():
    listar()
    indice = int(input("Digite o índice para deletar: "))

    if 0 <= indice < len(usuarios):
        usuarios.pop(indice)
        print("Usuário removido!")
    else:
        print("Índice inválido")


while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Deletar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        deletar()
    elif opcao == "0":
        break
    else:
        print("Opção inválida")