import numpy as np
import pandas as pd

path_korpus = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg" \
              "/Sprachtechnologie/Projekte/Masterarbeit remastered/Masterarbeit bereinigt - Kopie.xlsx"

df_korpus = pd.read_excel(path_korpus)

print(df_korpus.shape) #Alle Zeilen und Spalten da

print(df_korpus.isnull().sum()) #Alle Werte da

print(df_korpus.duplicated())
doppelreihe=df_korpus.duplicated() #Keine doppelten Reihen

df_korpus.convert_dtypes(infer_objects=True, convert_string=True,
                convert_integer=True, convert_boolean=True, convert_floating=True, dtype_backend='numpy_nullable')
print(df_korpus.dtypes) #Datentypen korrigieren


#Statistische Kennwerte: Lage- und Streuungsmaße, Verteilung, Ausreißer

print(df_korpus.describe(include=np.number))
print(df_korpus.Token)

#Ausreißer entdecken

##Spannweite für jede Spalte mit numerischen Werten ermitteln

#df_korpus.describe([x*0.1 for x in range(19)])
#TODO Andere Funktion finden, um Spannweiten zu ermitteln