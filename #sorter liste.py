# Definer liste
usortert = [5, 3, 1, 2, 4]

# Gjennomfør så mange gjennomganger som det er elementer i listen
for _ in range(len(usortert)):
    # Gå gjennom hvert element i listen
    for i in range(len(usortert)-1):
        # Sammenlign to nabo elementer
        if usortert[i] > usortert[i+1]:
            # Bytt plass hvis de er i feil rekkefølge
            usortert[i], usortert[i+1] = usortert[i+1], usortert[i]

    # Skriv ut listen etter gjennomgangen
    print(usortert)
