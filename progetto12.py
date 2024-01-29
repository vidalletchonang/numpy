import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset
df = pd.read_csv('Amazon Customer Behavior Survey (1).csv')

# Grafico KDE dell'indice di soddisfazione rispetto all'età
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
sns.displot(data=df, x='age', hue='Shopping_Satisfaction', kind="kde", height=6, multiple="fill",
            clip=(0, None), palette="ch:rot=-.25,hue=1,light=.80")
plt.xlabel('Age')
plt.ylabel('Percentuale di voti')
plt.show()
