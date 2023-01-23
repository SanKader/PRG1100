#Funksjonen bubble_sort() defineres
def bubble_sort():
    A = [1,3,5,6,7,9] #Liste A defineres og inneholder verdiene [1,3,5,6,7,9]
    bytte = True #Variabelen "bytte" defineres og settes til True
    #En while-løkke starter
    while bytte:
        bytte = False #Variabelen "bytte" settes til False
        #En for-løkke starter
        for i in range(len(A)-1): #Løkken går gjennom alle elementene i listen A, unntatt det siste
            if A[i] > A[i+1]: #Hvis elementet i er større enn elementet til høyre for det
                bytte = True #Så settes variabelen "bytte" til True
                A[i], A[i+1] = A[i+1], A[i] #Elementene bytter plass
        #For-løkken slutter
    #While-løkken slutter
    print(A) #Skriver ut den sorterte listen A

#Funksjonen insertion_sort() defineres
def insertion_sort():
    A = [5,3,8,6,9,1] #Liste A defineres og inneholder verdiene [5,3,8,6,9,1]
    #En for-løkke starter
    for i in range(1, len(A)): #Løkken går gjennom alle elementene i listen A, unntatt det første
        j = i #Variabelen j settes til i
        #En while-løkke starter
        while j > 0 and A[j-1] > A[j]: #Så lenge j er større enn 0 og elementet til venstre for j er større enn j
            A[j], A[j-1] = A[j-1], A[j] #Bytter plass på elementene
            j -= 1 #j reduseres med 1
        #While-løkken slutter
    #For-løkken slutter
    print(A) #Skriver ut den sorterte listen A

#Funksjonen efficient_insertion_sort() defineres
def efficient_insertion_sort():
    A = [5,3,8,6,9,1] #Liste A defineres og inneholder verdiene [5,3,8,6,9,1]
    #En for-løkke starter
    for i in range(1, len(A)): #Løkken går gjennom alle elementene i listen A, unntatt det første
        x = A[i] #Variabelen x settes til elementet i
        j = i - 1 #Variabelen j settes til i-1
        #En while-løkke starter
        while j >= 0 and A[j] > x: #Så lenge j er større eller lik 0 og elementet til venstre for j er større enn x
            A[j+1] = A[j] #Elementet til venstre for j flyttes ett steg til
            j -= 1 #j reduseres med 1
         #While-løkken slutter
        A[j+1] = x #x plasseres på sin korrekte posisjon i listen
    #For-løkken slutter
    print(A) #Skriver ut den sorterte listen A

def main():
    print("Velg en av følgende sorteringsmetoder:")
    print("1. Boblesortering")
    print("2. Innstikksortering")
    print("3. Effektiv innstikksortering")
    valg = int(input())
    if valg == 1:
        bubble_sort()
    elif valg == 2:
        insertion_sort()
    elif valg == 3:
        efficient_insertion_sort()
    else:
        print("Ugyldig valg.")

main()

#Hver av de tre sorteringsfunksjonene tar en liste som input og sorterer den i henhold til den valgte metoden. 
#Menyen lar deg velge hvilken metode du vil bruke og kaller den tilsvarende funksjonen. 
#Det kan være lurt å legge til validering for å sikre at en gyldig verdi blir gitt som input i menyen.

