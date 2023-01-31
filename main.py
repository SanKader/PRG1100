import os

def main():
    studentnr=input('Skriv inn studentnr: ')
    finnes, studnr=sjekk_student(studentnr)
    if finnes == False:
        print('Studentnr ikke gyldig')
    else:
        skriv_karakterliste(studnr)
    

def sjekk_student(studnr):
    finnes=False
    studenter=open('student.txt', 'r')
    linje=studenter.readline()
    while linje != '' and finnes == False:
        linje=linje.rstrip('\n')
        if linje != studnr:
            linje=studenter.readline()
            linje=studenter.readline()
            linje=studenter.readline()
            linje=studenter.readline()
        else:
            finnes=True
    studenter.close()

    return finnes, studnr;


def skriv_karakterliste(skriv_karakterlisteStudentnr):
    # henter studentinfo
    studentfil = open('student.txt', 'r')
    studentnr_fil = studentfil.readline()
    while studentnr_fil != '':
        studentnr_fil = studentnr_fil.rstrip('\n')
        fornavn_fil = studentfil.readline().rstrip('\n')
        etternavn_fil = studentfil.readline().rstrip('\n')
        studium_fil = studentfil.readline().rstrip('\n')

        if studentnr_fil != skriv_karakterlisteStudentnr:
            studentnr_fil = studentfil.readline()
        else:
            fornavn = fornavn_fil
            etternavn = etternavn_fil
            studium = studium_fil
            studentnr_fil = ''

    studentfil.close()

    # utskrift
    print()
    print('-----------------------------------------------------------------------------')
    print('karakterutskrift for studentnr:', skriv_karakterlisteStudentnr)
    print()
    print(fornavn, etternavn, studium)
    print()

    # henter eksamensresultat for student og legger i fil
    eksamensresultat_fil = open('eksamensresultat.txt', 'r')
    eksamner_temp = open('eksamner_temp.txt', 'w')

    emnekode_fil = eksamensresultat_fil.readline()
    while emnekode_fil != '':
        emnekode_fil = emnekode_fil.rstrip('\n')
        studentnr_fil = eksamensresultat_fil.readline().rstrip('\n')
        karakter_fil = eksamensresultat_fil.readline().rstrip('\n')
        if studentnr_fil == skriv_karakterlisteStudentnr:
            eksamner_temp.write(emnekode_fil+'\n')
            eksamner_temp.write(studentnr_fil+'\n')
            eksamner_temp.write(karakter_fil+'\n')
        emnekode_fil = eksamensresultat_fil.readline()
    eksamensresultat_fil.close()
    eksamner_temp.close()

    # printer eksamensresultater fra fil
    eksamner_temp = open('eksamner_temp.txt', 'r')
    emnekode_fil = eksamner_temp.readline()
    while emnekode_fil != '':
        emnekode = emnekode_fil.rstrip('\n')
        eksamner_temp.readline()
        karakter = eksamner_temp.readline().rstrip('\n')
        # henter emnenavn
        emne_fil = open('emne.txt', 'r')
        emnekode_emnefil = emne_fil.readline()
        while emnekode_emnefil != '':
            emnekode_emnefil = emnekode_emnefil.rstrip('\n')
            emnenavn_fil = emne_fil.readline().rstrip('\n')
            if emnekode_emnefil != emnekode:
                emnekode_emnefil = emne_fil.readline()
            else:
                emnenavn = emnenavn_fil
                emnekode_emnefil = ''
        emne_fil.close()
        print(emnekode, emnenavn, karakter)
        emnekode_fil = eksamner_temp.readline()

    eksamner_temp.close()
    os.remove('eksamner_temp.txt')

    # utskrift
    print('-----------------------------------------------------------------------------')
    print()
    print()

main()