import numpy as np
import matplotlib.pyplot as plt

# Tramo 1: x < 1
x1 = np.linspace(-2, 1, 400, endpoint=False)
y1 = 2*x1 + 4

# Tramo 2: 1 <= x < 3
x2 = np.linspace(1, 3, 400, endpoint=False)
y2 = x2**2 + 2

# Tramo 3: x >= 3
x3 = np.linspace(3, 6, 400)
y3 = x3 + 8

plt.figure(figsize=(9, 6))

plt.plot(x1, y1, label='2x + 4, x < 1')
plt.plot(x2, y2, label='x² + 2, 1 ≤ x < 3')
plt.plot(x3, y3, label='x + 8, x ≥ 3')

# Extremos en x = 1
plt.plot(1, 6, marker='o', markerfacecolor='white',
         markeredgecolor='black', markersize=8)
plt.plot(1, 3, 'o', color='black', markersize=8)

# Extremos en x = 3
plt.plot(3, 11, marker='o', markerfacecolor='white',
         markeredgecolor='black', markersize=8)
plt.plot(3, 11, 'o', color='black', markersize=5)

plt.xlim(-2, 6)
plt.ylim(-1, 16)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Continuidad de una función definida por tramos')
plt.grid(True)
plt.legend()
plt.show()