import numpy as np
from manim import *

# Define o campo vetorial
def f(x, y):
    return np.array([1, 1])

# Crie um grid de pontos no plano
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# Crie um vetor para cada ponto do grid
U = np.zeros((X.shape[0], X.shape[1], 2))
V = np.zeros((X.shape[0], X.shape[1], 2))
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        U[i, j, :] = f(X[i, j], Y[i, j])
        V[i, j, :] = f(X[i, j], Y[i, j])

# Crie a animação
def animate(scene):
    scene.set_camera_position([0, 0, 10])
    scene.set_camera_angle(0)
    scene.add_axes()
    scene.add_grid()
    scene.add_vectors(U, V, color='blue')
    scene.render()

# Execute a animação
animate(scene) # Execute a animação