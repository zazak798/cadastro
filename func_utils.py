def item_registration(list_of_items: list):
    item = {}
    name_item = input('Que item vamos cadastrar? ').strip().capitalize()

    while True:
        for items in list_of_items:
            if name_item == items['name']:
                print('Item já existente!')
        
        cad_item_quantity = input('Quantos vamos cadastrar? ')

        try:
                quantity = int(cad_item_quantity)
                item['nome'] = name_item
                item['quantidade'] = int(quantity)
                list_of_items.append(item)

                print(f"nome: {item['nome']} ")
                print(f"quantidade: {item['quantidade']} ")
                break

        except:
            print('Quantidade inválida!')
        


def edit(list_to_edit: list):
    item_to_edit = input('Que item vamos editar? ').capitalize()
    while True:
        item = search_item(list_to_edit, item_to_edit)
        change = input(
            'Digite [R/r] para Retirar a quantidade desejada\n'
            'Digite [A/a] para adicionar a quantidade desejada\n' 
            ''
            ).strip().capitalize()
        
        if change == 'A':
            amount = input('Digite a quantidade: ')

            try:
                item['quantidade'] += int(amount)

                print('Quantidade atualizada')
                break

            except:
                print('Quantidade invalida')

        elif change == 'R':
            amount = input('Digite a quantidade: ')

            try:
                if int(amount) <= item['quantidade']:
                    item['quantidade'] -= int(amount)
                    print('Quantidade atualizada')
                    break

                else:
                    print('Quantidade maior que temos no estoque')
                    break

            except:
                print('Quantidade invalida')
        else:
            print('Opção inválida!')



def list_to_items(list_to_edit : list):
    if list_to_edit:
        for item in list_to_edit:
            print(f"Item: {item['nome']}. Quantidade: {item['quantidade']}")
    
    else:
        print('Lista vazia')

def remove_item(list_to_edit):
    item_to_remove = input('Vamos remover qual item?' \
    '').strip().capitalize()

    for item in list_to_edit:
        if item['nome'] == item_to_remove:
            list_to_edit.remove(item)
            print('Item removido com sucesso') 
            return

    print("Item não encontrado")       

def search_item(list_to_edit, item):
    for product in list_to_edit:
        if item == product['nome']:
            return product
        
    print('Item não existe na lista')
