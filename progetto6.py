#Visualizza la distribuzione di acquisto per età
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Amazon Customer Behavior Survey (1).csv')
eta_counts = dataset['age'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(eta_counts.index, eta_counts*100/sum(eta_counts),color='#4F9E19',edgecolor='black', alpha=0.7)
plt.title('Amazon Customers Age')
plt.xlabel('Age')
plt.ylabel('Percentage of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()