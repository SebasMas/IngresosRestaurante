import matplotlib.pyplot as plt


#Creamos una lista para los días de la semana
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#Creamos otra lista para los ingresos de cada día (Establecemos que el tamaño de la lista es igual a la longitud de la lista dias y cada índice contiene el valor 0
# ya que no podemos iterar una lista vacía)
ingresos = [0] *len(dias)

#Creamos un ciclo para recorrer la lista dias[] 
for i in range(len(dias)):
    #Por cada índice, preguntamos la cantidad de dinero recibidad ese día
    dinero = int(input(f"Ingresos del día {dias[i]}: "))
    #Actualizamos el valor de cada índice de la lista ingresos[] por el dinero recibido
    ingresos[i] += dinero

#Usamos la libreria matplotlib para llamar una figura vacía y los ejes de la misma
fig, ax = plt.subplots()

#Establecemos los títulos de cada eje
ax.set_ylabel('Ventas')
ax.set_title('Cantidad de Ventas por Día')

#Establecemos las listas que va a recibir esta figura
plt.bar(dias, ingresos)
#Título de la imagen que va a entregar el programa
plt.savefig('Gráfica Z Burguer')
plt.show()

