
import numpy as np
import matplotlib.pyplot as plt

# Crear los valores de x e y
x = np.linspace(0, np.sqrt(5), 500)
y = np.linspace(-2.6, 2.6, 500)

X, Y = np.meshgrid(x, y)

# Ecuación de la curva: y² = x²(5 - x²)
Z = Y**2 - X**2 * (5 - X**2)

# Graficar la curva
plt.figure(figsize=(9, 6))
plt.contour(X, Y, Z, levels=[0], colors='blue')

# Punto P(2,2)
plt.scatter(2, 2, color='red', s=70, label='Punto P(2,2)')

# Recta tangente: y = -3x + 8
x_t = np.linspace(0, np.sqrt(5), 300)
y_t = -3*x_t + 8

plt.plot(x_t, y_t, color='green',
         label='Recta tangente: y = -3x + 8')

# Configuración de la gráfica
plt.xlabel('Consumo de energía (MWh)')
plt.ylabel('Producción (miles de unidades)')
plt.title('Relación entre producción y consumo energético')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.show()
