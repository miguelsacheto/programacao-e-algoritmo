#importar o json para salvar
import json

#tentar carregar os dados salvos 
try:

    with open("filmes.json", "r", encoding="utf-8") as ficheiro:
        filmes = json.load(ficheiro)

except FileNotFoundError:
    filmes = []

#comprar o ingresso

def comprar_ingresso():

    resposta = input("deseja comprar ingressos? (sim/não)")

    if resposta == "sim":

        if len(filmes) == 0:

            print("nenhum filme cadastrado")
            return
        
        else:

            for filme in filmes:
                print(f'id: {filme["id"]} - nome: {filme["nome"]} | R$ {filme["preço"]} | Data: {filme["data"]}')

            id_escolhido = int(input("de qual filme deseja comprar um ingresso(id)? "))

            filme_escolhido = None
            
            for filme in filmes:

                if filme["id"] == id_escolhido:
                    filme_escolhido = filme
                    break

                if filme_escolhido is None:
                    print("filme não encontrado!")

                else:

                    print("\n======= TELA =======")

                mapa = ""

                for poltrona in filme_escolhido["poltronas"]:

                    if poltrona["status"] == "disponivel":
                        mapa += f'[{poltrona["numero"]}] '

                    else:

                        mapa += "[X] "

                    if poltrona["numero"] == 5:
                        mapa += "\n"

                print(mapa)

                if poltrona["status"] == "disponivel":
                    mapa += f'[{poltrona["numero"]}] '

                else:

                    mapa += "[X] "
                     
                    # quebra a linha depois da poltrona 5 para formar duas fileiras

                    if poltrona["numero"] == 5:
                                    mapa += "\n"
            
                    print(mapa)

    elif resposta == "não":

        print("ok, obrigado por visitar nosso site!")
        return

#cadastra filmes e cria os ids pra eles

def cadastrar_filmes():

    poltronas = [] 
    nome = input("nome do filme: ")
    preço = float(input("preço do ingresso: "))
    dia_do_filme = input("dia do filme: ")

    if len(filmes) == 0:

        id_filme = 1

    else: 

        max(f["id"] for f in filmes)
        maior_id = max(id_filme) + 1

    filme = {
        "nome": nome,
        "preço": preço,
        "data": dia_do_filme,
        "id": id_filme
    }

#criar as poltronas e as deixa em status disponivel

    for i in range (1,11):

        poltrona = {
        "numero": i,
        "status": "disponivel",
        }

        poltronas.append(poltrona)

    filme["poltronas"] = poltronas

    filmes.append(filme) 

    salvar_dados()

#salvar os filmes e a as poltronas em outro arquivo

def salvar_dados():

    with open("filmes.json", "w", encoding = "utf-8") as ficheiro:
         json.dump(filmes, ficheiro, indent=4, ensure_ascii=False)

#menu

def menu():
    resposta = input( "=== MENU CINEMA ===\n o que voce deseja\n 1.cadastrar filmes\n 2.comprar ingressos\n 3.salvar dados\n 4.sair\n digite o numero referente a opção: ")
    if resposta == "1":
        cadastrar_filmes()

    elif resposta == "2":
        comprar_ingresso()

    elif resposta == "3":
        salvar_dados()

    elif resposta == "4":
        exit()

while True: menu()
