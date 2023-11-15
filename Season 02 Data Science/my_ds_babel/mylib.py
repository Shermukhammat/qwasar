def add_table(table, csv):
    for series in table:
        stop = len(series)-1
        for n in range(len(series)):
            if n != stop:
                csv += f"{series[n]},"
            else:
                csv += f"{series[n]}\n"
    return csv

def creat_column(column):
    csv = ""
    for n in range(len(column)):
        if n != len(column)-1:
            csv += f'{column[n][0]},'
        else:
            csv += f'{column[n][0]}\n'
    return csv


def open_csv(opened_file):
    respons = []
    for row in opened_file.readlines():
        respons.append(row[0:-1].split(','))
    return respons

def column(columns):
    respons = ""   
    for column  in columns[0:-1]:
        respons += f"'{column}' text,"
    return respons + f"'{columns[-1]}' text"

def make_question(column):
    respons = ""
    leng = len(column)
    for n in range(leng-1):
        respons+="?, "
    return respons+"?"