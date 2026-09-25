import numpy as np
import matplotlib.pyplot as plt

# Intervalo de tiempo
t = np.linspace(0, 5, 500)

# Función original
h = -5*t**2 + 20*t + 2

# Segunda función
h2 = -5*t**2 + 20*t + 5

# Puntos importantes de la función original
t_inicial = 0
h_inicial = 2

t_vertice = 2
h_vertice = 22

t_raiz_1 = -0.098
t_raiz_2 = 4.098

# Crear gráfica
plt.figure(figsize=(10, 6))

# Graficar funciones
plt.plot(t, h, label='h(t) = -5t² + 20t + 2')
plt.plot(t, h2, label='h₂(t) = -5t² + 20t + 5')

# Marcar valor inicial
plt.scatter(t_inicial, h_inicial, s=60, label='Valor inicial (0, 2)')

# Marcar vértice
plt.scatter(t_vertice, h_vertice, s=60, label='Vértice (2, 22)')

# Marcar raíz que aparece en el intervalo 0 <= t <= 5
plt.scatter(t_raiz_2, 0, s=60, label='Raíz ≈ (4.098, 0)')

# Eje de simetría
plt.axvline(x=2, linestyle='--', label='Eje de simetría: t = 2')

# Etiquetas
plt.xlabel('Hora (t)')
plt.ylabel('Pasajeros (miles)')
plt.title('Cantidad de pasajeros del sistema de transporte')

plt.grid(True)
plt.legend()
plt.xlim(0, 5)

plt.show()