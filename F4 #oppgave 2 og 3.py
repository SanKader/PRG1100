studentliste = []
print(studentliste)
print()

studentfil = open('studentinformasjon.txt', 'r', encoding="utf-8")

stnr = studentfil.readline()

while stnr != '':
    stnr = stnr.rstrip('\n')
    fornavn = studentfil.readline().rstrip('\n')
    etternavn = studentfil.readline().rstrip('\n')
    epost = studentfil.readline().rstrip('\n')
    fødselsdato = studentfil.readline().rstrip('\n')
    kjønn = studentfil.readline().rstrip('\n')
    studium = studentfil.readline().rstrip('\n')

    studentliste += [[stnr, fornavn, etternavn,
                      epost, fødselsdato, kjønn, studium]]
    student_dict = {}

    for student in studentliste:
        student_dict[student[0]] = student[1:]

    stnr = studentfil.readline()

studentfil.close()

print(studentliste)
listelengde = len(studentliste)
print(listelengde)


def hele_liste():
    print(studentliste)
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')
    print(student_dict)


def FEF_student():
    listelengde = len(studentliste)
    c = 1
    for r in range(listelengde):
        print(studentliste[r][c], 'har etternavn',
              studentliste[r][c+1], 'og fødselsdato', studentliste[r][c+3])


def FEE_kvinner():
    c = 1
    for r in range(listelengde):
        if studentliste[r][c+4] == 'Female':
            print(studentliste[r][c], studentliste[r]
                  [c+1], studentliste[r][c+2])


def SFEK_ALLE_BACH():
    c = 1
    for r in range(listelengde):
        if studentliste[r][c+5] == 'Bach IT og IS':
            print(studentliste[r][c-1], studentliste[r]
                  [c], studentliste[r][c+1], studentliste[r][c+4])


def tell_kvinner():
    student_dict = {}
    antall_kvinner = 0

    for student in studentliste:
        student_dict[student[0]] = student[1:]
        # If the gender of the student is Female
        if student[5] == "Female":
            antall_kvinner += 1
            # Print the information about the student
            print("Student ID:", student[0])
            print("Fornavn:", student[1])
            print("Etternavn:", student[2])
            print("Epost:", student[3])
            print("Fødselsdato:", student[4])
            print("Kjønn:", student[5])
            print("Studium:", student[6])
            print("------------------")
            print('antall kvinner er', antall_kvinner)


def tell_studenter_per_studium():
    program_count = {"Bach IT og IS": 0, "Bach økadm": 0}
    for student in studentliste:
        program = student[6]
        program_count[program] += 1

    print('antall studenter', program_count)


def main():
    print("Velg en av følgende sorteringsmetoder:")
    print("1. skriv ut alle studenter")
    print("2. fornavn, etternavn og fødselsdato")
    print("3. fornavn etternavn og epostadresser for alle kvinner")
    print('4. Studentnr, fornavn, etternavn og kjønn for alle studenter på studiet "bach it og is"')
    print('5. tell antall kvinner')
    print('6. antall studenter per studium')
    valg = int(input())
    if valg == 1:
        hele_liste()
    elif valg == 2:
        FEF_student()
    elif valg == 3:
        FEE_kvinner()
    elif valg == 4:
        SFEK_ALLE_BACH()
    elif valg == 5:
        tell_kvinner()
    elif valg == 6:
        tell_studenter_per_studium()
    else:
        print("Ugyldig valg.")


main()
