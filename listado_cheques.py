import csv
import sys
import datetime
#No hicimos uso del argparse

print(sys.argv)
#DATOS OBLIGATORIOS QUE DEBE ENVIAR EL USUARIO
filename = sys.argv[1]
dni_a_filtrar = sys.argv[2]
pantalla_o_csv = sys.argv[3]
tipo = sys.argv[4]
#OPCIONALES
estado = None #Esto por lo que vi hace que no tire error out of range en el codigo
fecha_a_filtrar = None #Esto por lo que vi hace que no tire error out of range en el codigo

if len(sys.argv) > 5:
     estado = sys.argv[5]

if len(sys.argv) > 6:
     fecha_a_filtrar = sys.argv[6]     


with open(filename, "r") as file:
        reader = csv.DictReader(file)
        datos = [row for row in reader]

datos_filtrados = [dato for dato in datos if dato ['DNI'] == dni_a_filtrar]
datos_filtrados = [dato for dato in datos_filtrados if dato ['Tipo'] == tipo]

if estado is not None:
    datos_filtrados = [dato for dato in datos_filtrados if dato ['Estado'] == estado]

if pantalla_o_csv == 'CSV':  
    #with open("salida.csv", "w") as salida:
     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") #Esto le da formato cuando se crea el .csv con fecha
     with open(f"{dni_a_filtrar}_{timestamp}.csv","w") as salida:
        writer = csv.DictWriter(salida, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(datos_filtrados)
elif pantalla_o_csv == 'PANTALLA':
    for fila in datos_filtrados:
        print(fila)
else:
    print("Opción incorrecta. Elegir entre 'CSV' o 'PANTALLA'.")
     
