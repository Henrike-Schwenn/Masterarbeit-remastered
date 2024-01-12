import numpy as np
import pandas as pd

path_korpus = "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg" \
              "/Projekte/Masterarbeit remastered/Korpus/" \
              "/Masterarbeit bereinigt - Kopie.xlsx"

df_korpus = pd.read_excel(path_korpus)

# Alle Zeilen und Spalten da
df_korpus.shape

# Alle Werte da
df_korpus.isnull().sum()

# Keine doppelten Reihen
df_korpus.duplicated()

# Datentypen korrigieren
df_korpus.convert_dtypes(
    infer_objects=True, convert_string=True, convert_integer=True,
    convert_boolean=True, convert_floating=True
)

# Leerzeichen aus Spaltenüberschriften entfernen
df_korpus.rename(columns={
    "Token": "token", "Datenquelle Token": "datenquelle_token",
    "Token belegt?": "token_belegt_?", "Sprache": "sprache", "POS": "pos",
    "Klasse": "klasse", "Stammvokal Graphem": "stammvokal_graphem",
    "Stammauslaut Graphem": "stammauslaut_graphem",
    "Dental Graphem": "dental_graphem",
    "Stammvokal standardisiert": "stammvokal_standardisiert",
    "Stammauslaut standardisiert": "stammauslaut_standardisiert",
    "Dental standardisiert": "dental_standardisiert",
    "Idg. Wurzel ID": "id_idg_wurzel",
    "Idg. Wurzel e-Stufe": "e_stufe_idg_wurzel",
    "Datenquelle idg. Wurzel e-Stufe": "datenquelle_e_stufe_idg_wurzel",
    "Idg. Wurzel o-Stufe": "o_stufe_idg_wurzel",
    "Datenquelle idg. Wurzel o-Stufe": "datenquelle_o_stufe_idg_wurzel",
    "Idg. Wurzel Nullstufe": "nullstufe_idg_wurzel",
    "Datenquelle idg. Wurzel Nullstufe": "datenquelle_nullstufe_idg_wurzel",
    "Anzahl Probleme Stammvokal Ringe": "ringe_stammvokal_probleme",
    "Anzahl Probleme Stammauslaut Ringe": "ringe_stammauslaut_probleme",
    "Anzahl Probleme Dental Ringe": "ringe_dental_probleme",
    "Anzahl Probleme Stammvokal Lühr": "lühr_stammvokal_probleme",
    "Anzahl Probleme Stammauslaut Lühr": "lühr_stammauslaut_probleme",
    "Anzahl Probleme Dental Lühr": "lühr_dental_probleme"
}, inplace=True)

# Statistische Kennwerte: Mittelwert, Standardabweichung, Min. und max.
# Werte, Quartile

#TODO id_idg_wurzel in object umwandeln, weil keine stetige numerische Variable
#df_probleme=df_korpus.loc[:,
# 'ringe_stammvokal_probleme':'lühr_dental_probleme']


kenndaten_probleme=df_korpus.ringe_stammvokal_probleme.describe(), df_korpus.lühr_stammvokal_probleme.describe()
#print(kenndaten_probleme)


# Ausreißer entdecken

# Spannweite für jede Spalte mit numerischen Werten ermitteln

# df_korpus.describe([x*0.1 for x in range(19)])
# TODO Andere Funktion finden, um Spannweiten zu ermitteln
