import pandas as pd
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('data.csv')
df.plot(title='Toate valorile')
plt.show()
X = 5 
Y = 12
df.head(X).plot(title=f'primele {X} valori')
plt.show()
df.tail(Y)[['Durata', 'Puls']].plot(title=f'ultimele {Y} valori pentru  Durata si Puls')
plt.show()