#Escribir un programa que pregunte al usuario por el número de horas 
#trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.
time = input("numero de horas trabajadas?: ")
coste = input("Coste por hora?: ") 
x = int(time)
y = int(coste)
print(f"lo que le cobra es: {x * y}")  