import pandas as pd

path_korpus = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg" \
              "/Sprachtechnologie/Projekte/Masterarbeit remastered/Masterarbeit bereinigt - Kopie.xlsx"

df_korpus = pd.read_excel(path_korpus)


print(df_korpus.dtypes)


