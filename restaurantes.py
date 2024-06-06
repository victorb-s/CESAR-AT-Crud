import json
import os
import textwrap 
from time import sleep

# Abrir e Fechar Json -----------------------
arquivo = os.path.join(os.path.dirname(__file__), 'restaurantes.json')

def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)
    
def salvar_json(arquivo, restaurantes):
    with open(arquivo, 'w') as f:
        json.dump(restaurantes, f, indent=4)

# Funções Base ------------------------------

# Adicionar Restaurante ---------------------
def adicionarRestaurante(arquivo):
    restaurantes = carregar_json(arquivo)
        
    nomeRestaurante = input("- Digite o nome: >>> ").title()
    
    while True:
        if filtrarRestaurante(arquivo, nomeRestaurante):
            print("\nO nome informado já existe!")
            nomeRestaurante = input("- Digite o nome: >>> ").title()
        else:
            break
        
    notaRest = float(input("- Digite a nota (0-5): >>> "))

    while (notaRest < 0 or notaRest > 5):
        print("Nota inválida. Tente novamente.")
        notaRest = float(input("- Digite a nota (0-5): >>> "))

    enderecoRest = input("- Informe o endereço (logradouro - nro - bairro - cidade/sigla estado): >>> ")
    telefoneRest = input("- Informe o número de telefone ((xx) 9xxx-xxx): >>> ")
    mesasRest = int(input("- Informe o número de mesas disponíveis: >>> "))
    horariosFuncionamento = input("- Informe os horários de funcionamento (ex: 09h - 12h e 12h - 20h): >>> ")
    cardapio = input("- Informe um item servido no seu restaurante e seu preço em R$ (Pressione Enter para cancelar): >>> ")
    
    while True:
        maisCardapio = input("- Informe outro item servido no seu restaurante e seu preço em R$ (Pressione Enter para cancelar): >>> ")
        if maisCardapio == "":
            break
        
        cardapio += "\n\t\t\t\t" + maisCardapio

    restaurantes.append({
            'nomeRestaurante': nomeRestaurante,
            'notaRest': notaRest,
            'enderecoRest': enderecoRest,
            'telefoneRest': telefoneRest,
            'mesasRest': mesasRest,
            'horariosFuncionamento': horariosFuncionamento,
            'cardapio': cardapio
            })
        
    salvar_json(arquivo, restaurantes)
    print("O restaurante foi adicionado!\n")
    
def filtrarRestaurante(arquivo, nomeRestaurante):
    restaurantes = carregar_json(arquivo)

    for restaurante in restaurantes:
        if restaurante['nomeRestaurante'].title() == nomeRestaurante:
            return True
    return False

# Listar Restaurantes -----------------------
def listarRestaurantes(arquivo):
    restaurantes = carregar_json(arquivo)

    if not restaurantes:
        print("\n=== Nenhum restaurante foi encontrado. ===\n")
        return

    topoListaRest = " LISTA DE RESTAURANTES "
    print("\n")
    print(topoListaRest.center(50, "-"))
    for restaurante in restaurantes:
        linha = f"""
Nome:\t\t\t\t{restaurante['nomeRestaurante']}
Nota:\t\t\t\t{restaurante['notaRest']}*
Endereço:\t\t\t{restaurante['enderecoRest']}
Telefone:\t\t\t{restaurante['telefoneRest']}
Mesas disponíveis:\t\t{restaurante['mesasRest']}
Horários:\t\t\t{restaurante['horariosFuncionamento']}
Cardápio:\t\t\t{restaurante['cardapio']}
            """
        print("=" * 50)
        print(textwrap.dedent(linha))
        print("=" * 50)
    print("-" * 50, "\n")
            
# Atualizar Restaurantes --------------------
def atualizarRestaurante(arquivo):
    restaurantes = carregar_json(arquivo)

    nomeRestAntigo = input("\n- Digite o nome do restaurante a ser atualizado: >>> ").title()

    for restaurante in restaurantes:
        if restaurante['nomeRestaurante'] == nomeRestAntigo:
            while True:
                if filtrarRestaurante(arquivo, nomeRestAntigo):
                    while True:
                        nomeRestNovo = input("- Digite o novo nome (Pressione Enter para avançar): >>> ")
                        if nomeRestNovo == "":
                            break
                        if nomeRestNovo != nomeRestAntigo and filtrarRestaurante(arquivo, nomeRestAntigo):
                            print("O nome inserido já existe. Por favor, insira um nome diferente.")
                        else:
                            restaurante['nomeRestaurante'] = nomeRestNovo.title()
                            break
             
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar a nota do restaurante? (S/N): >>> ",
                                chave="notaRest",
                                prompt="- Digite a nova nota: >>> ",
                                tipo=float
                                )
                
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar o endereço do restaurante? (S/N): >>> ",
                                chave="enderecoRest",
                                prompt="- Digite o novo endereço: >>> ",
                                tipo=str
                                )
                
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar o telefone do restaurante? (S/N): >>> ",
                                chave="telefoneRest",
                                prompt="- Digite o novo telefone: >>> ",
                                tipo=str
                                )
                
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar a quantidade de mesas do restaurante? (S/N): >>> ",
                                chave="mesasRest",
                                prompt="- Digite o novo quantia de mesas: >>> ",
                                tipo=int
                                )
                
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar o horário de funcionamento do restaurante? (S/N): >>> ",
                                chave="horariosFuncionamento",
                                prompt="- Digite o novo horário de funcionamento: >>> ",
                                tipo=str
                                )
                
                atualizarChave(restaurante,
                                pergunta="- Deseja atualizar o cardápio do restaurante? (S/N): >>> ",
                                chave="cardapio",
                                prompt="- Digite novos produtos para o cardápio (Um por vez): >>> ",
                                tipo=str
                                )

                break
    
            salvar_json(arquivo, restaurantes)
            print("O restaurante foi atualizado.")
    print("\n")

