import requests
import pandas as pd
import sys
import collections
import numpy as np


#url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
url = sys.argv[1]

r = requests.get(url,verify=False)
r_text = r.text.replace('\\r\\n', '').replace('"\r\n}', '').replace('{\r\n  "html": "', '')


df = pd.read_html(r_text)
df1 = df
df = df[0].copy()
df = df[df['Bola1']==df['Bola1']].reset_index(drop=True)


nr_pop = list(range(1,26))
nr_pares = []
nr_impares = []
nr_primos = []


for i in nr_pop:
    if i%2 == 0:
        nr_pares.append(i)
    else:
        nr_impares.append(i)

    cont = 0
    for j in nr_pop:
        if i%j == 0:
            cont+=1 
    if cont <= 2 and i!=1:
        nr_primos.append(i)

comb = []
v_01,v_02,v_03,v_04,v_05,v_06,v_07,v_08,v_09,v_10,v_11,v_12,v_13,v_14,v_15,v_16,v_17,v_18,v_19,v_20,v_21,v_22,v_23,v_24,v_25 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 



lst_campos = []
for i in range(1,16):
    lst_campos.append('Bola'+f'{i}')


for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0

    for campo in lst_campos:
        if int(row[campo]) in nr_pares:
            v_pares += 1
        if int(row[campo]) in nr_impares:
            v_impares += 1
        if int(row[campo]) in nr_pares:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-' + str(v_primos) + 'np')



    freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]

freq_nr.sort(key=lambda tup: tup[1])
freq_nr[0] # primeiro (numero mais frequente)
freq_nr[-1] # ultimo (numero menos frequente)

counter = collections.Counter(comb)
resultado = pd.DataFrame(counter.items(), columns=['Combinacao','Frequencia'])
resultado['Percentual Frequencia'] = resultado['Frequencia']/resultado['Frequencia'].sum()
resultado = resultado.sort_values(by='Percentual Frequencia')



print(
f'''

O número mais frequente é o: {freq_nr[0][0]}
O número menos frequente é o: {freq_nr[-1][0]}
A combinacao de Pares, Impares e Primos mais frequente é: {resultado['Combinacao'].values[-1]} com a frequencia de {np.around(resultado['Percentual Frequencia'].values[-1] * 100, 2)} %


'''
)