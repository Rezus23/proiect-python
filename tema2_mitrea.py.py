import pandas as pd
import matplotlib.pyplot as plt


Y = 11  
X = 6 

df = pd.read_csv('data.csv')
colors = {'Durata': 'pink', 'Puls': 'aqua', 'MaxPuls': 'red', 'Calorii': 'purple'}

df.plot(title='Valorile', color=[colors[i] for i in df.columns])
plt.show() 

df.head(X).plot(title=f'primele {X} valori')
plt.show()

plt.style.use('grayscale')
df.tail(Y)[['Durata', 'Puls']].plot(title=f'ultimele {Y} valori pentru  Durata si Puls')
plt.show()