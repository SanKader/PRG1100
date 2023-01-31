# flere verdier

ansatte = {}
print()

ansattfil = open('laerer.txt', 'r', encoding='utf-8')


fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')

    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    # fornavn som key og etternavn, epost som value i en liste
    ansatte[fornavn] = [etternavn, epost]
    fornavn = ansattfil.readline()

ansattfil.close()
# skriver ut hele dictionaryen
print('resultatet ble:', ansatte)
print()

# skriver ut alle nøkler og deler av opplysningene, nøkkel og epost
for key in ansatte:
    print(key, ansatte[key][1])
