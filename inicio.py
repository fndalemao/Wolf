import abrir_evento


def title(title):
    print('=' * 50)
    print(title.center(50).upper())
    print('=' * 50)


def menu_principal():
    print('1 - Abrir evento.')
    print('2 - Fechar evento.')
    print('3 - Selecionar evento')
    print('4 - Lista de eventos')
    print('5 - Lista de equipamentos')
    print('6 - Adicionar equipamento ao evento')
    print('7 - Registrar equipamento')

    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        while True:
            nome = str(input('Digite o nome do evento: '))
            try:
                abrir_evento.create_evento(nome)
                break
            except:
                print('ESTE EVENTO JÁ FOI CRIADO!')

        abrir_evento.inserir_evento(nome, str(input('Digite a data do evento: [dd/mm/yyyy]')),
                       str(input('Digite a data de saída do galpão: [dd/mm/yyyy] ')),
                       str(input('Digite a data da volta para o galpão: [dd/mm/yyyy]')))

title('menu')
menu_principal()


