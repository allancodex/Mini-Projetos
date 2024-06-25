#calculadora simples
#definindo as funções necessárias: add, sub, mul, div
#mostrar as opções de operações para usuário
#pedir valores 
#o programa continuará rodando até o usuário parar o loop

while True:
    class Valores_e_operacoes:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self, num1, num2):
            return print(num1 + num2)

        def sub(self, num1, num2):
            return print(num1 - num2)

        def mul(self, num1, num2):
            return print(num1 * num2)

        def div(self, num1, num2):
            return print(num1 / num2)


    #Pedindo e verificando input do usuário com relação a operação escolhida
    opcoes = ['multiplicação', 'divisão', 'soma', 'subtração']
    while True:
        escolha = input('Qual operação voce deseja realizar? (multiplicação, divisão, soma, subtração): ').lower().strip()
        if escolha in opcoes:
            break
        else:
            print('Escolha uma opção válida')

    # Pedindo e verificando input do usuário com relação aos valores inseridos para as variáveis
    while True:
        try:
            val1 = int(input('Valor um: '))
            val2 = int(input('Valor dois: '))
            break
        except ValueError:
            print('Por favor, insira um inteiro para as duas variáveis')

    #Realizando a operação pedida pelo usuário
    resultado = Valores_e_operacoes(val1, val2)
    match escolha:
        case 'multiplicação':
            resultado.mul(val1, val2)

        case 'divisão':
            resultado.div(val1, val2)

        case 'soma':
            resultado.add(val1, val2)

        case 'subtração':
            resultado.sub(val1, val2)

    #Pergunta se o usuário deseja continuar
    decisao = input('Você deseja continuar?(sim/não) ').lower().strip()
    if decisao == 'não':
        break
