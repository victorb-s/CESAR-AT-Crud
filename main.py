import restaurantes
import reservas
import usuarios
import json
import os
from time import sleep

arquivo_usuarios = os.path.join(os.path.dirname(__file__), 'usuarios.json')
arquivo_restaurantes = os.path.join(os.path.dirname(__file__), 'restaurantes.json')

def jaExisteUsuario(cpf):
    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)

    cpf = cpf.replace(".", "").replace("-", "")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def jaExisteRestaurante(nome):
    with open(arquivo_restaurantes, 'r') as f:
        restaurantes = json.load(f)

    for restaurante in restaurantes:
        if restaurante['nomeRestaurante'] == nome:
            return True
    return False


def menu_inicial ():
    print ("=" *50)
    print (" >>> BEM VINDO AO SISTEMA RESERVAS SMART <<< ")
    print ("       1 - MÓDULO RESTAURANTES ")
    print ("       2 - MÓDULO USUÁRIOS ")
    print ("       3 - MÓDULO RESERVAS ")
    print ("       4 - SAIR ")
    print ("=" *50)

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("Informe uma opção: "))

        match(opcao_inicial):
            case 1:
                restaurantes.moduloRestaurante()
            case 2:
                usuarios.moduloUsuarios()
            case 3:
                reservas.moduloReservas()
            case 4:
                print("SAINDO...")
                sleep(1)
                break
            case _:
                print("Opção inválida.")



if __name__ == "__main__":
    main()