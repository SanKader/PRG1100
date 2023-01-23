# Definer liste
usortert = [4, 8, 1, 2, 2]

# Initialiser største verdi og indeksvariabler
storste_verdi = usortert[0]
storste_indeks = 0

# Gå gjennom hvert element i listen
for i in range(len(usortert)):
    # Sjekk om verdien er større enn største verdi
    if usortert[i] > storste_verdi:
        # Oppdater største verdi og indeks
        storste_verdi = usortert[i]
        storste_indeks = i

# Skriv ut listen før bytte
print(usortert)

# Bytt største verdi med siste element
usortert[storste_indeks], usortert[-1] = usortert[-1], usortert[storste_indeks]

# Skriv ut listen etter bytte
print(usortert)
