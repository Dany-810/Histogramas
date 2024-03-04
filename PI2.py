import matplotlib.pyplot as plt
import numpy as np

# Generamos vectores de variables aleatorias
anemia = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
diabetes = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
fumador = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
muerto = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí

# Graficamos las gráficas de torta usando subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].pie([np.sum(anemia == 0), np.sum(anemia == 1)], labels=['No', 'Sí'], autopct='%1.1f%%')
axs[0, 0].set_title('Cantidad de anémicos')
axs[0, 1].pie([np.sum(diabetes == 0), np.sum(diabetes == 1)], labels=['No', 'Sí'], autopct='%1.1f%%')
axs[0, 1].set_title('Cantidad de diabéticos')
axs[1, 0].pie([np.sum(fumador == 0), np.sum(fumador == 1)], labels=['No', 'Sí'], autopct='%1.1f%%')
axs[1, 0].set_title('Cantidad de fumadores')
axs[1, 1].pie([np.sum(muerto == 0), np.sum(muerto == 1)], labels=['No', 'Sí'], autopct='%1.1f%%')
axs[1, 1].set_title('Cantidad de muertos')

plt.suptitle('Gráficas de torta de las distribuciones de las variables')
plt.show()
