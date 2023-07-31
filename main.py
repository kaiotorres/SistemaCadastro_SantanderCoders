import json

# Menu e Submenu
menu_str = """
\nBoas vindas ao nosso sistema:

1 - Inserir usuário
2 - Excluir usuário
3 - Atualizar usuário
4 - Informações de um usuário
5 - Informações de todos os usuários
6 - Sair\n
"""

sub_menu_str = """
\nQual informação deseja alterar?
1 - Nome
2 - Telefone
3 - Endereço
\n
"""

def ler_salvar_arquivo(ler=True, nome_arquivo='cadastros.json', cadastros=None):
    if ler:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:  # lembrar de setar o enconding para utf-8
                return json.load(arquivo)
        except FileNotFoundError:
            return {}

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(cadastros, arquivo)

def add_usuario(cadastros, nome, telefone="Não Informado", endereco="Não Informado"):
    for usuario in cadastros.values():
        if usuario['Nome'] == nome and usuario['Telefone'] == telefone and usuario['Endereço'] == endereco and not usuario['Status']:
            usuario['Status'] = True
            return cadastros

    novo_id = 1
    if cadastros:
        novo_id = max(int(key) for key in cadastros) + 1

    novo_usuario = {
        'Status': True,
        'Nome': nome,
        'Telefone': telefone,
        'Endereço': endereco
    }

    cadastros[str(novo_id)] = novo_usuario
    return cadastros

def excluir_usuario(cadastros, *ids):
    for id in ids:
        if str(id) in cadastros:
            cadastros[str(id)]['Status'] = False
        else:
            print(f"Usuário com ID {id} não encontrado!")

    ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)
    return cadastros

def editar_usuario(cadastros, id, campo, novo_valor):
    if str(id) in cadastros:
        if campo == 1:
            cadastros[str(id)]['Nome'] = novo_valor
        elif campo == 2:
            cadastros[str(id)]['Telefone'] = novo_valor
        elif campo == 3:
            cadastros[str(id)]['Endereço'] = novo_valor
    else:
        print(f"Usuário com ID {id} não encontrado!")

    ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)
    return cadastros

def exibir_usuario(cadastros, id):
    if str(id) in cadastros and cadastros[str(id)]['Status']:
        usuario = cadastros[str(id)]
        print(f"Nome: {usuario['Nome']}")
        print(f"Telefone: {usuario['Telefone']}")
        print(f"Endereço: {usuario['Endereço']}")
    else:
        print("Usuário não encontrado!")

def exibir_todos_usuarios(cadastros):
    for usuario_id, usuario in cadastros.items():
        if usuario['Status']:
            print(f"ID: {usuario_id}")
            print(f"Nome: {usuario['Nome']}")
            print(f"Telefone: {usuario['Telefone']}")
            print(f"Endereço: {usuario['Endereço']}")
            print()

def main():
    cadastros = ler_salvar_arquivo()

    while True:
        print(menu_str)
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            n = int(input("Digite o número de cadastros que deseja inserir: "))
            for _ in range(n):
                nome = input("Insira o nome: ")
                telefone = input("Insira o telefone: ")
                endereco = input("Insira o endereço: ")
                cadastros = add_usuario(cadastros, nome, telefone, endereco)
            ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)

        elif opcao == 2:
            ids = [int(id) for id in input("Insira o(s) ID(s) do(s) usuário(s) que deseja excluir (separados por espaço): ").split()]
            cadastros = excluir_usuario(cadastros, *ids)
            ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)

        elif opcao == 3:
            id_usuario = int(input("Insira o ID do usuário que deseja atualizar: "))
            print(sub_menu_str)
            campo = int(input("Digite a opção desejada: "))
            novo_valor = input(f"Insira o novo valor para o campo selecionado: ")
            cadastros = editar_usuario(cadastros, id_usuario, campo, novo_valor)
            ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)

        elif opcao == 4:
            id_usuario = int(input("Insira o ID do usuário que deseja exibir: "))
            exibir_usuario(cadastros, id_usuario)

        elif opcao == 5:
            exibir_todos_usuarios(cadastros)

        elif opcao == 6:
            ler_salvar_arquivo(ler=False, nome_arquivo='cadastros.json', cadastros=cadastros)
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
