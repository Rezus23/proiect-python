import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')
df.plot(title='Toate valorile')
plt.show()
X = 5 
Y = 12
plt.style.use('seaborn-v0_8-darkgrid')
df.head(X).plot(title=f'primele {X} valori')
plt.style.use('ggplot')

plt.show()
df.tail(Y)[['Durata', 'Puls']].plot(title=f'ultimele {Y} valori pentru  Durata si Puls')
plt.show()
