import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


df_filled = pd.read_csv('fifa_2023.csv')


df_filled = df_filled.select_dtypes(include=['number']).dropna(axis=1)


scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_filled)


pca = PCA()
pca.fit(df_scaled)


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
bars = plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.8, align='center')
plt.title('Procentajul Varianței Explicată de Fiecare Componentă Principală')
plt.xlabel('Componenta Principală')
plt.ylabel('Procentajul Varianței Explicată')


for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.01,
             f'{pca.explained_variance_ratio_[i]*100:.2f}%', ha='center', color='black')


cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()
plt.subplot(1, 2, 2)
line = plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o', linestyle='-', color='b')
plt.title('Suma Cumulată a Proportiilor Varianței Explicată')
plt.xlabel('Numărul de Componente Principale')
plt.ylabel('Suma Cumulată a Proportiilor Varianței Explicată')


for i, point in enumerate(line[0].get_data()[1]):
    plt.text(i + 1, point + 0.005, f'{point*100:.2f}%', ha='center', color='black')

plt.tight_layout()
plt.show()

