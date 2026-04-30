from func_uteis import cadastro_item, continua, editar, listar, remover

if __name__ == "__main__":
    print('Bem-vindo ao sistema de itens!')
    print('-'*30 )
    
    lista_de_itens = []
    while True:
        opcao = input(
            'Digite C para cadastrar \n' \
            'Digite R para remover itens \n' \
            'Digite E para editar um item \n' \
            'Digite L para Listar os itens \n' \
            ''
            ).upper()

        if opcao == 'C':
            while True:
                cadastro_item(lista_de_itens)
                if not continua('Cadastrando'):
                    break
        
        elif opcao == "E":
            while True:
                editar(lista_de_itens)

                if not continua('Editando'):
                    break

        elif opcao == 'L':
            listar(lista_de_itens)

        elif opcao == 'R':
            remover(lista_de_itens)

        else:
            print('Opção inválida.')

        continuar = input('Quer continuar em nosso sistema? [S/N] ').upper()
        
        if continuar == 'S':
            continue
        break


