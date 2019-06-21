#! python3

def loadJSON(data, fname):

    fhandler = open(fname + '.json', 'w')
    fhandler.write(fname + ' = [\n')

    lastChars = ',\n'

    for c, coords in enumerate(data):
        point = {"x": coords[0], "y": coords[1]}

        if c == len(data) - 1:
            lastChars = '\n];'
        fhandler.write('  ' + str(point) + lastChars)
    fhandler.close()

    # print("%s data points created" % len(data))
    # print("Open index.html to see visualization")
