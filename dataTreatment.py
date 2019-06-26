#! python3
# dataTreament.py — Colleccion de utilidades para la manipulacion de 
#                   la data para y proveniente de la SOM

def cleaner(brute_data):
    """
        Devuelve una lista de vectores limpios
    """

    cleaned_data = list()

    for doc in brute_data:
        doc_lst = [
            doc['runtime'],
            doc['tomato']['rating']
        ]

        cleaned_data.append(doc_lst)
    return cleaned_data

def standarize(n):
    """
        Metodo de estandarizacion sencilla (base 10)
    """
    if abs(n) >= 10:
        return n / 10
    return n

def build_JSON_coor(data, fname):
    """
        Construye un archivo JSON de coordenadas x,y
    """
    
    fhandler = open('data.js', 'w')
    fhandler.write('const data = [\n')

    lastChars = ',\n'

    for c, coords in enumerate(data):
        point = { "x": coords[0], "y": coords[1] }

        if c == len(data) - 1:
            lastChars = '\n];'
        fhandler.write('  ' + str(point) + lastChars)
    fhandler.close()
