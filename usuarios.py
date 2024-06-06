import json
import os
import main
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')

def adicionar_usuario(nome, idade, email, cpf):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    cpf = cpf.replace(".", "").replace("-", "")

    if main.jaExisteUsuario(cpf):
        print("Já existe um usuário cadastrado com esse CPF")
        return

    usuarios.append({'nome': nome, 'idade': idade, 'email': email, 'cpf' : cpf})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)

    print("CLIENTE ADICIONADO COM SUCESSO!")

def atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_email, novo_cpf):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    novo_cpf = novo_cpf.replace(".", "").replace("-", "")
    cpf_antigo = cpf_antigo.replace(".", "").replace("-", "")

    if main.jaExisteUsuario(novo_cpf):
        print("Já existe um usuário com esse novo cpf")
        return

    for usuario in usuarios:
        if usuario['cpf'] == cpf_antigo:
            if novo_nome != "":
                usuario['nome'] = novo_nome
            if nova_idade != "":
                usuario['idade'] = int(nova_idade)
            if novo_email != "":
                usuario['email'] = novo_email
            if novo_cpf != "":
                usuario['cpf'] = novo_cpf
            break

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)

    print("CLIENTE ATUALIZADO COM SUCESSO!")
    

def listar_usuarios():
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    if usuarios:
        print("=" *50)
        print("| LISTA DE CLIENTES | ")
        print("-" *50)
        for usuario in usuarios:
            print("*" *50)
            print(f"NOME: {usuario['nome']}\nIDADE: {usuario['idade']}\nEMAIL: {usuario['email']}\nCPF: {usuario['cpf']}")
            print("+" *50)
          
    else:
        print("NÃO HÁ NENHUM CLIENTE CADASTRADO!")

def excluir_usuario(cpf):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    cpf = cpf.replace(".", "").replace("-", "")

    for usuario in usuarios:  
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
        print("CLIENTE EXCLUÍDO COM SUCESSO!")

def buscar_usuario (cpf):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    cpf = cpf.replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(f"NOME: {usuario['nome']}\nIDADE: {usuario['idade']}\nEMAIL: {usuario['email']}\nCPF: {usuario['cpf']}")
            return
    
    print("NÃO HÁ NENHUM CLIENTE CADASTRADO COM ESSE CPF! POR FAVOR, TENTE NOVAMENTE!")
    

def exibir_menu():
    print("\nSEJA BEM-VINDO(A) AO ESPAÇO DO CLIENTE!  QUAL DOS SERVIÇOS ABAIXO VOCÊ DESEJA?:\n")
    print(" | 1 -->    ADICIONAR CADASTRO DE CLIENTE       <-- |")
    print(" | 2 -->     ATUALIZAR CLIENTE CADASTRADO       <-- |")
    print(" | 3 -->      EXIBIR CADASTRO DO CLIENTE        <-- |")
    print(" | 4 -->     LISTAR CLIENTES CADASTRADOS        <-- |")
    print(" | 5 -->     EXCLUIR CLIENTE CADASTRADO         <-- |")
    print(" | 6 -->      VOLTAR AO MENU ANTERIOR           <-- |\n")

def maioridade(idade):
    if(idade <= 17):
        print(" ---> O CADASTRO DEVE SER FEITO POR UMA PESSOA MAIOR DE IDADE! <--- ")
        return False
    else:
        return True

def moduloUsuarios():
    while True: 
        exibir_menu()
        opcao = input("INSIRA O NÚMERO DA SUA ESCOLHA:\n ---> ")

        if opcao == "1":
            nome = input(" INSIRA O NOME:\n ---> ")
            idade = int(input(" INSIRA A IDADE:\n ---> "))
            if maioridade(idade):
                email = input("INSIRA O EMAIL: \n ---> ")
                cpf = input("INSIRA O CPF (SOMENTE NÚMEROS):\n ---> ")
                adicionar_usuario(nome, idade, email, cpf)
            
        elif opcao == "2":
            cpf_antigo = input("INSIRA O CPF A SER ATUALIZADO:\n ---> ")

            if not main.jaExisteUsuario(cpf_antigo):
                continue

            print("DIGITE OS NOVOS DADOS (deixe vazio para manter o atual):")
            novo_nome = input("Novo nome: ")
            nova_idade = input("Nova idade: ")
            novo_email = input("Novo e-mail: ")
            novo_cpf = input("Novo CPF: ")
            
            atualizar_usuario(cpf_antigo, novo_nome, nova_idade, novo_email, novo_cpf)

        elif opcao == "3":
            cpf = input("INSIRA O CPF DO CLIENTE (SOMENTE NÚMEROS):\n ---> ")
            buscar_usuario(cpf)

        elif opcao == "4":
            listar_usuarios()

        elif opcao == "5":
            cpf = input("INSIRA O CPF DO CLIENTE A SER EXCLUÍDO:\n ---> ")
            excluir_usuario(cpf)

        elif opcao == "6":
            print("VOLTANDO AO MENU ANTERIOR...\n")
            sleep(1)
            break

        else:
            print(" --> 😭 OPÇÃO INVÁLIDA. TENTE NOVAMENTE! 😭 <--")