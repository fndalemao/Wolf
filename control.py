import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()


def create_evento(nome):
    c.execute(f'CREATE TABLE {nome} (id_equipamento integer not null primary key autoincrement unique, '
              'numero_equipamento integer not null, '
              'modelo_equipamento text not null, '
              'tipo_equipamento text not null, '
              'status_equipamento text not null default "Evento")')


def inserir_evento(nome, data, data_saida, data_entrada):
    nome_lista = ['"', nome, '"']
    nome_sql = nome_lista[0] + nome_lista[1] + nome_lista[2]
    data_lista = ['"', data, '"']
    data_sql = data_lista[0] + data_lista[1] + data_lista[2]
    data_saida_lista = ['"', data_saida, '"']
    data_saida_sql = data_saida_lista[0] + data_saida_lista[1] + data_saida_lista[2]
    data_entrada_lista = ['"', data_entrada, '"']
    data_entrada_sql = data_entrada_lista[0] + data_entrada_lista[1] + data_entrada_lista[2]
    c.execute(f'INSERT INTO evento (nome, data, data_saida, data_entrada) '
              f'VALUES({nome_sql}, {data_sql}, {data_saida_sql}, {data_entrada_sql})')
    connection.commit()


def inserir_hist_evento():
    c.execute(f'INSERT INTO historico_evento SELECT * FROM evento')
    connection.commit()


def ver_equipamento_galpao():
    select = f'SELECT * FROM equipamento WHERE status = "Galpão"'
    print('ID'.ljust(18), 'Modelo'.ljust(16), 'N°'.ljust(20), 'Tipo'.ljust(14), 'Status'.ljust(16))
    for row in c.execute(select):
        for i, s in enumerate(row):
            if i <= 3:
                print(str(s).ljust(18), end='')
            else:
                print(str(s).ljust(18), end='\n')


def inserir_equip_evento(nome, id):
    nome_lista = ['"', nome, '"']
    nome_sql = nome_lista[0] + nome_lista[1] + nome_lista[2]
    c.execute(f'INSERT INTO {nome} SELECT * FROM equipamento WHERE id = {id}')
    c.execute(f'UPDATE equipamento SET status = {nome_sql} WHERE id = {id}')
    connection.commit()


def ver_equipamento():
    select = f'SELECT * FROM equipamento'
    print('ID'.ljust(18), 'Modelo'.ljust(16), 'N°'.ljust(20), 'Tipo'.ljust(14), 'Status'.ljust(16))
    for row in c.execute(select):
        for i, s in enumerate(row):
            if i <= 3:
                print(str(s).ljust(18), end='')
            else:
                print(str(s).ljust(18), end='\n')


def historico_eventos():
    select = 'SELECT * FROM historico_evento'
    print('ID'.ljust(19), 'Nome'.ljust(18), 'Data'.ljust(13), 'Data de Saída'.ljust(16), 'Data de Entrada')
    for row in c.execute(select):
        for i, s in enumerate(row):
            if i <= 3:
                print(str(s).ljust(18), end='')
            else:
                print(str(s).ljust(18), end='\n')


def delete_evento(nome):
    nome_lista = ['"', nome, '"']
    nome_sql = nome_lista[0] + nome_lista[1] + nome_lista[2]
    c.execute(f'DROP TABLE {nome_sql}')
    c.execute(f'DELETE FROM evento WHERE nome = {nome_sql}')
    connection.commit()


def ver_evento(nome):
    select = f'SELECT id, modelo, numero, tipo FROM {nome} WHERE id = 2'
    for row in c.execute(select):
        print(row)


def registrar_equipamento(modelo, numero, tipo):
    modelo_lista = ['"', modelo, '"']
    modelo_sql = modelo_lista[0] + modelo_lista[1] + modelo_lista[2]
    tipo_lista = ['"', tipo, '"']
    tipo_sql = tipo_lista[0] + tipo_lista[1] + tipo_lista[2]
    c.execute(f'INSERT INTO equipamento (modelo, numero, tipo) VALUES({modelo_sql}, {numero}, {tipo_sql})')
    connection.commit()


def title(title):
    print('=' * 50)
    print(title.center(50).upper())
    print('=' * 50)


def menu_principal():
    print('1 - Abrir evento.')
    print('2 - Fechar evento.')
    print('3 - Ver evento')
    print('4 - Adicionar equipamento ao evento')
    print('5 - Lista de equipamentos')
    print('6 - Histórico de eventos')
    print('7 - Registrar equipamento')

    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        #nome = str(input('Digite o nome do evento: '))
        #create_evento(nome)
        while True:
            nome = str(input('Digite o nome do evento: '))
            try:
                create_evento(nome)
                break
            except:
                print('ESTE EVENTO JÁ FOI CRIADO!')

        inserir_evento(nome, str(input('Digite a data do evento: [dd/mm/yyyy]')),
                       str(input('Digite a data de saída do galpão: [dd/mm/yyyy] ')),
                       str(input('Digite a data da volta para o galpão: [dd/mm/yyyy]')))
        inserir_hist_evento()
    elif opcao == 2:
        while True:
            nome = str(input('Digite o nome do evento: '))
            try:
                delete_evento(nome)
                break
            except:
                print('ESTE EVENTO JÁ FOI FECHADO!')
    elif opcao == 3:
        while True:
            nome = str(input('Digite o nome do evento: '))
            try:
                ver_evento(nome)
                break
            except:
                print('EVENTO INVÁLIDO!')
    elif opcao == 4:
        ver_equipamento_galpao()
        nome = str(input('Digite o nome do evento: '))
        id = int(input('Selecione o equipamento: '))
        inserir_equip_evento(nome, id)



    elif opcao == 5:
        ver_equipamento()
    elif opcao == 6:
        historico_eventos()
    elif opcao == 7:
        while True:
            modelo = str(input('Digite o modelo do equipamento: '))
            numero = int(input('Digite o número do equipamento: '))
            tipo = str(input('Digite o tipo do equipamento: '))
            try:
                registrar_equipamento(modelo, numero, tipo)
                break
            except:
                print('ESTE EQUIPAMENTO JÁ FOI REGISTRADO!')


title('menu')
menu_principal()


