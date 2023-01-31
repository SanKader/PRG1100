ansatte = []
print(ansatte)
print()

ansattfil = open('laerer.txt', 'r', encoding='utf-8')

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')
    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    ansatte += [[fornavn, etternavn, epost]]

    fornavn = ansattfil.readline()

ansattfil.close()

print(ansatte)
print()

listelengde = len(ansatte)
print(listelengde)
print()

# skriver ut initialer og epostadresser
# uten variable for kolonne/c
print('initialerer og epostadresser')
for r in range(listelengde):
    print(ansatte[r][0][0:1], ansatte[r][1][0:1],
          'har e-postadresse', ansatte[r][2])
    print()

# skriver ut initialer og epostadresser for de med etternavn som starter på s
print('initialer og epostadresser for fornavn på S')
for r in range(listelengde):
    if ansatte[r][0][0:1] == 's':
        print(ansatte[r][0][0:1], ansatte[r][1][0:1],
              'har epostadresse', ansatte[r][2])
print()

# ved bruk av slicing på variabel for bedre oversikt
print('initialer og epostadresser for etternavn på s')
for r in range(listelengde):
    etternavn = ansatte[r][1]
    if etternavn[0:1] == 's':
        print(ansatte[r][0][0:1], etternavn[0:1],
              'har epostadresse', ansatte[r][2])
print()
