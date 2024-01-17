import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv('fifa_2023.csv')

df_filtered = df[(df['rating'] > 60) & (df['DEF'] > 86)].copy()

X_columns = ['SHO']
Y_columns = ['rating']

X = df_filtered[X_columns].values
Y = df_filtered[Y_columns].values

cca = CCA(n_components=1)
X_c, Y_c = cca.fit_transform(X, Y)

df_filtered.loc[:, 'X_c1'] = X_c
df_filtered.loc[:, 'Y_c1'] = Y_c

scatter = plt.scatter(df_filtered['X_c1'], df_filtered['Y_c1'])
plt.title('Scatter Plot pentru Variabilele Canonice (cu rating > 87 și DEF > 86)')

plt.xlabel('SHOOTING')
plt.ylabel('RATING')

mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.
set_text(f"Name: {df_filtered['name'].iloc[sel.target.index]}\nCard Type: {df_filtered['card_type'].iloc[sel.target.index]}"))

plt.show()
