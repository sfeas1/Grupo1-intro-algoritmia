import random

# Validación de cantidad mínima
N = int(input("Ingrese la cantidad de competidores (mínimo 3): "))
while N < 3:
    print("Debe ingresar al menos 3 competidores.")
    N = int(input("Ingrese la cantidad de competidores (mínimo 3): "))

# Ingreso del récord actual
print("\n====================")
print("   RECORD ACTUAL  ")
print("====================\n")
horas_r = int(input("Horas: "))
minutos_r = int(input("Minutos (0-59): "))
while minutos_r < 0 or minutos_r > 59:
    print("Valor inválido.")
    minutos_r = int(input("Minutos (0-59): "))
segundos_r = int(input("Segundos (0-59): "))
while segundos_r < 0 or segundos_r > 59:
    print("Valor inválido.")
    segundos_r = int(input("Segundos (0-59): "))

record_seg = horas_r * 3600 + minutos_r * 60 + segundos_r

# Lista de competidores y estructura por país
competidores = []
tiempos_por_pais = {}

print("\n====================")
print("   COMPETIDORES  ")
print("====================\n")

for i in range(N):
    print("\nCompetidor", i + 1)
    nombre = input("Nombre del ciclista: ")
    numero = int(input("Número identificatorio: "))
    pais = input("País del competidor: ")

    # Generación aleatoria del tiempo
    horas = random.randint(0, 3)
    minutos = random.randint(0, 59)
    segundos = random.randint(0, 59)
    tiempo_seg = horas * 3600 + minutos * 60 + segundos

    print("Tiempo generado:", horas, "h", minutos, "min", segundos, "seg")

    # Guardar en la lista
    competidores.append({
        "nombre": nombre,
        "numero": numero,
        "pais": pais,
        "tiempo_seg": tiempo_seg
    })

    # Acumular tiempo por país
    if pais not in tiempos_por_pais:
        tiempos_por_pais[pais] = {"suma": 0, "cantidad": 0}
    tiempos_por_pais[pais]["suma"] += tiempo_seg
    tiempos_por_pais[pais]["cantidad"] += 1

# Ordenar por tiempo (de menor a mayor)
def obtener_tiempo(competidor):
    return competidor["tiempo_seg"]

competidores.sort(key=obtener_tiempo)
# Mostrar si el mejor tiempo supera el récord
mejor = competidores[0]
if mejor["tiempo_seg"] < record_seg:
    print("\n🎉 Hay nuevo record!")
    print("Lo supero", mejor["nombre"], "| El competidor número:", mejor["numero"], "| De", mejor["pais"])
else:
    print("\n El récord actual sigue vigente")

# Mostrar podio (Top 3)
print("\n====================")
print("      PODIO TOP 3    ")
print("====================\n")
for i in range(3):
    c = competidores[i]
    h = c["tiempo_seg"] // 3600
    m = (c["tiempo_seg"] % 3600) // 60
    s = c["tiempo_seg"] % 60
    print(f"{i+1}° - {c['nombre']} (#{c['numero']}, {c['pais']}) - {h}h {m}m {s}s")

# Promedio por país
print("\n====================")
print(" PROMEDIO POR PAÍS ")
print("====================\n")
for pais in tiempos_por_pais:
    suma = tiempos_por_pais[pais]["suma"]
    cant = tiempos_por_pais[pais]["cantidad"]
    promedio = suma // cant
    h = promedio // 3600
    m = (promedio % 3600) // 60
    s = promedio % 60
    print(f"{pais}: {h}h {m}m {s}s")
