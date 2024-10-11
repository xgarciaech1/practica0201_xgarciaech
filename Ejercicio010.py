#cada paquete así que deben calcular el peso de los payasos y muñecas que 
#saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
#Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado
munecas = input("Cuantos payasos quires?: ")
payaso = input("Cuantas muñecas quires?: ")
x = float((payaso) * (112))
y = float((munecas) * (75))
u = int(x + y)
print("El peso total del producto es:", (u), "gramos")