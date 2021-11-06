import csv


def enumeradorURLS(start, cant):
    """Devuelve los primeros cant urls a partir de start+1
    Recordatorio: siempre arrancar de start+cant de la anterior iteracion"""
    url = 'https://www.therichest.com'
    with open('collectors/famosos.csv', newline='') as File:
        reader = csv.reader(File)
        i = j = 0
        for row in reader:
            if j == cant:
                return row
            if len(row) == 0 or row[0].find('/') != 0:
                continue
            elif i < start:
                i += 1
                continue
            else:
                i += 1
                j += 1
                row = url + row.pop()
                yield row


"""
a = enumeradorURLS(0, 5)
print("out-->")
print(next(a))
print(next(a))
print("Gen-->")
for i in a:
    print(i)
b=enumeradorURLS(5,10)

for elem in a:
    print(elem)
print()
for elem in b:
    print(elem)
"""
a = enumeradorURLS(708, 5)
for elem in a:
    print(elem)
