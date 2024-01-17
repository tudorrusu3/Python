import sys
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Încarcă datele din fișierul CSV
df = pd.read_csv('fifa_2023.csv')

# Alegeți coloanele pentru x, y și numele jucătorului
x_column = 'PAC'
y_column = 'PHY'
name_column = 'name'

df_filtered = df[df['DEF'] > 80]

# Extrage valorile pentru x, y și numele jucătorului din datele filtrate
x = df_filtered[x_column].values
y = df_filtered[y_column].values
names = df_filtered[name_column].values

# Creează un scatter plot
scatter = plt.scatter(x, y, label=names)
plt.title(f'Scatter Plot pentru {x_column} vs {y_column} (cu DEF > 80)')
plt.xlabel(x_column)
plt.ylabel(y_column)

# Adaugă etichete la puncte cu mplcursors
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(names[sel.target.index]))

# Afișează graficul sau salvează-l într-un fișier
plt.show()

# Două linii pentru a face compilatorul capabil să deseneze
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
