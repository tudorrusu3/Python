import sys
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv('fifa_2023.csv')

x_column = 'PAC'
y_column = 'PHY'
name_column = 'name'

df_filtered = df[df['DEF'] > 80]

x = df_filtered[x_column].values
y = df_filtered[y_column].values
names = df_filtered[name_column].values

scatter = plt.scatter(x, y, label=names)
plt.title(f'Scatter Plot pentru {x_column} vs {y_column} (cu DEF > 80)')
plt.xlabel(x_column)
plt.ylabel(y_column)

mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(
    f"Name: {names[sel.target.index]}\nPace: {x[sel.target.index]}\nPhysical: {y[sel.target.index]}"
))

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
