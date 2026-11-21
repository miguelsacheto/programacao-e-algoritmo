import json
#tentar carregar os dados salvos 
try:

    with open("filmes.json", "r", encoding="utf-8") as ficheiro:
        filmes = json.load(ficheiro)
except FileNotFoundError:
    filmes = []

#comprar o ingresso

def comprar_ingresso():

    resposta = input("deseja comprar um ingresso? (sim/não)")
    if resposta == "sim":
        print("ingresso comprado com sucesso!")
    elif resposta == "não":
        print("ok, obrigado por visitar nosso site!")

#cadastrar filmes

def cadastrar_filmes():

    poltronas = [] 
    nome = input("nome do filme: ")
    preço = float(input("preço do ingresso: "))
    dia_do_filme = input("dia do filme: ")

    filme = {
        "nome": nome,
        "preço": preço,
        "data": dia_do_filme,
    }

#criar as poltronas

    for i in range (1,11):
        poltrona = {
        "numero": i,
        "status": "disponivel",
        }
        poltronas.append(poltrona)

    filme["poltronas"] = poltronas
    filmes.append(filme) 

    salvar_dados()

#salvar os filmese a as poltronas 

def salvar_dados():

    with open("filmes.json", "w", encoding = "utf-8") as ficheiro:
         json.dump(filmes, ficheiro, indent=4, ensure_ascii=False)

#menu

def menu():
    resposta = input( "=== MENU CINEMA ===\n o que voce deseja\n 1.cadastrar filmes(1)\n 2.comprar ingressos(2)\n 3.salvar dados(3)\n")
    if resposta == "1":
        cadastrar_filmes()
    elif resposta == "2":
        comprar_ingresso()
    elif resposta == "3":
        salvar_dados()

menu()
