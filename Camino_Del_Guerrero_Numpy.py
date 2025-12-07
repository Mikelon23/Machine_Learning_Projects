import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)

# ==========================================
# 1. PREPARACIÓN DE DATOS (XOR)
# ==========================================
# Inputs (4 ejemplos, 2 características cada uno)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Targets (Lo que queremos que aprenda) - (4 ejemplos, 1 respuesta)
# XOR: 0, 1, 1, 0
y = np.array([[0], [1], [1], [0]])

# ==========================================
# 2. ARQUITECTURA DE LA RED
# ==========================================
# Definimos la Sigmoide y su derivada (para el Backpropagation)

