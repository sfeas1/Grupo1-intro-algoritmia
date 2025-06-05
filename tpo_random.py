import random

nombres = [
    "Alejandro",
    "Juan",
    "Pedro",
    "Luis",
    "Carlos",
    "Eduardo",
    "Miguel",
    "José",
    "Francisco",
    "Antonio",
    "Diego",
    "Martín",
    "Adrián",
    "Daniel",
    "Andrés",
    "Rafael",
    "Jorge",
    "Sergio",
    "Pablo",
    "Víctor",
    "Alberto",
    "Fernando",
    "Raúl",
    "David",
    "Guillermo",
    "Ignacio",
    "Joaquín",
    "Nicolás",
    "Ricardo",
    "Rubén",
    "Santiago",
    "Tomás",
    "Sebastián",
    "Bruno",
    "Manuel",
    "Esteban",
    "Óscar",
    "Héctor",
    "Germán",
    "Cristian",
    "Javier",
    "Julio",
    "Hugo",
    "Marcos",
    "Benjamín",
    "Emilio",
    "Felipe",
    "Enrique",
    "Ramón",
    "Román",
    "María",
    "Ana",
    "Laura",
    "Sofía",
    "Carmen",
    "Lucía",
    "Paula",
    "Elena",
    "Sara",
    "Claudia",
    "Marta",
    "Natalia",
    "Isabel",
    "Julieta",
    "Valentina",
    "Victoria",
    "Andrea",
    "Carolina",
    "Gabriela",
    "Daniela",
    "Julia",
    "Patricia",
    "Beatriz",
    "Raquel",
    "Silvia",
    "Emma",
    "Alicia",
    "Lorena",
    "Vanessa",
    "Ángela",
    "Nuria",
    "Teresa",
    "Rosa",
    "Alejandra",
    "Mónica",
    "Inés",
    "Sandra",
    "Sonia",
    "Pilar",
    "Verónica",
    "Jessica",
    "Gloria",
    "Estela",
    "Noelia",
    "Miriam",
    "Rebeca",
    "Lidia",
    "Catalina",
    "Eva",
    "Paloma"
]

apellidos = [
    "García",
    "Fernández",
    "Rodríguez",
    "López",
    "Martínez",
    "Pérez",
    "Gómez",
    "Díaz",
    "Sánchez",
    "Romero",
    "González",
    "Torres",
    "Álvarez",
    "Castro",
    "Herrera",
    "Ramírez",
    "Flores",
    "Vargas",
    "Medina",
    "Suárez",
    "Mendoza",
    "Morales",
    "Ruiz",
    "Aguilar",
    "Alonso",
    "Andrade",
    "Arias",
    "Avila",
    "Ayala",
    "Barrera",
    "Benítez",
    "Blanco",
    "Cabrera",
    "Campos",
    "Cano",
    "Cárdenas",
    "Cortés",
    "Delgado",
    "Duarte",
    "Escobar",
    "Espinosa",
    "Farías",
    "Ferraro",
    "Godoy",
    "Guerrero",
    "Gutiérrez",
    "Iglesias",
    "Jiménez",
    "León",
    "Lucero",
    "Machado",
    "Maldonado",
    "Márquez",
    "Molina",
    "Montoya",
    "Morán",
    "Moretti",
    "Moreno",
    "Núñez",
    "Ortiz",
    "Paredes",
    "Patiño",
    "Pereira",
    "Ponce",
    "Quiroga",
    "Ramos",
    "Rivas",
    "Rosso",
    "Russo",
    "Salazar",
    "Salinas",
    "Santos",
    "Silva",
    "Soto",
    "Tapia",
    "Valdez",
    "Valencia",
    "Vega",
    "Velázquez",
    "Vera",
    "Villalba",
    "Villanueva",
    "Yáñez",
    "Vázquez",
    "Serrano",
    "Noguera",
    "Pizarro",
    "Sosa",
    "Cabré",
    "Beltrán",
    "Castañeda",
    "Cervantes",
    "Correa",
    "Cuevas",
    "Figueroa",
    "Dávila",
    "Escudero",
    "Bustos",
    "Caputo",
    "Ferrari"
]

paises = [
    "Argentina",
    "Bolivia",
    "Brasil",
    "Chile",
    "Colombia",
    "Ecuador",
    "Paraguay",
    "Perú",
    "Uruguay",
    "Venezuela"
]

# Ordenar por tiempo (de menor a mayor)
def obtener_tiempo(competidor):
    return competidor["tiempo_seg"]

def pedir_tiempo(hms, min, max):
    while True:
        valor = int(input(f"Ingresar {hms}: ({min}-{max}): "))

        if min <= valor <= max:
            return valor
        print("Valor inválido.")

def generar_nombre_random():
    nombre = nombres[random.randint(0,99)]
    apellido = apellidos[random.randint(0,99)]
    return (f"{nombre} {apellido}")

def pais_random():
    return paises[random.randint(0,9)]

# Validación de cantidad mínima
N = int(input("Ingrese la cantidad de competidores (mínimo 3): "))
while N < 3:
    print("Debe ingresar al menos 3 competidores.")
    N = int(input("Ingrese la cantidad de competidores (mínimo 3): "))

# Ingreso del récord actual
print("\n====================")
print("   RECORD ACTUAL  ")
print("====================\n")

horas_r = pedir_tiempo("Horas", 0, 3)
minutos_r = pedir_tiempo("Minutos", 0, 59)
segundos_r = pedir_tiempo("Segundos", 0, 59)

record_seg = horas_r * 3600 + minutos_r * 60 + segundos_r

# Lista de competidores y estructura por país
competidores = []
tiempos_por_pais = {}

print("\n====================")
print("   COMPETIDORES  ")
print("====================\n")

for i in range(N):
    numero = i + 1
    nombre = generar_nombre_random()
    pais = pais_random()

    print(f"\nCompetidor número: {numero}")
    print(f"Nombre del ciclista: {nombre}")
    print(f"País del competidor: {pais}")

    # Definir los rangos mínimos y máximos
    min_seg = 30 * 60                   # Mínimo de 30 minutos
    max_seg = (3 * 3600) + (59 * 60) + 59   # Máximo de 3 horas 59 minutos y 59 segundos

    # Generar un único número aleatorio entre el mínimo y el máximo
    tiempo_seg = random.randint(min_seg, max_seg)

    # Dividir el total en horas, minutos y segundos
    horas = tiempo_seg // 3600
    minutos = (tiempo_seg - (horas * 3600)) // 60
    segundos = (tiempo_seg - (horas * 3600)) - (minutos * 60)

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
    plural = ""
    if(cant > 1):
        plural = "es"
    print(f"{pais} ({cant} competidor{plural}): {h}h {m}m {s}s")
