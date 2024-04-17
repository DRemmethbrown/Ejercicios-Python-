n=int(input("Por favor, introduce un número par: "))

if n%2 != 0:
    print("El número ingresado no es par.")
else:
    nt = ""
    for i in range(n-1, -1, -1):
        nt += str(i) + ","
    print("Los números que le anteceden son:", nt[:-1])