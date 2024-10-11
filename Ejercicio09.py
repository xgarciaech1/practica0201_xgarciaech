#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años,
#y muestre por pantalla el capital obtenido en la inversión.
cantida = input("Cantidad a invertir: ")
interes = input("Interes anual: ")
años = input("El numero de años que quieres invertir: ")
x = float(cantida)
y = float(interes)
u = float(años)
resultado_final = print(x * (1 + (u * y) / 100))