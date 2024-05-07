# class Calculadora:
#     def __init__(self, num1, num2):
#         self.sumar = num1 + num2
#         self.restar = num1 - num2
#         self.multiplicar = num1 * num2
#         if num2 != 0:
#             self.dividir = num1 / num2
#         else:
#             self.dividir = "Error: No se puede dividir por cero."

#     def respuesta(self):
#         print("El resultado de la suma es:", self.sumar)
#         print("El resultado de la resta es:", self.restar)
#         print("El resultado de la multiplicación es:", self.multiplicar)
#         print("El resultado de la división es:", self.dividir)

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# operacion = Calculadora(num1, num2)
# operacion.respuesta()

class Gestor_empresa:
    def __init__(self):
        self.ingresos=0
        self.gastos=0
    def opci1(self,cant):
        self.ingresos+=cant
        print("Ingresos: ",self.ingresos)
    def opci2(self,cant):
        self.gastos+=cant
        print("Salidas: ",self.gastos)
    def opci3(self):
        balance=self.ingresos-self.gastos
        print("Balance: ",balance)

registro=Gestor_empresa()
opcion=0
while opcion!=4:
    print("\n1.Agregar ingresos")
    print("2.Agregar Salidas")
    print("3.Ver balance")
    print("4.Salir")
    opcion=int(input("Elija su opcion: "))
    if opcion == 1:
        cant = float(input("Ingrese cantidad de ingresos: "))
        registro.opci1(cant)
    elif opcion == 2:
        cant = float(input("Ingrese cantidad de gastos: "))
        registro.opci2(cant)
    elif opcion == 3:
        registro.opci3()
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Opcion no valida.")