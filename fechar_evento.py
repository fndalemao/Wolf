import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()


def delete_evento(nome_evento):
    c.execute('DROP TABLE %s'% nome_evento)


while True:
    try:
        delete_evento(str(input('Digite o nome do evento: ')))
        break
    except:
        print('ESTE EVENTO JÁ FOI FECHADO!')
