#Testando uma ideia que tive vai funcionar

index = 0
nome = 0
nomes = ['bob','syd','beau']

#função que atribui código ao nome do funcionãrio
def org_funcionarios(nomes):
    for index, nome in enumerate(nomes):     
        func = {'codigo': index, 'nome': nome}
        print(func)

org_funcionarios(nomes)

