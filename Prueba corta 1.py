###CORREGUIR 1###
# contra = str(input("Introduce la contraseña: "))
# if contra== "sesamo":
#   print("Pasa")
# else:
#   print('No pasa')


###CORREGUIR 2###
# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base 
# base = int(input('Introduce la base imponible de la factura: '))
# print(aplica_iva(base, iva=21))


###CORREGUIR 3###

# u = (1, 2, 3)
# v = (4, 5, 6)

# def producto_escalar(u, v):
#     resultado=0
#     for i in range(len(u)):
#         resultado+=u[i] * v[i]
#     return resultado

# print(producto_escalar(u, v))


###CORREGUIR 4###
# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     if usuario in listin:
#          del listin[usuario]
#          return 
#     else:
#          return
# print(elimina(listin, 'Pablo'))



###CORREGUIR 5###

# a = ((1, 2, 3),
#      (3, 2, 1))
# b = ((1, 2),
#      (3, 4),
#      (5, 6))

# def producto(a, b):
#     filas_a=len(a)
#     columnas_a=len(a[0])
#     columnas_b=len(b[0])

#     producto = []

#     for i in range(filas_a):
#         fila = []
#         for j in range(columnas_b):
#             suma = 0
#             for k in range(columnas_a):
#                 suma += a[i][k] * b[k][j]
#             fila+= (suma,)
#         producto+= [tuple(fila)]
#     return tuple(producto)
# print(producto(a,b))
