import os
from regras import regras

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

print("=" * 32)
print("VÉRITAS".center(32))
print("O jogo de conhecimento católico".center(32))
print("=" * 32)
print(" ")
jogador = input("Digite seu nome: ")
limpar_tela()

print("Seja bem vindo(a): ", jogador)
limpar_tela()

while True:
    resposta = input(f"{jogador}, você deseja ver as regras do jogo? ").lower()
    if resposta in ["sim", "s", "si", "ss"]:
        print(regras)
        break
    elif resposta in ["não", "n", "ñ", "nn", "no"]:
        break
    else:
        print(f"Erro,{jogador} por gentileza, digite sim ou não.")

print("Vamos iniciar o jogo. ")