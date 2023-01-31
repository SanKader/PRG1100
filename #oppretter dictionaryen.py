# oppretter dictionaryen

kontakter = {'kari': 11111111, 'knut': 22222222,
             'lise': 33333333, 'lars': 4444444}

print('kontaktlista mi er:', kontakter)
print()

# for å hente ut en verdi fra dictionaryen oppgir du nøkkelen
# NB case-sensitiv
print(kontakter["lise"])
print()

# dersom nøkkel ikke finnes termineres programmet
# print(kontakter['tore'])
# det kan vi løse ved åteste om kontakten finnes via in-operatoren
if 'tore' in kontakter:
    print(kontakter['tore'])
else:
    print('kontakten tore finnes ikke')
print()

# søkekriteriet som inndata
navn = input('oppgi navn på kontakten: ')
if navn in kontakter:
    print(navn, 'har telefonnr', kontakter[navn])
else:
    print('kontakten', navn, 'finnes ikke')
print()

# utskrift av alle nøkler med verdier i en for-løkke
for key in kontakter:
    print(key, kontakter[key])

# legge til kontakt
navn = input('oppgi navn på ny kontakt: ')
tlfnr = int(input('og telefonnr er: '))
kontakter[navn] = tlfnr
print(kontakter)
print()

# slette kontakt
navn = input('oppgi navn på kontakten som skal slettes: ')
if navn in kontakter:
    print(navn, 'har telefonnr', kontakter[navn])
    del kontakter[navn]
else:
    print('kontakten finnes ikke')
print(kontakter)
print()
