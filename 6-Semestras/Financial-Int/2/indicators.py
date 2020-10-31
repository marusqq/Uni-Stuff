import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def read_csv_file(path):
    '''reads data in path, converts it to DF. Indexes on DATE'''
    df = pd.read_csv(path, delimiter=',', index_col = 'Date', parse_dates = True)
    #df['Date'] = pd.to_datetime(df['Date'])
    #df = df.set_index('Date')
    return df

def wr(high, low, close, lbp=14):
    '''calculate williams % range by taking arguments:
        high, low, close, lbp (14 by default)'''

    hh = high.rolling(lbp, min_periods=0).max()  # highest high over lookback period lbp
    ll = low.rolling(lbp, min_periods=0).min()  # lowest low over lookback period lbp

    wr = -100 * (hh - close) / (hh - ll)
    return pd.Series(wr)

def macd(close):
    '''calculates macd by taking close as argument'''
    
    exp1 = close.ewm(span=12, adjust=False).mean()
    exp2 = close.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    ma = pd.Series(macd.rolling(13).mean(), name = 'MA')

    return pd.Series(macd), ma
 
#Ease of Movement  
def eom(high, low, vol, n):
    '''calculates eom using high, low, vol and n'''

    EoM = (high.diff(1) + low.diff(1)) * (high - low) / (2 * vol)  
    EoM = pd.Series(EoM.rolling(n).mean())  

    return EoM

#read our data
df = read_csv_file("TSLA.csv")

#----------------------W%R
#calculate w%r
wr = wr(df['High'], df['Low'], df['Close'])

#----------------------MACD
#calculate macd
macd, macdMA = macd(df['Close'])

#----------------------Ease of Movement
#calculate ease of movement
eom = eom(df['High'], df['Low'], df['Vol'], 14)


#------------------------ Showing plot
fig, ax = plt.subplots(4, sharex=True)
fig.set_size_inches(14, 6)
fig.suptitle('TSLA and W%R, MACD, EOM indicators')

ax[0].set(ylabel='TSLA [CLOSE]')
ax[1].set(ylabel='TSLA [W%R]')
ax[2].set(ylabel='TSLA [MACD]')
ax[3].set(xlabel='Date', ylabel='TSLA [EOM]')

ax[0].plot(df.Close, color = 'green', label = 'TSLA - Close')
ax[1].plot(wr, color = 'grey', label = 'TSLA - W%R')

ax[2].bar(df.index, macd - macdMA)
ax[2].plot(macd, color = 'yellow', label = 'TSLA - MACD')
ax[2].plot(macdMA, color = 'cyan', label = 'TSLA - MACDAvg')

ax[3].plot(eom, color = 'purple', label = 'TSLA - Ease of Movement')

plt.show()