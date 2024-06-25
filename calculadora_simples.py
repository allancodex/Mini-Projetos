#calculadora simples
#while loop ate o usuario sair
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
    escolha = input('Qual operação voce deseja realizar? (multiplicação, divisão, soma, subtração): ').lower()
    if escolha in opcoes:
        break
    else:
        print('Escolha uma opção válida')


while True:
    val1 = input('Valor um: ')
    val2 = input('Valor dois: ')
    if val1.isdigit() == False:
        val1 = input('Valor um: ')
    else:
        break

print(val1,val2)

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
