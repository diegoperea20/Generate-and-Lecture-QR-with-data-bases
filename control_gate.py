import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime
import openpyxl

# Inicializa la cámara
cap = cv2.VideoCapture(0)  # El valor 0 representa la cámara predeterminada

# Crea un nuevo archivo de Excel con la fecha actual
def crear_nuevo_archivo():
    now = datetime.now()
    fecha_actual = now.strftime("%Y-%m-%d")
    archivo_excel = f"{fecha_actual}.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Nombre", "Hora", "Minuto", "Fecha"])
    return wb, ws, archivo_excel, now

wb, ws, archivo_excel, now = crear_nuevo_archivo()

while True:
    # Captura un fotograma de la cámara
    ret, frame = cap.read()

    # Decodifica los códigos QR presentes en el fotograma
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        print("Contenido del código QR:", data)
        
        # Obtiene las coordenadas de los vértices del código QR
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(frame, [hull], True, (0, 255, 0), 3)
        else:
            cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 3)
        
        # Obtiene la hora actual
        hora = now.hour
        minuto = now.minute
        fecha = now.strftime("%d/%m/%Y")

        # Agrega los datos al archivo de Excel
        ws.append([data, hora, minuto, fecha])

    # Muestra el fotograma con los códigos QR detectados y el cuadrado verde
    cv2.imshow("Codigos QR en tiempo real", frame)
    wb.save(archivo_excel)

    
    # Si la fecha cambia, crea un nuevo archivo de Excel
    nueva_fecha = datetime.now().strftime("%Y-%m-%d")
    if nueva_fecha != archivo_excel[:-5]:  # Compara con la fecha en el nombre actual del archivo
        wb.save(archivo_excel)
        wb, ws, archivo_excel, now = crear_nuevo_archivo()

   

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
