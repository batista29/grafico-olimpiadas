import requests
import json
import numpy as np
import matplotlib.pyplot as plt

api = 'https://apis.codante.io/olympic-games/countries'
olimpiadas = requests.get(api)
olimpiadas = olimpiadas.json()

infos = olimpiadas['data']

nome = []
ouros = []

for pais in infos:
    nome.append(pais['name'])
    ouros.append(pais['gold_medals'])

x = np.arange(len(nome))

fig, ax = plt.subplots()

ax.bar(nome, ouros, width=1, color=['tab:red','tab:blue','tab:green', 'tab:orange'])

ax.set_ylabel('Medalhas de Ouro')
ax.set_xlabel('Países')
ax.set_title('Número de Medalhas de Ouro por País nas Olimpíadas')

plt.subplots_adjust(bottom=0.25)
ax.set_xticks(x)
ax.set_xticklabels(nome, rotation=90)

plt.show()