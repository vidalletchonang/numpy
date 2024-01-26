import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del dataset Titanic
titanic = sns.load_dataset('titanic')
titanic['age'] = titanic['age'].fillna(titanic['age'].mean())

# Quanti ponti c'erano sulla nave?
numero_di_ponti = titanic['embarked'].nunique()
print(f"C'erano {numero_di_ponti} ponti sulla nave.")

# Ci sono dati mancanti? Dove? Quanti?
dati_mancanti = titanic.isnull().sum()
print("Dati mancanti:")
print(dati_mancanti)

# Logica per gestire i dati mancanti:
# Per 'age', potremmo sostituire i valori mancanti con la media dell'età.
# Per 'embarked', potremmo eliminare le righe con dati mancanti.
titanic.dropna(subset=['embarked'], inplace=True)

# Verifica che i dati mancanti siano stati gestiti
dati_mancanti_dopo_gestione = titanic.isnull().sum()
print("Dati mancanti dopo gestione:")
print(dati_mancanti_dopo_gestione)

# Tramite seaborn visualizziamo un lmplot su age e fare
sns.lmplot(x='age', y='fare', data=titanic, hue='sex', fit_reg=False)
plt.title('Scatter Plot tra Età e Tariffa con divisione per Sesso')
plt.show()
