import pandas as pd
import matplotlib.pyplot as plt

# Creazione del DataFrame dai dati forniti
data = {
    'district': ['101-Bois-de-Liesse', '102-Cap-Saint-Jacques', '11-Sault-au-Récollet', '111-Mile-End', '112-DeLorimier'],
    'Coderre': [2481, 2525, 3348, 1734, 1770],
    'Bergeron': [1829, 1163, 2770, 4782, 5933],
    'Joly': [3024, 2675, 2532, 2514, 3044],
    'total': [7334, 6363, 8650, 9030, 10747],
    'winner': ['Joly', 'Joly', 'Coderre', 'Bergeron', 'Bergeron'],
    'result': ['plurality', 'plurality', 'plurality', 'majority', 'majority'],
    'district_id': [101, 102, 11, 111, 112]
}

df = pd.DataFrame(data)

# Grafico a barre confronto voti totali per candidato
total_votes = df.groupby('winner').sum()[['Coderre', 'Bergeron', 'Joly']]
total_votes.plot(kind='bar', stacked=True)
plt.title('Confronto Voti Totali per Candidato')
plt.xlabel('Candidato')
plt.ylabel('Voti Totali')
plt.legend(title='Candidato')
plt.savefig('confronto_voti_totali.png', dpi=300)
plt.show()

# Grafico a barre confronto numero votanti per distretto
voters_per_district = df.groupby('district')['total'].sum()
voters_per_district.plot(kind='bar', color='purple')
plt.title('Numero di Votanti per Distretto')
plt.xlabel('Distretto')
plt.ylabel('Numero di Votanti')
plt.savefig('numero_votanti_per_distretto.png', dpi=300)
plt.show()

# Grafico a barre comparativo voti primi 4 distretti per candidato (formato appaiato)
top_4_districts = df.groupby('district').head(4)
votes_per_candidate_per_district = top_4_districts.groupby(['district', 'winner']).sum().unstack()['total']
votes_per_candidate_per_district.plot(kind='bar')
plt.title('Confronto Voti Primi 4 Distretti per Candidato (Appaiato)')
plt.xlabel('Distretto')
plt.ylabel('Voti')
plt.legend(title='Candidato')
plt.savefig('confronto_voti_primi_4_distretti_appaiato.png', dpi=300)
plt.show()

# Grafico a barre comparativo voti primi 4 distretti per candidato (formato impilato)
votes_per_candidate_per_district.plot(kind='bar', stacked=True)
plt.title('Confronto Voti Primi 4 Distretti per Candidato (Impilato)')
plt.xlabel('Distretto')
plt.ylabel('Voti')
plt.legend(title='Candidato')
plt.savefig('confronto_voti_primi_4_distretti_impilato.png', dpi=300)
plt.show()
