import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()


def create_evento(nome):
    print(nome)
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
    c.execute(f'INSERT INTO evento (nome, data, data_saida, data_entrada) VALUES({nome_sql}, {data_sql}, {data_saida_sql}, {data_entrada_sql})')
    connection.commit()


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


