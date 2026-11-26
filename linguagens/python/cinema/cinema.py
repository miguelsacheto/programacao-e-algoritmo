import json

# Tentar carregar os dados salvos
try:
    with open("filmes.json", "r", encoding="utf-8") as ficheiro:
        filmes = json.load(ficheiro)

except FileNotFoundError:
    filmes = []


# Comprar ingresso
def comprar_ingresso():

    resposta = input("Deseja comprar ingressos? (sim/não): ").lower()

    if resposta == "sim":

        if len(filmes) == 0:
            print("Nenhum filme cadastrado!")
            return

        else:
            for filme in filmes:
                print(f'ID: {filme["id"]} - Nome: {filme["nome"]} | R$ {filme["preço"]} | Data: {filme["data"]}')

            id_escolhido = int(input("De qual filme deseja comprar um ingresso (ID)? "))

            filme_escolhido = None

            for filme in filmes:
                if filme["id"] == id_escolhido:
                    filme_escolhido = filme
                    break

            if filme_escolhido is None:
                print("Filme não encontrado!")
                return

            # Mostrar as poltronas
            print("\n======= TELA =======")

            mapa = ""

            for poltrona in filme_escolhido["poltronas"]:

                if poltrona["status"] == "disponivel":
                    mapa += f'[{poltrona["numero"]}] '
                else:
                    mapa += "[X] "

                if poltrona["numero"] % 5 == 0:
                    mapa += "\n"

            print(mapa)

            # Escolher poltrona
            poltrona_escolhida = int(input("Escolha o número da poltrona: "))

            encontrada = False

            for poltrona in filme_escolhido["poltronas"]:

                if poltrona["numero"] == poltrona_escolhida:
                    encontrada = True

                    if poltrona["status"] == "disponivel":

                        poltrona["status"] = "indisponivel"

                        salvar_dados()

                        print("\nIngresso comprado com sucesso!")
                        print(f'Filme: {filme_escolhido["nome"]}')
                        print(f'Poltrona: {poltrona_escolhida}')
                        print(f'Valor: R$ {filme_escolhido["preço"]:.2f}')

                    else:
                        print("Essa poltrona já está ocupada!")

                    break

            if encontrada == False:
                print("Poltrona inválida!")

    elif resposta == "não":
        print("Ok, obrigado por visitar nosso site!")

    else:
        print("Resposta inválida!")


# Cadastrar filmes
def cadastrar_filmes():

    poltronas = []

    nome = input("Nome do filme: ")
    preço = float(input("Preço do ingresso: "))
    dia_do_filme = input("Dia do filme: ")

    if len(filmes) == 0:
        id_filme = 1

    else:
        maior_id = max(f["id"] for f in filmes)
        id_filme = maior_id + 1

    filme = {
        "nome": nome,
        "preço": preço,
        "data": dia_do_filme,
        "id": id_filme
    }

    # Criar as poltronas
    for i in range(1, 11):

        poltrona = {
            "numero": i,
            "status": "disponivel"
        }

        poltronas.append(poltrona)

    filme["poltronas"] = poltronas

    filmes.append(filme)

    salvar_dados()

    print("Filme cadastrado com sucesso!")


# Salvar dados
def salvar_dados():

    with open("filmes.json", "w", encoding="utf-8") as ficheiro:
        json.dump(filmes, ficheiro, indent=4, ensure_ascii=False)


# Menu
def menu():

    resposta = input(
        "\n=== MENU CINEMA ===\n"
        "O que você deseja?\n"
        "1. Cadastrar filmes\n"
        "2. Comprar ingressos\n"
        "3. Salvar dados\n"
        "4. Sair\n"
        "Digite o número da opção: "
    )

    if resposta == "1":
        cadastrar_filmes()

    elif resposta == "2":
        comprar_ingresso()

    elif resposta == "3":
        salvar_dados()
        print("Dados salvos!")

    elif resposta == "4":
        salvar_dados()
        print("Saindo do sistema...")
        exit()

    else:
        print("Opção inválida!")


while True:
    menu()
