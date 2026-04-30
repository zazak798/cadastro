def cadastro_item(lista_de_itens: list):
    item = {}
    nome_item = input('Que item vamos cadastrar? ').strip().capitalize()

    for itens in lista_de_itens:
        if nome_item == itens['nome']:
            print('Item já existente!')
            return
    
    cad_item_quantidade = input('Quantos vamos cadastrar? ')

    try:
        quantidade = int(cad_item_quantidade)
        item['nome'] = nome_item
        item['quantidade'] = int(quantidade)
        lista_de_itens.append(item)

        print(f"nome: {item['nome']} ")
        print(f"quantidade: {item['quantidade']} ")

    except:
        print('Quantidade inválida!')
        return
    


def editar(lista_de_itens: list):
    item_para_editar = input('Que item vamos editar? ').capitalize()
    if lista_de_itens:
        for item in lista_de_itens:
            if item['nome'] == item_para_editar:
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
                        if int(quantidade) < item['quantidade']:
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
                    return

        else:
            print('Não encontrei o item desejado')
            return
        
    else:
        print('Lista vazia')

def listar(lista : list):
    if lista:
        for item in lista:
            print(f"Item: {item['nome']}. Quantidade: {item['quantidade']}")
    
    else:
        print('Lista vazia')
        return

def remover(lista):
    item_a_remover = input('Vamos remover qual item?' \
    '').strip().capitalize()

    for item in lista:
        if item['nome'] == item_a_remover:
            lista.remove(item)
            print('Item removido com sucesso') 
            return

    print("Item não encontrado")       

def continua(msg):
    continuar = True

    while continuar:
        continua = input(f'Quer continuar {msg} [S/N] ').upper()

        if continua == 'S':
            continuar = True
            return continuar
        
        elif continua == 'N':
            return False
        
        else:
            print("Opção inválida")
            continuar = True


