import citire
import matplotlib.pyplot as plt
import seaborn as sns

def genereaza_statistici_si_grafice(file_path):
    df = citire.incarca_date(file_path)
    df_tratat = citire.tratare_date(df)

    print("Statistici descriptive:")
    print(df_tratat.describe())


    plt.figure(figsize=(10, 6))
    sns.histplot(df_tratat['PAC'], bins=20, kde=True, color='skyblue')
    plt.title('Distribuția Vitezei FIFA Players')
    plt.xlabel('Viteză PAC')
    plt.ylabel('Număr de Jucători')
    plt.show()

    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_tratat[['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']])
    plt.title('Statistici de Bază pentru PAC, SHO, PAS, DRI, DEF, PHY')
    plt.xlabel('Statistici de Bază')
    plt.ylabel('Valoare')
    plt.show()

    numeric_columns = df_tratat.select_dtypes(include=['number']).columns
    correlation_matrix = df_tratat[numeric_columns].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matrice de Corelație între Atributele FIFA Players')
    plt.show()

    alegere = input("Doriți să vedeți următoarea etapă? (da/nu): ").lower()
    if alegere == 'da':
        # Adăugați aici codul pentru următoarea etapă sau set de date
        print("Implementați aici următoarea etapă sau set de date.")
    else:
        print("Programul se încheie.")

if __name__ == "__main__":
    file_path = 'FIFA_2023.csv'
    genereaza_statistici_si_grafice(file_path)
