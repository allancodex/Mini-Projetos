#Testando uma ideia que tive vai funcionar

index = 0
nome = 0
nomes = ['bob','syd','beau']

#função que atribui código ao nome do funcionãrio
def org_funcionarios(nomes):
    for index, nome in enumerate(nomes):
        return index, nome

#função que mostra todos os funcionários e seus códigos
def indentificar_funcionario(index, nome):
    for index, nome in enumerate(nomes):
        print(f'Código do funcionário: {index}, nome do funcionário: {nome}')

org_funcionarios(nomes)
indentificar_funcionario(index, nome)
