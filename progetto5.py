#Visualizza la distribuzione di acquisto per gender
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Amazon Customer Behavior Survey (1).csv')
gender_counts = dataset['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values,color='#008080')
plt.title('Amazon Customers Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.show()