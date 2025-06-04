# Ingreso de la cantidad de competidores
N = int(input("Ingrese la cantidad de competidores: "))

# Inicialización de variables
ganador_num = 0
ganador_tiempo_seg = None
suma_tiempos_seg = 0

# Lista para almacenar datos de los competidores
competidores = [] 

print("\n====================")
print("   RECORD ACTUAL  ")
print("====================\n")

print("Ingrese el récord actual:")
horas_r = int(input("Horas: "))
minutos_r = int(input("Minutos (0-59): "))
while minutos_r < 0 or minutos_r > 59:
    print("Valor inválido. Debe estar entre 0 y 59.")
    minutos_r = int(input("Minutos (0-59): "))
segundos_r = int(input("Segundos (0-59): "))
while segundos_r < 0 or segundos_r > 59:
    print("Valor inválido. Debe estar entre 0 y 59.")
    segundos_r = int(input("Segundos (0-59): "))

record_seg = horas_r * 3600 + minutos_r * 60 + segundos_r

print("\n====================")
print("   COMPETIDORES  ")
print("====================\n")

for i in range(N):
    print("\nCompetidor", i + 1)
    numero = int(input("Número identificatorio: "))
    pais = input("País del competidor: ")
    horas = int(input("Horas: "))
    minutos = int(input("Minutos (0-59): "))
    while minutos < 0 or minutos > 59:
        print("Valor inválido. Debe estar entre 0 y 59.")
        minutos = int(input("Minutos (0-59): "))
    segundos = int(input("Segundos (0-59): "))
    while segundos < 0 or segundos > 59:
        print("Valor inválido. Debe estar entre 0 y 59.")
        segundos = int(input("Segundos (0-59): "))

    tiempo_seg = horas * 3600 + minutos * 60 + segundos
    suma_tiempos_seg += tiempo_seg

    # Guardar información del competidor
    competidores.append({'numero': numero, 'pais': pais, 'tiempo_seg': tiempo_seg})

    # Determinar si es el ganador
    if ganador_tiempo_seg is None or tiempo_seg < ganador_tiempo_seg:
        ganador_tiempo_seg = tiempo_seg
        ganador_num = numero

# Mostrar resultados
ganador_h = ganador_tiempo_seg // 3600
ganador_m = (ganador_tiempo_seg % 3600) // 60
ganador_s = ganador_tiempo_seg % 60

print("\n====================")
print("   RESULTADOS  ")
print("====================\n")

print("Ganador: Competidor", ganador_num)
print("Tiempo del ganador: ", ganador_h, "h", ganador_m, "m", ganador_s, "s")

if ganador_tiempo_seg < record_seg:
    print("¡El ganador superó el récord anterior!")
else:
    print("El ganador no superó el récord anterior.")

# Calcular y mostrar promedio general
promedio_seg = suma_tiempos_seg // N
prom_h = promedio_seg // 3600
prom_m = (promedio_seg % 3600) // 60
prom_s = promedio_seg % 60

print("Tiempo promedio general: ", prom_h, "h", prom_m, "m", prom_s, "s")

# Agrupar por país y calcular promedios
print("\n====================")
print(" PROMEDIO POR PAÍS ")
print("====================\n")

# Diccionario para almacenar suma de tiempos y cantidad por país
pais_tiempos = {}
for c in competidores:
    pais = c['pais']
    tiempo = c['tiempo_seg']
    if pais not in pais_tiempos:
        pais_tiempos[pais] = {'suma': 0, 'cantidad': 0}
    pais_tiempos[pais]['suma'] += tiempo
    pais_tiempos[pais]['cantidad'] += 1

# Mostrar promedios por país
for pais in pais_tiempos:
    suma = pais_tiempos[pais]['suma']
    cantidad = pais_tiempos[pais]['cantidad']
    promedio = suma // cantidad
    h = promedio // 3600
    m = (promedio % 3600) // 60
    s = promedio % 60
    print("País:", pais)
    print("Promedio: ", h, "h", m, "m", s, "s")
    print()
