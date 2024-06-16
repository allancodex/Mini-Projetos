import random

MAXIMO_LINHAS = 3
APOSTA_MAXIMA = 100
APOSTA_MINIMA = 1

LINHAS = 3
COLUNAS = 3

#Itens da roleta
cont_simbolos = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

valores_simbolos = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

#Função para verificar se o usuário ganhou. Em caso positivo, quanto
def checar_resultados(colunas, linhas, aposta, valores_simbolos):
    ganhos = 0
    linhas_vencedoras = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_para_checar = coluna[linha]
            if simbolo != simbolo_para_checar:
                break
        else:
            ganhos += valores_simbolos[simbolo] * aposta
            linhas_vencedoras.append(linha + 1)
    return ganhos, linhas_vencedoras


#função para criar o resultado da roleta
def resultado_da_aposta(linhas, colunas, simbolos):
    todos_simbolos = []
    for simbolo, cont_simbolos in simbolos.items():
        for _ in range(cont_simbolos):
            todos_simbolos.append(simbolo)

    col = []
    for _ in range(colunas):
        coluna = []
        simbolos_atuais = todos_simbolos [:]
        for _ in range(linhas):
            resultado = random.choice(simbolos_atuais)
            simbolos_atuais.remove(resultado)
            coluna.append(resultado)
        col.append(coluna)
    return col
    #EXPLICAÇÃO NO TEMPO 29:55

#função para mostrar ao usuário o resultado da roleta
def mostrar_resultado(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i  != len(colunas) - 1:
                print(coluna[linha], end = " | ")
            else:
                print(coluna[linha],end =" ")

        print()

#função para receber o deposito
def deposito():
    while True:
        deposito = input("Valor do deposito em R$")
        if deposito.isdigit():
            deposito = int(deposito)
            if deposito > 0:
                break
            else:
                print("O valor de deposito tem que maior que zero")
        else:
            print("Por favor, digite um valor")
    return deposito

#Função para saber em quantas linhas será apostado
def numero_linhas():
    while True:
        linhas = input("Quantidade de linhas que você vai apostar (1-" + str(MAXIMO_LINHAS) + "): ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1<= linhas <= MAXIMO_LINHAS:
                break
            else:
                print("Escolha um número válido")
        else:
            print("Por favor, digite um número")
    return linhas

#valor que será apostado em cada linha
def valor_aposta_linha():
    while True:
        aposta = input("Valor da aposta em cada linha: ")
        if aposta.isdigit():
            aposta = int(aposta)
            if APOSTA_MINIMA <= aposta <= APOSTA_MAXIMA:
                break
            else:
                print(f"O valor da aposta tem que ser entre R${APOSTA_MINIMA} - R${APOSTA_MAXIMA}")
        else:
            print("Por favor, digite um valor")
    return aposta

def rodada(valor_depositado):
    linhas = numero_linhas()
    # Loop de para verificar se o valor da aposta é válido
    while True:
        aposta = valor_aposta_linha()
        valor_total = aposta * linhas
        if valor_total > valor_depositado:
            print(f"Você nao tem o suficiente para fazer essa aposta, seu saldo é R$ {valor_depositado} ")
        else:
            break

    print(f"Você está apostando R${aposta} em {linhas} linhas. Total da aposta é igual a: R${valor_total}")

    slots = resultado_da_aposta(LINHAS, COLUNAS, cont_simbolos)
    mostrar_resultado(slots)
    ganhos, linhas_vencedoras = checar_resultados(slots, linhas, aposta, valores_simbolos)
    print(f"Vocẽ ganhou R$ {ganhos}")
    print(f"Vocẽ ganhou na linha(s): ", *linhas_vencedoras)
    return ganhos - valor_total


def main():
    valor_depositado = deposito()
    while True:
        print(f"Valor atual disponível R${valor_depositado} ")
        spin = input("Pressione enter para apostar ou 's' para sair ")
        if spin == 's':
            break
        valor_depositado += rodada(valor_depositado)

    print(f"Você tem R${valor_depositado}")

#Essa é, muito possivelmente a versao final

main()