import schedule
import time
import subprocess

# Define una variable global para almacenar el objeto Popen del proceso
clock_process = None

root="C:/Users/User/Desktop/qr_generator/control_gate.py"

# Función para lanzar el proceso del script control_gate.py
def lanzar_clock():
    global clock_process
    print("Ejecutando el script control_gate.py...")
    clock_process = subprocess.Popen(["python", root])

# Define la función para cerrar el proceso del script control_gate.py
def cerrar_clock():
    global clock_process
    if clock_process:
        print("Cerrando el script control_gate.py...")
        clock_process.terminate()

# Programa el lanzamiento del script clock_control_day.py a las 18:54
schedule.every().day.at("19:15").do(lanzar_clock)

# Programa el cierre del script clock_control_day.py a las 18:55
schedule.every().day.at("19:18").do(cerrar_clock)

while True:
    schedule.run_pending()
    time.sleep(1)
