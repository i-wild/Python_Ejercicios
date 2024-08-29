import time
import datetime
import msvcrt  # Módulo estándar de Python para Windows

# simulación de un reloj
H = 0  # Horas
M = 0  # Minutos
S = 0  # Segundos
esc_counter = 0  # Contador para detectar presiones de ESC

print("Presiona ESC dos veces para salir")

while True:
    # Comprobar si una tecla ha sido presionada
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\x1b':  # Código ASCII para ESC
            esc_counter += 1
            if esc_counter == 2:
                print("\nSaliendo...")
                break
        else:
            esc_counter = 0  # Resetear contador si se presiona otra tecla

    # Aumentar segundos
    S += 1
    time.sleep(1)
    if S == 60:
        S = 0
        M += 1
    # Aumentar minutos
    if M == 60:
        S = 0
        M = 0
        H += 1
    # Aumentar horas
    if H == 24:
        S = 0
        M = 0
        H = 0
    if H == 23 and M == 59 and S == 59:
        break
    # Formatear la hora
    hora_formateada = datetime.datetime(1, 1, 1, H, M, S).strftime("%H:%M:%S")
    print(hora_formateada, end="", flush=True)
    print("\r", end="", flush=True)
