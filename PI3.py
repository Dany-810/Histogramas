import numpy as np
import plotly.graph_objects as go

# Cargamos el array X_embedded que contiene los datos reducidos
X_embedded = np.load('X_embedded.npy')

# Cargamos el array y que contiene la columna objetivo
y = np.load('y.npy')

# Creamos una figura vacía
fig = go.Figure()

# Agregamos una traza de dispersión 3D para la clase vivo (y == 0)
fig.add_trace(go.Scatter3d(
    x=X_embedded[y == 0, 0],
    y=X_embedded[y == 0, 1],
    z=X_embedded[y == 0, 2],
    mode='markers',
    marker=dict(
        color='blue',
        size=5
    ),
    name='Vivo'
))

# Agregamos una traza de dispersión 3D para la clase muerto (y == 1)
fig.add_trace(go.Scatter3d(
    x=X_embedded[y == 1, 0],
    y=X_embedded[y == 1, 1],
    z=X_embedded[y == 1, 2],
    mode='markers',
    marker=dict(
        color='red',
        size=5
    ),
    name='Muerto'
))

# Definimos el título y los ejes del gráfico
fig.update_layout(
    title='Gráfico de dispersión 3D de los datos reducidos por TSNE',
    scene=dict(
        xaxis_title='Componente 1',
        yaxis_title='Componente 2',
        zaxis_title='Componente 3'
    )
)

# Mostramos el gráfico
fig.show()
