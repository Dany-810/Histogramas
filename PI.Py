import matplotlib.pyplot as plt
import numpy as np

# Generamos un vector de edades aleatorias
edades = np.random.randint(18, 80, size=1000)

# Graficamos el histograma de edades
plt.hist(edades)
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de edades')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Generamos vectores de variables aleatorias
anemia = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
diabetes = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
fumador = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
muerto = np.random.randint(0, 2, size=1000) # 0 = no, 1 = sí
genero = np.random.randint(0, 2, size=1000) # 0 = hombre, 1 = mujer

# Filtramos los vectores por género
anemia_h = anemia[genero == 0]
anemia_m = anemia[genero == 1]
diabetes_h = diabetes[genero == 0]
diabetes_m = diabetes[genero == 1]
fumador_h = fumador[genero == 0]
fumador_m = fumador[genero == 1]
muerto_h = muerto[genero == 0]
muerto_m = muerto[genero == 1]

# Graficamos los histogramas agrupados por género
fig, axs = plt.subplots(2, 2, figsize=(10, 10), sharey=True)
axs[0, 0].bar(['No', 'Sí'], [np.sum(anemia_h == 0), np.sum(anemia_h == 1)], width=0.4, align='edge', label='Hombre')
axs[0, 0].bar(['No', 'Sí'], [np.sum(anemia_m == 0), np.sum(anemia_m == 1)], width=-0.4, align='edge', label='Mujer')
axs[0, 0].set_ylabel('Cantidad de anémicos')
axs[0, 0].legend()

axs[0, 1].bar(['No', 'Sí'], [np.sum(diabetes_h == 0), np.sum(diabetes_h == 1)], width=0.4, align='edge', label='Hombre')
axs[0, 1].bar(['No', 'Sí'], [np.sum(diabetes_m == 0), np.sum(diabetes_m == 1)], width=-0.4, align='edge', label='Mujer')
axs[0, 1].set_ylabel('Cantidad de diabéticos')
axs[0, 1].legend()

axs[1, 0].bar(['No', 'Sí'], [np.sum(fumador_h == 0), np.sum(fumador_h == 1)], width=0.4, align='edge', label='Hombre')
axs[1, 0].bar(['No', 'Sí'], [np.sum(fumador_m == 0), np.sum(fumador_m == 1)], width=-0.4, align='edge', label='Mujer')
axs[1, 0].set_ylabel('Cantidad de fumadores')
axs[1, 0].legend()

axs[1, 1].bar(['No', 'Sí'], [np.sum(muerto_h == 0), np.sum(muerto_h == 1)], width=0.4, align='edge', label='Hombre')
axs[1, 1].bar(['No', 'Sí'], [np.sum(muerto_m == 0), np.sum(muerto_m == 1)], width=-0.4, align='edge', label='Mujer')
axs[1, 1].set_ylabel('Cantidad de muertos')
axs[1, 1].legend()

plt.suptitle('Histogramas agrupados por hombre y mujer')
plt.show()
