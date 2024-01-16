# PRUEBA B - DESARROLLO DE ALGORITMO
# Francisco Rolando Aguilera Portillo

import csv
import os

# Función principal para convertir un archivo .csv en un .txt tabulado
def convertir_csv(csv_ruta, txt_tabulado_ruta):
    # Abrimos el archivo .csv para su lectura
    with open(csv_ruta, 'r') as archivo_csv:
        # Usamos la función reader() para leer línea a línea el .csv
        data = csv.reader(archivo_csv)
        # Leemos y guardamos la primera línea como un header o cabecera
        header = next(data)
        # Abrimos un archivo .txt para su respectiva escritura
        with open(txt_tabulado_ruta, 'w') as txt_tabulado:
            # Modificamos el header original para tener el formato solicitado de AÑO.MES.DIA en la primera columna
            nuevo_header = [header[0] + '.' + header[1] + '.' + header[2]] + header[3:]
            # Se concatena las tres primeras columnas con un punto y luego se utiliza el vector desde la posición 3 en adelante
            txt_tabulado.write('\t'.join(nuevo_header) + '\n')
            # Iteramos cada fila del CSV hasta el "end of file"
            for fila in data:
                # Concatenamos las tres primeras columnas según el formato solicitado de AÑO.MES.DIA
                fila_aux = fila[0] + '.' + fila[1] + '.' + fila[2]
                # Continuamos con los siguientes datos de forma secuencial, desde la posición 3 en adelante
                nueva_fila = [fila_aux] + fila[3:]
                # Escribimos la nueva fila tabulada
                txt_tabulado.write('\t'.join(nueva_fila) + '\n')

# Función para mover el archivo .txt a una carpeta determinada
def mover_archivo(ruta_archivo, carpeta_destino):
    # Extraemos el nombre de la carpeta de la ruta de destino
    nombre = os.path.basename(carpeta_destino)
    # Si la carpeta de destino no existe, la creamos
    if not os.path.exists(nombre):
        os.makedirs(nombre)
    # Generamos la nueva ruta del archivo uniendo la carpeta de destino y el nombre del archivo
    nueva_ruta = os.path.join(carpeta_destino, os.path.basename(ruta_archivo))
    # Mover el archivo a la carpeta especificada
    os.replace(ruta_archivo, nueva_ruta)
    print("\n Se ha creado el archivo exitosamente y se ha movido a la carpeta de destino preseleccionada.")

# Variables
csv_ruta = "DDU_IN/dhl.csv"
txt_tabulado_ruta = "dhl.txt"
carpeta_destino = "DDU_OUT"

# Función para convertir el archivo .csv en un archivo de texto (.txt) tabulado
convertir_csv(csv_ruta, txt_tabulado_ruta)

# Función para mover el archivo en la ruta de destino seleccionada
mover_archivo(txt_tabulado_ruta, carpeta_destino)