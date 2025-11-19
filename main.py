# Lista de funcionários
funcionarios = []

def adicionar_funcionario():
    print("\n--- Adicionar Funcionário ---")
    nome = input("Nome do funcionário: ")
    salario = float(input("Salário do funcionário: "))
    
    funcionario = {"nome": nome, "salario": salario}
    funcionarios.append(funcionario)
    
    print(f"Funcionário {nome} adicionado com sucesso!")


def listar_funcionarios():
    print("\n--- Lista de Funcionários ---")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    for f in funcionarios:
        print(f"Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")


def buscar_por_nome():
    print("\n--- Buscar Funcionário por Nome ---")
    nome = input("Digite o nome: ")

    encontrados = [f for f in funcionarios if f["nome"].lower() == nome.lower()]
    
    if encontrados:
        for f in encontrados:
            print(f"Nome: {f['nome']} | Salário: R$ {f['salario']:.2f}")
    else:
        print("Nenhum funcionário com esse nome foi encontrado.")


def calcular_media_salarial():
    print("\n--- Média Salarial ---")
    if not funcionarios:
        print("Não há funcionários cadastrados.")
        return
    
    media = sum(f["salario"] for f in funcionarios) / len(funcionarios)
    print(f"Média salarial: R$ {media:.2f}")

while True:
    print("\n----- MENU -----")
    print("1 - Adicionar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Buscar Funcionário por Nome")
    print("4 - Calcular Média Salarial")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_funcionario()
    elif opcao == "2":
        listar_funcionarios()
    elif opcao == "3":
        buscar_por_nome()
    elif opcao == "4":
        calcular_media_salarial()
    elif opcao == "5":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
