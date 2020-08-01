import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_stock(path):
  data = pd.read_csv(path, index_col = 'Local time')
  return data

def keltner_channel(df, n = 20):

    #Upper
    KelchU = ((4 * df['High'] - 2 * df['Low'] + df['Close']) / 3)
    KelchU = pd.Series(KelchU.rolling(n).mean(), name = 'KelchUpper')

    #Middle
    KelchM = ((df['High'] + df['Low'] + df['Close']) / 3)
    KelchM = pd.Series(KelchM.rolling(n).mean(), name = 'KelchMiddle')

    #Lower
    KelchL = ((-2 * df['High'] + 4 * df['Low'] + df['Close']) / 3)
    KelchL = pd.Series(KelchL.rolling(n).mean(), name = 'KelchLower')

    df = df.join(KelchU)  
    df = df.join(KelchM)  
    df = df.join(KelchL)

    return df

#Read the Stock
df = read_stock('NFLX_Daily.csv')

#Calculate Keltner
df = keltner_channel(df)

#set size of plot
plt.figure(figsize=(20,5))

#plot NFLX
df['Close'].plot(color = 'black', title = 'Kelch Channel')

#plot Kelch
df['KelchUpper'].plot(color = 'cyan')
df['KelchMiddle'].plot(color = 'grey')
df['KelchLower'].plot(color = 'red')

print(len(df['Close']))
plt.show()



