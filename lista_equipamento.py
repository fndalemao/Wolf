import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()


def registrar_equipamento(numero, modelo, tipo):
    modelo_lista = ['"', modelo, '"']
    modelo_sql = modelo_lista[0] + modelo_lista[1] + modelo_lista[2]
    tipo_lista = ['"', tipo, '"']
    tipo_sql = tipo_lista[0] + tipo_lista[1] + tipo_lista[2]
    c.execute(f'INSERT INTO equipamento (numero, modelo, tipo) VALUES({numero}, {modelo_sql}, {tipo_sql})')
    connection.commit()


registrar_equipamento(int(input('Digite o número do equipamento: ')), str(input('Digite o modelo do equipamento: ')), str(input('Digite o tipo do equipamento: ')))
