import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Încarcă datele din fișierul CSV
df_filled = pd.read_csv('fifa_2023.csv')

# Elimină coloanele non-numerice sau cu date lipsă (dacă este necesar)
# De exemplu, eliminăm coloanele 'Name', 'Type 1', 'Type 2', 'Legendary'
df_filled = df_filled.select_dtypes(include=['number']).dropna(axis=1)

# Standardează datele pentru a le aduce la aceeași scară
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_filled)

# Crează instanța PCA și aplică fit pe datele standardizate
pca = PCA()
pca.fit(df_scaled)

# Afișează procentajul varianței explicată de fiecare componentă principală
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.8, align='center')
plt.title('Procentajul Varianței Explicată de Fiecare Componentă Principală')
plt.xlabel('Componenta Principală')
plt.ylabel('Procentajul Varianței Explicată')

# Afișează suma cumulată a proporțiilor varianței explicată
cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()
plt.subplot(1, 2, 2)
plt.plot(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance, marker='o', linestyle='-', color='b')
plt.title('Suma Cumulată a Proportiilor Varianței Explicată')
plt.xlabel('Numărul de Componente Principale')
plt.ylabel('Suma Cumulată a Proportiilor Varianței Explicată')

plt.tight_layout()
plt.show()

# Poți alege numărul de componente principale bazat pe suma cumulată a proporțiilor varianței explicată
# De exemplu, dacă vrei să păstrezi 95% din varianța totală, alegi numărul de componente corespunzător
num_components_for_95_variance = len(cumulative_explained_variance[cumulative_explained_variance <= 0.95])

# Creează un nou obiect PCA cu numărul ales de componente principale și aplică fit_transform pe date
pca_with_selected_components = PCA(n_components=num_components_for_95_variance)
df_pca = pca_with_selected_components.fit_transform(df_scaled)

# Poți continua analiza ACP sau utiliza datele transformate (df_pca) în analize ulterioare
