import sqlite3
from mylib import add_table, creat_column, open_csv, column, make_question
import os


def sql_to_csv(database, table_name):
    database = sqlite3.connect(database)

    table = database.execute(f"SELECT * FROM {table_name};")
    table = table.fetchall()
    column = database.execute(f'SELECT name FROM pragma_table_info("{table_name}");')
    column = column.fetchall()

    database.close()

    csv = creat_column(column)
    csv = add_table(table[0:-2], csv)

    for n in range(len(table[-1])):
        if n != len(table[-1]) - 1:
            csv += f"{table[-1][n]},"
        else:
            csv += f"{table[-1][n]}\n"
    return csv

# csv_content = sql_to_csv("all_fault_line.db", "fault_lines")
# # print(csv_content[0:1000])


def csv_to_sql(csv_content, database, table_name): 
    csv_content = open_csv(csv_content)

    conection = sqlite3.connect(database)

    cursor = conection.cursor()
    cursor.execute(f"create table if not exists {table_name} ({column(csv_content[0])})")
    # data = [(1, "Ridesharing", 'None', 'None', 'None', 'None'), (2, "Water Purifying", 'None', 'None', 'None', 'None'), (3, "Forensics", 'None', 'None', 'None', 'None'), (4, "Botany", 'None', 'None', 'None', 'None')]
    cursor.executemany(f"INSERT INTO {table_name} VALUES({make_question(csv_content[1])})", csv_content[1:])

    conection.commit()
    conection.close()


# csv_content = open('list_volcano.csv')
# csv_to_sql(csv_content, 'list_volcanos.db','volcanos')


# conection = sqlite3.connect('list_volcanos.db')
# cursor = conection.cursor()
# for row in cursor.execute(f"select * from volcanos"):
#     print('...')
#     print(row)
# conection.close()

# os.remove('list_volcanos.db')