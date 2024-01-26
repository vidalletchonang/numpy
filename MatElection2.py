import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del dataset Titanic
titanic = sns.load_dataset('titanic')

# Numero di passeggeri per ogni classe di imbarco
sns.countplot(x='embarked', data=titanic)
plt.title('Numero di passeggeri per classe di imbarco')
plt.show()

# Numero di passeggeri per sopravvissuti/non sopravvissuti
sns.countplot(x='alive', data=titanic)
plt.title('Numero di passeggeri per sopravvissuti/non sopravvissuti')
plt.show()

# Distribuzione delle tariffe (fare)
sns.histplot(titanic['fare'], bins=30, kde=True)
plt.title('Distribuzione delle tariffe')
plt.xlabel('Tariffe')
plt.show()

# Distribuzione delle età rispetto alla classe di imbarco (boxplot)
sns.boxplot(x='class', y='age', data=titanic)
plt.title('Distribuzione delle età rispetto alla classe di imbarco')
plt.xlabel('Classe di imbarco')
plt.ylabel('Età')
plt.show()

# Distribuzione delle età rispetto alla classe di imbarco (swarmplot)
sns.swarmplot(x='class', y='age', data=titanic)
plt.title('Distribuzione delle età rispetto alla classe di imbarco')
plt.xlabel('Classe di imbarco')
plt.ylabel('Età')
plt.show()

# Boxplot e lmplot rispetto alle colonne fare e survived
sns.boxplot(x='survived', y='fare', data=titanic)
plt.title('Boxplot tra Fare e Survived')
plt.xlabel('Sopravvissuti (1) / Non sopravvissuti (0)')
plt.ylabel('Fare')
plt.show()

sns.lmplot(x='fare', y='survived', data=titanic, logistic=True)
plt.title('Regplot tra Fare e Survived')
plt.xlabel('Fare')
plt.ylabel('Survived')
plt.show()
