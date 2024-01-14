import pandas as pd

# Încărcați setul de date (exemplu CSV)
df = pd.read_csv('Pokemon.csv')

# Verificați prezența datelor lipsă
print(df.isnull().sum())

# Eliminați rândurile cu date lipsă
df = df.dropna()




# Eliminați duplicatelor bazate pe toate coloanele
df = df.drop_duplicates()

# Eliminați duplicatelor bazate pe anumite coloane
# df = df.drop_duplicates(subset=['coloana1', 'coloana2'])









# Salvați setul de date curățat într-un nou fișier CSV
df.to_csv('nume_set_date_curatat.csv', index=False)
