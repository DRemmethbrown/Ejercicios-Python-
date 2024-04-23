# cant=int(input("Ingrese la cant: "))
# ex=str(input("Ingrese en que unidad de medida esta expresado: "))

# if ex =="m":
#     ft= cant *3.28
#     pulg= cant *39.37
#     yrd= cant *1.09
#     cm= cant *100
#     print(cant,"mt son equivalentes a:",round(ft,2),"pies o",round(pulg,2),"pulgadas o",round(yrd,2),"yardas o",cm,"centimetros.")
# elif ex =="c":
#     ft= cant /30.48
#     pulg= cant /2.54
#     yrd= cant /91.44
#     mt= cant /100
#     print(cant,"cm son equivalentes a:",round(ft,2),"pies o",round(pulg,2),"pulgadas o",round(yrd,2),"yardas o",mt,"metros.")
# elif ex =="f":
#     cm= cant *30.48
#     pulg= cant *12
#     yrd= cant /3
#     mt= cant /3.28
#     print(cant,"pies son equivalentes a:",round(cm,2),"centimetros o",round(pulg,2),"pulgadas o",round(yrd,2),"yardas o",round(mt,2),"metros.")
# elif ex =="p":
#     cm= cant *2.54
#     ft= cant /12
#     yrd= cant /36
#     mt= cant /39.37
#     print(cant,"pulgadas son equivalentes a:",round(cm,2),"centimetros o",round(ft,2),"pies o",round(yrd,2),"yardas o",round(mt,2),"metros.")
# elif ex =="y":
#     cm= cant *91.44
#     ft= cant *3
#     pulg= cant *36
#     mt= cant /1.09
#     print(cant,"yardas son equivalentes a:",round(cm,2),"centimetros o",round(ft,2),"pies o",round(pulg,2),"pulgadas o",round(mt,2),"metros.")
# else:
#     print("Expresión no valida!!")


cant = float(input("Ingrese la cantidad: "))

if cant <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    cants = {}

    for i in range(12):
        if cant >= [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.01][i]:
            cant_mon = cant // [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.01][i]
            cants[[200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.01][i]] = cant_mon
            cant -= cant_mon * [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.01][i]

    print("Para la cantidad de", cant, "quetzales, se necesitan las siguientes monedas y billetes:")
    for den in cants:
        if den >= 1:
            print(int(cants[den]), "billetes de Q", den)
        else:
            print(int(cants[den]), "monedas de Q", den)
