from func_uteis import cadastro_item, editar, listar, remover
import os

if __name__ == "__main__":
    print('Bem-vindo ao sistema de itens!')
    print('-'*30 )
    resposta = None
    lista_de_itens = []
    while resposta != 'S':
        resposta = input(
            'Digite C para cadastrar \n' \
            'Digite R para remover itens \n' \
            'Digite E para editar um item \n' \
            'Digite L para Listar os itens \n' \
            'Digite S para Sair \n' \
            ''
            ).upper()

        if resposta == 'C':
            cadastro_item(lista_de_itens)
            os.system('cls')
        
        elif resposta == "E":
            editar(lista_de_itens)
            os.system('cls')


        elif resposta == 'L':
            listar(lista_de_itens)
            os.system('cls')


        elif resposta == 'R':
            remover(lista_de_itens)
            os.system('cls')

        elif resposta == 'S':
            print('Adeus')

        else:
            print('Opção inválida.')



