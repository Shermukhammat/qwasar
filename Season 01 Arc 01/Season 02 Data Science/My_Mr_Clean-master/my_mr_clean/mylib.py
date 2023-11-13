import re

def drop_ab(abdict, data):
    for key, value in abdict.items():
        # print(key)
        # print(value)
        matche = f"{key}.*{value}"
        while True:
            loc = re.search(matche, data)
        
            if loc:
                a = list(loc.span())[0]
                b = list(loc.span())[1]
                data = data.replace(data[a:b], "")
            else:
                break     
    return data


def drop_symbol(data):
    
    while True:
        loc = re.search(" .\n", data)
        if loc:
            a = list(loc.span())[0]
            b = list(loc.span())[1]
            data = data.replace(data[a:b], "")
        else:
            break
    return data

    
def drops(elements, put, data):
    for rep in elements:
        data = data.replace(rep, put)
    return data
