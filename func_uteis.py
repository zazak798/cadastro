def cadastro_item(lista_de_itens: list):
    item = {}
    nome_item = input('Que item vamos cadastrar? ').strip().capitalize()

    while True:
        for itens in lista_de_itens:
            if nome_item == itens['nome']:
                print('Item já existente!')
        
        cad_item_quantidade = input('Quantos vamos cadastrar? ')

        try:
                quantidade = int(cad_item_quantidade)
                item['nome'] = nome_item
                item['quantidade'] = int(quantidade)
                lista_de_itens.append(item)

                print(f"nome: {item['nome']} ")
                print(f"quantidade: {item['quantidade']} ")
                break

        except:
            print('Quantidade inválida!')
        


def editar(lista_de_itens: list):
    item_para_editar = input('Que item vamos editar? ').capitalize()
    while True:
        item = procura_item(lista_de_itens, item_para_editar)
        alteracao = input(
            'Digite [R/r] para Retirar a quantidade desejada\n'
            'Digite [A/a] para adicionar a quantidade desejada\n' 
            ''
            ).strip().capitalize()
        
        if alteracao == 'A':
            quantidade = input('Digite a quantidade: ')

            try:
                item['quantidade'] += int(quantidade)

                print('Quantidade atualizada')
                break

            except:
                print('Quantidade invalida')

        elif alteracao == 'R':
            quantidade = input('Digite a quantidade: ')

            try:
                if int(quantidade) <= item['quantidade']:
                    item['quantidade'] -= int(quantidade)
                    print('Quantidade atualizada')
                    break

                else:
                    print('Quantidade maior que temos no estoque')
                    break

            except:
                print('Quantidade invalida')
        else:
            print('Opção inválida!')



def listar(lista : list):
    if lista:
        for item in lista:
            print(f"Item: {item['nome']}. Quantidade: {item['quantidade']}")
    
    else:
        print('Lista vazia')

def remover(lista):
    item_a_remover = input('Vamos remover qual item?' \
    '').strip().capitalize()

    for item in lista:
        if item['nome'] == item_a_remover:
            lista.remove(item)
            print('Item removido com sucesso') 
            return

    print("Item não encontrado")       

def procura_item(lista, item):
    for produto in lista:
        if item == produto['nome']:
            return produto
        
    print('Item não existe na lista')
