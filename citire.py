import pandas as pd

def incarca_date(file_path):
    return pd.read_csv(file_path)

def tratare_date(df):
    df = elimina_date_lipsa(df)
    df = elimina_duplicate(df)
    return df

def elimina_date_lipsa(df):
    return df.dropna()

def elimina_duplicate(df):
    return df.drop_duplicates()

def salveaza_date(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    file_path = 'fifa_2023.csv'
    df = incarca_date(file_path)
    df_tratat = tratare_date(df)
    salveaza_date(df_tratat, 'Set_date_curatat.csv')
