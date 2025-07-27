#Lista de contatos usando dicionários em Python.

import os

contatos = {}

while True:
    os.system("clear")
    print("="*30)
    print("Lista de contatos.")
    print("1. Adicionar contato.\n2. Buscar contato por nome.\n3. Remover contato pelo nome.\n4. Sair")
    print("="*30)

    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        nome_contato = input("Digite o nome do contato a ser adicionado: ").lower()
        telefone_contato = input("Digite o telefone a ser adicionado: ")
        contatos[nome_contato] = telefone_contato
    elif opcao == "2":
        nome = input("Digite o nome do contato: ").lower()
        if nome in contatos:
            telefone = contatos[nome]
            print(f"Nome do contato: {nome}, número: {telefone}")
        else:
            print("Contato não encontrado!")
    
    elif opcao == "3":
        nome = input("Digite o nome do contato para remover: ").lower()
        if nome in contatos:
            contatos.pop(nome)
            print(f'Contato "{nome}" removido com sucesso.')
        else:
            print(f'Contato "{nome}" não encontrado.')

    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")
        
    input("Digite <enter> para continuar.")