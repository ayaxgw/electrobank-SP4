import csv
import sys
import datetime

def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp))

def format_datetime(dt_obj):
    return dt_obj.strftime('%Y-%m-%d %H:%M:%S')

# Validar que se proporcionen suficientes argumentos
if len(sys.argv) < 5:
    print("Uso: python script.py <filename> <dni_a_filtrar> <pantalla_o_csv> <tipo> [estado] [fecha_a_filtrar]")
    sys.exit(1)

# DATOS OBLIGATORIOS
filename = sys.argv[1]
dni_a_filtrar = sys.argv[2]
pantalla_o_csv = sys.argv[3]
tipo = sys.argv[4]
# OPCIONALES
estado = None
fecha_a_filtrar = None

# Leer argumentos opcionales
if len(sys.argv) > 5:
    estado = sys.argv[5]

if len(sys.argv) > 6:
    fecha_a_filtrar = sys.argv[6]

# Abre el archivo y lee el contenido
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    datos = [row for row in reader]

# Filtrar los datos 
datos_filtrados = [dato for dato in datos if dato['DNI'] == dni_a_filtrar]
datos_filtrados = [dato for dato in datos_filtrados if dato['Tipo'] == tipo]

if estado is not None:
    datos_filtrados = [dato for dato in datos_filtrados if dato['Estado'] == estado]

if fecha_a_filtrar is not None:
    fecha_a_filtrar = datetime.datetime.strptime(fecha_a_filtrar, '%Y-%m-%d').date()
    datos_filtrados = [dato for dato in datos_filtrados if datetime.datetime.strptime(dato['Fecha'], '%Y-%m-%d').date() == fecha_a_filtrar]

# Parte que valida si se desea la salida en CSV o en pantalla
if pantalla_o_csv == 'CSV':
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"{dni_a_filtrar}_{timestamp}.csv"

    with open(output_filename, "w") as salida:
        writer = csv.DictWriter(salida, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(datos_filtrados)
    print(f"Datos filtrados guardados en {output_filename}")

elif pantalla_o_csv == 'PANTALLA':  # Esta es la sección que deseas modificar
    for fila in datos_filtrados:
        fila['FechaOrigen'] = format_datetime(timestamp_to_datetime(fila['FechaOrigen']))
        fila['FechaPago'] = format_datetime(timestamp_to_datetime(fila['FechaPago']))
        print(f"Fila: {fila}")

else:
    print("Opción incorrecta. Elegir entre 'CSV' o 'PANTALLA'.")
