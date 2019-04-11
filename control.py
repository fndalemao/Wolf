import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()


def create_evento(nome):
    c.execute('CREATE TABLE %s (id_equipamento integer not null unique, '
              'numero_equipamento integer not null, '
              'modelo_equipamento text not null, '
              'tipo_equipamento text not null, '
              'foreign key(id_equipamento) references equipamento (id), '
              'foreign key(numero_equipamento) references equipamento (numero), '
              'foreign key(modelo_equipamento) references equipamento (modelo), '
              'foreign key(tipo_equipamento) references equipamento (tipo))' % nome)


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


def inserir_equip_evento(nome, id):
    c.execute(f'INSERT INTO {nome} SELECT * FROM equipamento WHERE id = {id}')


def historico_eventos():
    select = 'SELECT * FROM evento'
    print('ID'.ljust(19), 'Nome'.ljust(18), 'Data'.ljust(13), 'Data de Saída'.ljust(16), 'Data de Entrada')
    for row in c.execute(select):
        for i, s in enumerate(row):
            if i <= 3:
                print(str(s).ljust(18), end='')
            else:
                print(str(s).ljust(18), end='\n')


def delete_evento(nome_evento):
    c.execute('DROP TABLE %s'% nome_evento)


def ver_evento(nome):
    print(nome)
    select = f'SELECT * FROM {nome}'
    for row in c.execute(select):
        print(row)


def registrar_equipamento(numero, modelo, tipo):
    modelo_lista = ['"', modelo, '"']
    modelo_sql = modelo_lista[0] + modelo_lista[1] + modelo_lista[2]
    tipo_lista = ['"', tipo, '"']
    tipo_sql = tipo_lista[0] + tipo_lista[1] + tipo_lista[2]
    c.execute(f'INSERT INTO equipamento (numero, modelo, tipo) VALUES({numero}, {modelo_sql}, {tipo_sql})')
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
    elif opcao == 2:
        while True:
            try:
                delete_evento(str(input('Digite o nome do evento: ')))
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
        print('oi')
    elif opcao == 6:
        historico_eventos()


title('menu')
menu_principal()


