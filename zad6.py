import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
#
# print(df[df['Liczba'] > 1000])
#
# print(df[df['Imie'] == 'JAN'])
#
# print(df.agg({'Liczba': ['sum']}))
#
# x = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
#
# print(x.agg({'Liczba': ['sum']}))
#
# chl = df[(df['Plec'] == 'M')]
#
# dzie = df[(df['Plec'] == 'K')]
#
# print(chl.agg({'Liczba': ['sum']}))
# print(dzie.agg({'Liczba': ['sum']}))
#
# print(chl.sort_values(by='Liczba').tail(1))
# print(dzie.sort_values(by='Liczba').tail(1))
#
#
# df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.')
# print(df)
#
#
# print(df["Sprzedawca"].unique())
#
# print(df.sort_values(by='Utarg').tail())


# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()


# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
#
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True, title='Populacja z podziałem na kontynenty')
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# grupa = (df.groupby(['Imię i nazwisko']).agg({'Wartośc zamówienia':["sum"]}))
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
# plt.legend(loc='lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['Wartości'])
# print(df)
#
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot()
# plt.show()


# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel='Plec', ylabel='Mln', rot=0, legend=False, title='Ilośc urodzonych dzieci w latach 2000 - 2017')
# plt.show()

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# x = df[(df['Rok'] >= 2012) & (df['Rok'] <= 2017)]
# grupa = x.groupby(['Plec']).agg({'Liczba': ['sum']})
# print(grupa)
# grupa.plot(kind='pie',title = "% odzwierciedlenie płci dzieci urodzonych w latach 2012-2017" , subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), colors=['red', 'green'])
#
# plt.show()
