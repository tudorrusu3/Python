import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import mplcursors

# Citirea setului de date
data = pd.read_csv('Set_date_curatat.csv')

# Definirea datelor pentru plot
name_column = data['name']
card_type = data['card_type']
X = data[['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']]
y = data['rating']

# Filtrarea datelor pentru rating între 94 și 99
filtered_data = data[(data['rating'] >= 94) & (data['rating'] <= 99)]
filtered_X = filtered_data[['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']]
filtered_y = filtered_data['rating']

# Crearea modelului LDA
model = LinearDiscriminantAnalysis()
data_plot = model.fit(filtered_X, filtered_y).transform(filtered_X)

# Definirea unei scheme de culori corespunzătoare rating-urilor
color_scheme = {94: 'purple', 95: 'yellow', 96: 'orange', 97: 'blue', 98: 'green', 99: 'red'}

# Afișare rating-uri și culori corespunzătoare
print("Rating-urile și culorile corespunzătoare:")
for rating, color in color_scheme.items():
    print(f"Rating: {rating}, Culoare: {color}")

# Crearea plotului LDA
plt.figure()

# Crearea unei liste pentru a ține evidența de punctele din legenda
legend_points = {}

for rating, color in color_scheme.items():
    points = plt.scatter(data_plot[filtered_y == rating, 0], data_plot[filtered_y == rating, 1], alpha=.8, color=color)
    legend_points[f'Rating {rating}'] = points

# Adăugarea legendei la plot
plt.legend(legend_points.values(), legend_points.keys(), loc='best', shadow=False, scatterpoints=1)
plt.title('LDA jucatori cuprinsi intre 94 si 99 rating')
plt.xlabel('Atribute LDA')
plt.ylabel('Rating LDA')

mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(
    f"Name: {name_column[filtered_y.index[sel.target.index]]} \nPromotion: {card_type[filtered_y.index[sel.target.index]]}"
))

plt.show()
