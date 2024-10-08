#Escribir un programa que pida al usuario su peso (en kg)
#y estatura (en metros), calcule el índice de masa corporal y
#lo almacene en una variable, y muestre por pantalla la frase Tu índice 
#de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
#redondeado con dos decimales.
Peso = (input(float("Dime tu peso en kg: ")))
Altura = (input(float("Dime tu altura en m: ")))
imc = float(Peso/(Altura)**2)
input("Tu indice de masa coporal es{imc}: ")