frs = input("Introduca una frase: ")

ltr = input("Introduca la letra a buscar en la frase: ")

if len(ltr) == 1 and 'A' <= ltr <= 'Z':
    ltr = chr(ord(ltr) + 32)
cont = 0

for crtr in frs:

    if crtr == ltr or (crtr == ltr.upper() and 'a' <= ltr <= 'z'):
        cont += 1

print("La letra ",ltr, "aparece",cont,"veces en la frase.")
