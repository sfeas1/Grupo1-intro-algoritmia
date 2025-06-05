# TPO - Introduccion a la algoritmia - Grupo 1



# Simulación de Carrera de Ciclistas

Este programa simula una carrera de ciclistas en la que participan `N` competidores. El usuario debe ingresar la cantidad de participantes, los datos de cada ciclista (nombre, número identificatorio y país), y el tiempo récord anterior de la competencia. 

## Funcionalidad principal

Por cada ciclista, el programa:

- Genera automáticamente un **tiempo aleatorio** de carrera (en horas, minutos y segundos).
- Calcula el **tiempo total en segundos** para facilitar comparaciones.

Al finalizar la carga de todos los competidores, el programa:

1. **Determina al ganador** (el competidor con menor tiempo total).
2. **Compara el tiempo del ganador** con el récord ingresado por el usuario e informa si fue superado.
3. **Muestra el podio (Top 3)** con sus tiempos individuales.
4. **Calcula el tiempo promedio por país**, considerando todos los competidores de cada nación.

## Agregados

- Los **tiempos de carrera son generados aleatoriamente** dentro de un rango realista (0 a 3 horas, 0 a 59 minutos, 0 a 59 segundos) utilizando la librería `random`, para simular de forma automática los resultados de la carrera.

## Validaciones

- Se exige un mínimo de 3 competidores.
- Se validan los valores del tiempo récord para evitar entradas inválidas.

## Integrantes

- Feas, Santiago.
- Ferreyra, Gennaro Martin.
- Gallo, Julian Gabriel.
- Prividera, Francisco.
- Rodriguez, Joaquin.
- Russo Guiot, Gabriel Marcelo.
- Vazquez, Pedro.