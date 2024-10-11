#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% 
#de interés al año. Estos ahorros debido a intereses, que no se cobran hasta 
#finales de año, se te añaden al balance final de tu cuenta de ahorros. 
#Escribir un programa que comience leyendo la cantidad de dinero depositada 
#en la cuenta de ahorros, introducida por el usuario. Después el programa debe
#calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
#segundo y tercer años. Redondear cada cantidad a dos decimales.
dinero = input("Cuanto dinero quires depositar?: ")
x = float(dinero)
primero = (x - (x * 0.04))
segundo = (primero - (x * 0.04))
tercero = (segundo - (x * 0.04))
round(primero, 1)
round(segundo, 1)
round(tercero, 1)
print("Esto es lo recaudado:", (primero), "€")
print("Esto es lo recaudado:", (segundo), "€")
print("Esto es lo recaudado:", (tercero), "€")