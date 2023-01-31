# oppretter en tom liste
ansatte = []
print(ansatte)
print()

ansattfil = open('laerer.txt', 'r', encoding='utf-8')

# Leser hele fila linje for linje med while-løkke og test på eof, se s 336

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')

    # leser resten av posten
    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    # legger posten inn i lista, "liste i liste"-tankegang
    ansatte += [[fornavn, etternavn, epost]]
    fornavn = ansattfil.readline()

# lukker fila
ansattfil.close()

print('resulatet ble:', ansatte)
print()

# skriver ut hele liste
print(ansatte)
print()

# skriver ut en post
print(ansatte[0])
print()

# skriver ut en verdi
print(ansatte[0][2])

listelengde = len(ansatte)
print(listelengde)
print()

# dvs at vi får antall rader/poster som listelengde  ved 2-dimensjonal tabell

# skriver ut alle etternavn
print('etternavn:')
c = 1
for r in range(listelengde):  # print ute 12?
    print(ansatte[r][c])
print()

# skrive ut alle etternavn og eposter

print('etternavn og eposter')
c = 1
for r in range(listelengde):
    print(ansatte[r][c], 'har epostadresse', ansatte[r][c+1])
