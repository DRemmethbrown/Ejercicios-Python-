n=int(input("Por favor, introduce un número par: "))

if n%2 != 0:
    print("El número ingresado no es par.")
else:
    nt = ""
    for i in range(n- 1, 0, -2):
        nt += str(i) + ","
    print("Los números impares que le anteceden son:", nt[:-1])