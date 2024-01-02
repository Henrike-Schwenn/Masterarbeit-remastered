import pandas as pd

path_korpus = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg" \
              "/Sprachtechnologie/Projekte/Masterarbeit remastered/Masterarbeit bereinigt - Kopie.xlsx"

df_korpus = pd.read_excel(path_korpus)

#Alle Zeilen und Spalten da?

print(df_korpus.shape) #483 Zeilen, 25 Spalten

#Fehlende Werte?

print(df_korpus.isnull().sum()) #Alle Werte da

#Doppelte Reihen?

print(df_korpus.duplicated())
doppelreihe=df_korpus.duplicated()
print("Das sind", doppelreihe) #Keine doppelten Reihen

#Ausreißer entdecken

##Spannweite für jede Spalte mit numerischen Werten ermitteln

df_korpus.describe([x*0.1 for x in range(19)])
#TODO Andere Funktion finden, um Spannweiten zu ermitteln