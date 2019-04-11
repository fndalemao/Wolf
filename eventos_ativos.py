import sqlite3
connection = sqlite3.connect('wolf.db')
c = connection.cursor()

select = 'SELECT * FROM evento'


def eventos_ativos():
    print('ID'.ljust(19), 'Nome'.ljust(18), 'Data'.ljust(13), 'Data de Saída'.ljust(16), 'Data de Entrada')
    for row in c.execute(select):
        for i, s in enumerate(row):
            if i <= 3:
                print(str(s).ljust(18), end='')
            else:
                print(str(s).ljust(18), end='\n')


eventos_ativos()
