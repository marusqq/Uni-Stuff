import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(path):
    '''reads data in path, converts it to DF. Indexes on DATE'''
    df = pd.read_csv(path, delimiter=',', index_col = 'Date', parse_dates = True)
    #df['Date'] = pd.to_datetime(df['Date'])
    #df = df.set_index('Date')
    return df

data = read_csv_file('TSLA.csv')
#perskaitom faila

close = data['Close']
# cia destytojas naudojo b, as panaudojau close

date = list(data.index.values)
#pasimu musu pagrindines datos(kur uzsipildem per read_data) indexus (kas yra datos (2019...))

profit = pd.Series(np.zeros(200))
#tuscias masyvas profito kur toliau pildysim ji

period1 = 9
period2 = 26
#tai cia tie grafiko issilenkimo koeficientai

c = close.rolling(window=period1).mean()
d = close.rolling(window=period2).mean()
#pasidarom cia tas dvi linijas kur ten rodo trenda

#sunki vieta.
#temp gali but arba True arba False
temp1 = c > d

#sk pagal tai nusistato
sk = temp1 != temp1.shift(1)

poz = 0
#kol neperkam ir neparduodam tada 0
for i in range(np.max([period1, period2]), len(close)):
    profit[i] = (close[i] - close[i-1]) * poz
    if c[i] >= d[i] and c[i-1] < d[i-1]:
        print('{0}, {1} pirkimas'.format(i,close[i]))
        poz = 1

    if c[i] < d[i] and c[i-1] >= d[i-1]:
        print('{0}, {1} pardavimas'.format(i,close[i]))
        poz = -1

#cia pagrindine data (close), c (pirma trend funkcija), d (antra trend funkcija)
plt.subplot(211)
plt.plot(close, color = '#0000ff')
plt.plot(c, color = '#fc9803')
plt.plot(d, color = '#ff0000')
plt.plot(close[sk], 'k*')

#o cia tiesiog kiek uzsidirbome
plt.subplot(212)
plt.plot(date, profit.cumsum())
#print(profit)

plt.show()
