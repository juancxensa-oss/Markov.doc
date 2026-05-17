import numpy as np

# Estados
estados = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición
P = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.3, 0.3, 0.4]
])

# Función para cambiar de estado
def siguiente_estado(estado_actual):
    return np.random.choice(estados, p=P[estado_actual])

# Simulación
estado_actual = 0  # empezamos en soleado
simulacion = []

for i in range(100):
    simulacion.append(estados[estado_actual])
    estado_actual = estados.index(siguiente_estado(estado_actual))

print(simulacion)