def atualizarChave(restaurante, pergunta, chave, prompt, tipo):
    while True:
        opcao = input(f"\n{pergunta}").lower()

        if opcao in ("s", "sim"):
            if tipo == str:
                novoValor = input(f"{prompt}")

                if chave == 'cardapio':
                    while True:
                        maisCardapio = input("Digite novos produtos para o cardápio (Pressione Enter para cancelar) >>> ")
                        if maisCardapio == "":
                            break
                        cardapio += "\n\t\t\t\t" + maisCardapio

                if novoValor:
                    restaurante[chave] = novoValor
                    
            elif tipo == float:
                novoValor = float(input(f"{prompt}"))
                
                if chave == 'notaRest':
                    while (novoValor < 0 or novoValor> 5):
                        print("Nota inválida. Tente novamente.")
                        novoValor = float(input("- Digite a nova nota (0-5): >>> "))

                if novoValor:
                    restaurante[chave] = novoValor

            elif tipo == int:
                novoValor = float(input(f"{prompt}"))

                if novoValor:
                    restaurante[chave] = novoValor
            break

        elif opcao in ("n", "nao"):
            break
        
        else:
            print("Opção Inválida, por favor, insira algo válido")

# Excluir Restaurante ---------------------
def excluirRestaurante(arquivo, nomeRestaurante):
    restaurantes = carregar_json(arquivo)
    
    for restaurante in restaurantes:
        if restaurante['nomeRestaurante'] == nomeRestaurante.title():
            restaurantes.remove(restaurante)
            salvar_json(arquivo, restaurantes)
            print("O restaurante foi excluído.\n")
			return
    
    print("O restaurante não foi encontrado")

# Buscar Restaurante -----------------------
def buscarRestaurante(arquivo, nomeRestaurante):
    restaurantes = carregar_json(arquivo)

    topoListaRest = f" INFOS {nomeRestaurante.upper()} "
    print("\n")
    print(topoListaRest.center(50, "-"))
    for restaurante in restaurantes:
        if restaurante['nomeRestaurante'] == nomeRestaurante.title():
            linha = f"""
Nome:\t\t\t\t{restaurante['nomeRestaurante']}
Nota:\t\t\t\t{restaurante['notaRest']}*
Endereço:\t\t\t{restaurante['enderecoRest']}
Telefone:\t\t\t{restaurante['telefoneRest']}
Mesas disponíveis:\t\t{restaurante['mesasRest']}
Horários:\t\t\t{restaurante['horariosFuncionamento']}
Cardápio:\t\t\t{restaurante['cardapio']}
                """
            print("=" * 50)
            print(textwrap.dedent(linha))
            print("=" * 50)
            print("-" * 50, "\n")
			return

	print("Nenhum restaurante foi encontrado com esse nome")

    
    
def exibirMenu():
    print("=" * 21, " MENU ", "=" * 21)
    print("\t[1]\tAdicionar Restaurantes")
    print("\t[2]\tListar Restaurantes")
    print("\t[3]\tAtualizar Restaurante")
    print("\t[4]\tExcluir Restaurante")
    print("\t[5]\tListar um Restaurante")
    print("\t[6]\tVOLTAR AO MENU INICIAL")
    print("=" * 50)
    
def moduloRestaurante():
    while True:
        exibirMenu()
        opcao = (input(">>> "))
        
        match(opcao):
            case "1" | "Adicionar Restaurante":
                adicionarRestaurante(arquivo)

            case "2" | "Listar Restaurantes":
                listarRestaurantes(arquivo)

            case "3" | "Atualizar Restaurante":
                atualizarRestaurante(arquivo)

            case "4" | "Excluir Restaurante":
                nomeRestaurante = input("Digite o nome do restaurante a ser exclúido: >>> ")
                excluirRestaurante(arquivo, nomeRestaurante)

            case "5" | "Buscar Restaurante":
                nomeRestaurante = input("Digite o nome do restaurante: >>> ")
                buscarRestaurante(arquivo, nomeRestaurante)

            case "6" | "Voltar":
                print("VOLTANDO AO MENU ANTERIOR...\n")
                sleep(2)
                break

            case _:
                print("Opção inválida. Tente novamente.")