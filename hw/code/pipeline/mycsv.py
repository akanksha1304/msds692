import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):

    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    content = data
    header = []
    data = []
    sentences = content.split('\n')
    header = sentences[0].split(',')
    for i in range(1, len(sentences)):
        row_list = sentences[i].split(',')
        data.append(row_list)
    return header, data
