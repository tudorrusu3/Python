import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA
import matplotlib.pyplot as plt

# Încarcă datele din fișierul CSV
df = pd.read_csv('fifa_2023.csv')

# Alegeți variabilele relevante pentru CCA
X_columns = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']
Y_columns = ['Rating']

# Extrage datele relevante
X = df[X_columns].values
Y = df[Y_columns].values

# Inițializează CCA cu n_components=1
cca = CCA(n_components=1)
X_c, Y_c = cca.fit_transform(X, Y)

# Plotează prima pereche de variabile canonice
plt.scatter(X_c, Y_c)
plt.xlabel('X_c1')
plt.ylabel('Y_c1')
plt.title('Perechea de variabile canonice')
plt.show()
