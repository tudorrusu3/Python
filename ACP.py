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
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.8, align='center')
plt.title('Procentajul Varianței Explicată de Fiecare Componentă Principală')
plt.xlabel('Componenta Principală')
plt.ylabel('Procentajul Varianței Explicată')

cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()
plt.subplot(1, 2, 2)
plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o', linestyle='-', color='b')
plt.title('Suma Cumulată a Proportiilor Varianței Explicată')
plt.xlabel('Numărul de Componente Principale')
plt.ylabel('Suma Cumulată a Proportiilor Varianței Explicată')

plt.tight_layout()
plt.show()

num_components_for_95_variance = len(cumulative_explained_variance[cumulative_explained_variance <= 0.95])

pca_with_selected_components = PCA(n_components=num_components_for_95_variance)
df_pca = pca_with_selected_components.fit_transform(df_scaled)

