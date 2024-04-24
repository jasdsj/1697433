import pandas as pd
import numpy as np
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

print(df[df['Liczba'] > 1000])

print(df[df['Imie'] == 'JAN'])

print(df.agg({'Liczba': ['sum']}))

x = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]

print(x.agg({'Liczba': ['sum']}))

chl = df[(df['Plec'] == 'M')]

dzie = df[(df['Plec'] == 'K')]

print(chl.agg({'Liczba': ['sum']}))
print(dzie.agg({'Liczba': ['sum']}))

print(chl.sort_values(by='Liczba').tail(1))
print(dzie.sort_values(by='Liczba').tail(1))


df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.')
print(df)


print(df["Sprzedawca"].unique())

print(df.sort_values(by='Utarg').tail())

