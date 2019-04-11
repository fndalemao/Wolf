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



