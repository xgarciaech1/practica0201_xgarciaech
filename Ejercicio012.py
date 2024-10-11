#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
#tiene un descuento del 60%. Escribir un programa que comience leyendo el
#número de barras vendidas que no son del día. Después el programa debe 
#mostrar el precio habitual de una barra de pan, el descuento que se le hace 
#por no ser fresca y la ganancia final total.
no = input("Cuantas barras de pan no del dia hemos vendido: ")
x = float(no)
pan = (3.49 - (x* 0.04))
print("El pan del mismo dia vale 3.49€")
print("Al no ser del dia descuento de 60%")
print("La ganacia del pan es de:", (x), "€")