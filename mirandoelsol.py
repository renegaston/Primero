"""
Ejercicio:
La estación de meteorología “Mirando el sol”, necesita almacenar las temperaturas de una semana. 
Para esto requiere de un sistema que permita mostrar y ejecutar el siguiente menú:

	        ******* Mirando el sol ******
              1.	Generar 	
              2.	Mostrar 
              3.	Promedio semanal
              4.	Bajo cero
              5.	Día con mayor y menor temperatura
              6.	Temperaturas ordenadas ascendentemente
              7.	Salir
                                Elija Opción: _

•	Si elige la opción 1, debe generar en forma aleatoria (en el rango -7.0 a 37.0) la información 
y almacenarla en un arreglo. Al finalizar este proceso, debe mostrar “Temperaturas generadas satisfactoriamente” 
•	Si elige la opción 2, debe mostrar las temperaturas con el siguiente formato:
		Día N° 1 = xx.x °
•	Si elige la opción 3, debe mostrar el promedio semanal que hubo
•	Si elige la opción 4, debe mostrar el dia y la temperatura bajo cero que hubo en la semana, si no hubo, mostrar mensaje adecuado
•	Si elige la opción 5, debe mostrar el número del día que hubo mayor y menor temperatura
•	Si elige la opción 6, debe mostrar las temperaturas ordenadas ascendentemente
•	Sólo con la opción 7 se saldrá del sistema

Si se elige las opciones 2, 3, 4, 5 o 6 sin haber elegido antes la opción 1, debe mostrar mensaje adecuado

Realizar un programa en Python que permita cumplir los requerimientos anteriores

"""
import numpy
import random
op=1
band=0
while(op!=7):
    print("\n\n******* Mirando el sol ******")
    print("1.	Generar")
    print("2.	Mostrar") 
    print("3.	Promedio semanal")
    print("4.	Bajo cero")
    print("5.	Día con mayor y menor temperatura")
    print("6.	Temperaturas ordenadas ascendentemente")
    print("7.	Salir")
    op=int(input("\tElija Opción: "))
    if(op==1):
        temperatura=[]
        for i in range(7):
            temperatura.append(round(random.uniform(-7,37),1))    
        band=1
        print("Temperaturas generadas satisfactorimente")
        print(temperatura)
    if(op==2):
        if(band==0):
            print("Debe generar temperatura")
        else:
            for i in range(7):
                print("Dia Nº "+str(i+1)+" = "+str(temperatura[i])+"º")
    if(op==3):
        if(band==0):
            print("Debe generar temperatura")
        else:
            suma=0
            for i in range(7):
                suma+=temperatura[i]
            prom=suma/(i+1)
            print("El promedio semanal es "+str(round(prom,1))+"º")
    if(op==4):
        if(band==0):
            print("Debe generar temperatura")
        else:
            bajo=[]
            dia=[]
            for i in range(7):
                if(temperatura[i]<0):
                    bajo.append(temperatura[i])
                    dia.append(i+1)
            if(len(bajo)!=0):
                print("\tEn la semana hubo temperatura bajo cero: ")
                for i in range(len(bajo)):
                    print("Dia "+str(dia[i])+" = "+str(bajo[i]))
            else:
                print("En la semana no hubieron temperatúras bajo cero")
    if(op==5):
        if(band==0):
            print("Debe generar temperatura")
        else:
            print("\t\tEl día con mayor temperatura es: ",str(temperatura.index(max(temperatura))+1))
            print("\t\tEl día con menor temperatura es: ",str(temperatura.index(min(temperatura))+1))
    if(op==6):#sorted sort
        if(band==0):
            print("Debe generar temperatura")
        else:
            menmay=sorted(temperatura)
            print("\tlas temperaturas ordenas ordenandas de menor a mayor son: \n",menmay)
else:
    print("Se ha finalizado el programa")