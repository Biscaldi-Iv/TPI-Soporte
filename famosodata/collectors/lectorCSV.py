import csv



def enumeradorURLS(start, cant):
    """Devuelve los primeros cant urls a partir de start+1
    Recordatorio: siempre arrancar de start+cant de la anterior iteracion"""
    url = 'https://www.therichest.com'
    with open('famosos.csv', newline='') as File:
        reader = csv.reader(File)
        i = j = 0
        for row in reader:
            if j == cant:
                return i,j,row
            if len(row) == 0 or row[0].find('/') != 0:
                continue
            elif i<start:
                i+=1
                continue
            else:
                i+=1
                j+=1
                row = url + row.pop()
                yield i,j,row


"""
a=enumeradorURLS(0,5)
b=enumeradorURLS(5,10)

for elem in a:
    print(elem)
print()
for elem in b:
    print(elem)
"""