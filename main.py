from func_utils import  item_registration, edit, list_to_items, remove_item
import os

if __name__ == "__main__":
    print('Bem-vindo ao sistema de itens!')
    print('-'*30 )
    response = None
    list_of_items = []
    while response != 'S':
        response = input(
            'Digite C para cadastrar \n' \
            'Digite R para remover itens \n' \
            'Digite E para editar um item \n' \
            'Digite L para Listar os itens \n' \
            'Digite S para Sair \n' \
            ''
            ).upper()

        if response == 'C':
            item_registration(list_of_items)
            os.system('cls')
        
        elif response == "E":
            edit(list_of_items)
            os.system('cls')


        elif response == 'L':
            list_to_items(list_of_items)
            os.system('cls')


        elif response == 'R':
            remove_item(list_of_items)
            os.system('cls')

        elif response == 'S':
            print('Adeus')

        else:
            print('Opção inválida.')



