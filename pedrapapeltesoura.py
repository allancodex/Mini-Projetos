import random

#lista de strings
opcoes = ["pedra","papel","tesoura"]

def pegar_escolhas():
    escolha_jogador = input("Pedra, papel ou tesoura? ")
    escolha_computador = random.choice(opcoes)
    #dict = {"key":"value"}
    escolhas = {"jogador" : escolha_jogador, "computador" : escolha_computador}

    return escolhas

def ganhador(jogador,computador):
    print(f"Você escolheu {jogador}, o computador escolheu {computador}")

    if jogador == computador:
        return "Empate!"
    elif jogador == "pedra":
        if computador == "tesoura":
            return "pedra ganha da tesoura! Você ganhou!"
        else:
            return "pedra perde para papel! Você perdeu."
    elif jogador == "papel":
        if computador == "pedra":
            return "papel ganha da pedra! Você ganhou!"
        else:
            return "papel perde para tesoura! Você perdeu."
    elif jogador == "tesoura":
        if computador == "papel":
            return "tesoura ganha do papel! Você ganhou!"
        else:
            return "tesoura perde para pedra! Você perdeu."


escolhas = pegar_escolhas()
resultado = ganhador(escolhas["jogador"], escolhas["computador"])
print(resultado)