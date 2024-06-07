import json
import os
import main
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'reservas.json')

def adicionarReserva(cpf_cliente, cliente, restaurante, mesa, data, horario):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)
    
    if not main.jaExisteRestaurante(restaurante):
        print("O restaurante informado não existe")
        return

    for reserva in reservas:
        if reserva['restaurante'] == restaurante and reserva['mesa'] == mesa and reserva['data'] == data and reserva['horario'] == horario:
            print("Já existe uma reserva para essa mesa, nesse mesmo dia e horário.")
            return

    reservas.append({
        'cpf_cliente': cpf_cliente,
        'cliente': cliente,
        'restaurante': restaurante,
        'mesa': mesa,
        'data': data,
        'horario': horario
    })

    with open(arquivo, 'w') as f:
        json.dump(reservas, f, indent=4)

    print("Reserva criada com sucesso.")

def buscarReserva(cpf_cliente):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    cpf_cliente = cpf_cliente.replace(".", "").replace("-", "")

    for reserva in reservas:
        if reserva['cpf_cliente'] == cpf_cliente:
            print("-" * 50)
            print(f"Reserva para: {reserva['cliente']}\nEm: {reserva['restaurante']} às {reserva['horario']}\nData: {reserva['data']}\nMesa: {reserva['mesa']}")
            print("-" * 50)
            return
        
    print("Nenhuma reserva encontrada para este cliente.")

def listarReservas():
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for reserva in reservas:
        print("-" * 50)
        print(f"Reserva para: {reserva['cliente']}\nEm: {reserva['restaurante']} às {reserva['horario']}\nData: {reserva['data']}\nMesa: {reserva['mesa']}")
        print("-" * 50)

def atualizarReserva(cpf_cliente, novo_cpf_cliente, novoCliente, novoRestaurante, novaMesa, novaData, novoHorario):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    cpf_cliente = cpf_cliente.replace(".", "").replace("-", "")

    for reserva in reservas:
        if reserva['cpf_cliente'] == cpf_cliente:
            if novo_cpf_cliente != "":
                reserva['cpf_cliente'] = novo_cpf_cliente
            if novoCliente != "":
                reserva['cliente'] = novoCliente
            if novoRestaurante != "":
                reserva['restaurante'] = novoRestaurante
            if novaMesa != "":
                novaMesa = int(novaMesa)
                reserva['mesa'] = novaMesa
            if novaData != "":
                reserva['data'] = novaData
            if novoHorario != "":
                reserva['horario'] = novoHorario

    with open(arquivo, 'w') as f:
        json.dump(reservas, f, indent=4)

    print("Reserva atualizada com sucesso.")

def excluirReserva(cpf_cliente):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    cpf_cliente = cpf_cliente.replace(".", "").replace("-", "")

    for reserva in reservas:
        if reserva['cpf_cliente'] == cpf_cliente:
            reservas.remove(reserva)

    with open(arquivo, 'w') as f:
        json.dump(reservas, f, indent=4)

def temReserva(cpf_cliente):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    cpf_cliente = cpf_cliente.replace(".", "").replace("-", "")

    for reserva in reservas:
        if reserva['cpf_cliente'] == cpf_cliente:
            return True
    return False

def exibirMenu():
    print("=" * 21, " MENU ", "=" * 21)
    print("\t[1]\tAdicionar Reserva")
    print("\t[2]\tListar Reservas")
    print("\t[3]\tAtualizar Reserva")
    print("\t[4]\tExcluir Reserva")
    print("\t[5]\tListar uma Reserva")
    print("\t[6]\tVOLTAR AO MENU INICIAL")
    print("=" * 50)

def moduloReservas():
    while True:
        exibirMenu()
        opcao = int(input(">>> "))
        
        match(opcao):
            case 1:
                cliente = input("Nome do cliente: ")
                cpf_cliente = input("Digite o CPF do cliente: ")
                cpf_cliente = cpf_cliente.replace(".", "").replace("-", "")

                if not main.jaExisteUsuario(cpf_cliente):
                    print("Este usuário não existe, não é possível fazer a reserva")
                else:
                    restaurante = input("Nome do restaurante: ")
                    if not main.jaExisteRestaurante(restaurante):
                        print("Este restaurante não existe, não é possível fazer a reserva")
                    else:
                        mesa = int(input("Mesa nº: "))
                        data = input("Data (DD/MM/AAAA): ")
                        horario = input("Horário (ex.: 19h): ")

                        adicionarReserva(cpf_cliente, cliente, restaurante, mesa, data, horario)

            case 2:
                listarReservas()

            case 3:
                cpf_cliente = input("CPF do cliente atual da reserva: ")

                if temReserva(cpf_cliente):
                    print("DADOS PARA ATUALIZAR (deixe vazio para manter a informação atual):")
                    novoCliente = input("Nome do novo cliente: ")
                    novo_cpf_cliente = input("Digite o CPF do novo cliente: ")
                    novoRestaurante = input("Nome do novo restaurante: ")
                    novaMesa = input("Nova mesa nº: ")
                    novaData = input("Nova data (DD/MM/AAAA): ")
                    novoHorario = input("Novo horário (ex.: 19h): ")
                    atualizarReserva(cpf_cliente, novo_cpf_cliente, novoCliente, novoRestaurante, novaMesa, novaData, novoHorario)
                else:
                    print("Nenhuma reserva encontrada para este cliente.")

            case 4:
                cpf_cliente = input("Digite o CPF do cliente da reserva: ")
                excluirReserva(cpf_cliente)

            case 5:
                cpf_cliente = input("Digite o CPF do cliente da reserva: ")
                buscarReserva(cpf_cliente)

            case 6:
                print("VOLTANDO AO MENU ANTERIOR...\n")
                sleep(2)
                break

            case _:
                print("Opção inválida. Tente novamente.")