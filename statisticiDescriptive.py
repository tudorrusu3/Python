import citire
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

def genereaza_statistici_si_grafice(file_path):
    try:

        df = citire.incarca_date(file_path)
        df_tratat = citire.tratare_date(df)


        df_peste_90_pace = df_tratat[df_tratat['PAC'] > 90]


        print("Statistici descriptive:")
        print(df_tratat.describe())

        # Histogram
        plt.figure(figsize=(10, 6))
        sns.histplot(df_tratat['PAC'], bins=20, kde=True, color='skyblue')
        plt.title('Distribuția Vitezei FIFA Players')
        plt.xlabel('Viteză PAC')
        plt.ylabel('Număr de Jucători')
        plt.show()

        # Boxplot
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=df_tratat[['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']])
        plt.title('Statistici de Bază pentru PAC, SHO, PAS, DRI, DEF, PHY')
        plt.xlabel('Statistici de Bază')
        plt.ylabel('Valoare')
        plt.show()

        # Stripplot
        plt.figure(figsize=(12, 8))
        strip_plot = sns.stripplot(x='position', y='SHO', data=df_peste_90_pace, color='blue', alpha=0.7)
        plt.title('Distribuția Abilităților de Șut în funcție de Poziția Jucătorului (Peste 90 PAC)')
        plt.xlabel('Poziția Jucătorului')
        plt.ylabel('Valoare Abilitate')

        mplcursors.cursor(hover=True).connect("add", lambda sel: add_tooltip(df_peste_90_pace, sel))

        plt.show()

        # Scatterplot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='SHO', y='DRI', data=df_peste_90_pace, color='green')
        plt.title('Compararea Abilităților de Șut și Dribling')
        plt.xlabel('Abilitate de Șut (SHO)')
        plt.ylabel('Abilitate de Dribling (DRI)')

        mplcursors.cursor(hover=True).connect("add", lambda sel: add_tooltip(df_peste_90_pace, sel))

        plt.show()


        numeric_columns = df_tratat.iloc[1:].select_dtypes(include=['number']).columns
        correlation_matrix = df_tratat.iloc[1:][numeric_columns].drop(columns=['Jucator']).corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matrice de Corelație între Atributele FIFA Players')
        plt.show()


    except Exception as e:
        print(f"An error occurred: {e}")

def add_tooltip(df, sel):
    sel.annotation.set_text(
        f'Nume jucător: {df.iloc[sel.target.index]["name"]}\n'
        f'Tip card: {df.iloc[sel.target.index]["card_type"]}'
    )

if __name__ == "__main__":
    file_path = 'FIFA_2023.csv'
    genereaza_statistici_si_grafice(file_path)
