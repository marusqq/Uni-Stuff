import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Parengiame funkcijas indikatoriui iškviesti
def PC_upper(data, N):
    Upper = np.zeros([len(data_pd.index)]) #sukuria tuscia masyva, kriame bus tiek elementu kiek yra reiksmiu
    for i in range(N-1, len(data_pd.index)-1):
        Upper[i+1] =max(data_pd['<HIGH>'][i-N+1:i+1])
    return Upper

def PC_lower(data, N):
    Lower = np.zeros([len(data_pd.index)]) #sukuria tuscia masyva, kriame bus tiek elementu kiek yra reiksmiu
    for i in range(N-1, len(data_pd.index)-1):
            Lower[i+1] = min(data_pd['<LOW>'][i-N+1:i+1])
    return Lower

#Nuskaitome duomenis
#data_pd = pd.read_csv('Strategija.csv', delimiter='\t')
data_pd = pd.read_csv('EURUSD.csv', delimiter='\t')

format = '%Y-%m-%d'
data_pd['<DATE>'] = pd.to_datetime(data_pd['<DATE>'], format=format)
data_pd = data_pd.set_index(data_pd['<DATE>']) #datą nustatome indeksu
data_pd = data_pd.drop(columns=['<DATE>'])

#Strategija
N=22

PC_UPPER = PC_upper(data_pd['<HIGH>'].values, N) #Išsikviečiame indikatoriaus funkcijas
PC_LOWER = PC_lower(data_pd['<LOW>'].values, N)

HIGH = (data_pd['<HIGH>'].values)
LOW = (data_pd['<LOW>'].values)
CLOSE = (data_pd['<CLOSE>'].values)

fig, ax = plt.subplots(2, 1, sharex=True, sharey=False)
plt.gcf().autofmt_xdate()
ax[0].set_title('Strategija')
ax[0].plot(data_pd['<CLOSE>'],  color = 'g')
ax[0].plot(data_pd.index[N:],PC_UPPER[N:], color = 'b')
ax[0].plot(data_pd.index[N:],PC_LOWER[N:], color = 'b')

data_pd['Pozicija ateityje'] = None #sukurias tuscia stulpeli data frame

#Pirkimai
for i in range(0, len(CLOSE) - 1):
    if (CLOSE[i+1] >= PC_UPPER[i+1]) and (PC_UPPER[i] > CLOSE[i]): #Kai vakar kaina mazesne uz indikatoriu ir siandien kaina didesne uz indikatoriu tai esame longe
        data_pd['Pozicija ateityje'].iloc[i+1] = 1 #uzpildo 1

#Pardavimai
for i in range(0, len(CLOSE) - 1):
     if (CLOSE[i + 1] <= PC_LOWER[i + 1]) and (PC_LOWER[i] < CLOSE[i]):
            data_pd['Pozicija ateityje'].iloc[i+1] = -1 #uzpildo -1

data_pd['Pozicija ateityje'].fillna(method='ffill',inplace=True) #uzpildo trukstamas reiksmes dubliuodamas


data_pd['Pokytis'] =  data_pd['Pozicija ateityje'].diff(1) #skaiciuoja skirtumus

idx = np.zeros([len(CLOSE)], dtype = bool) #sukuria vektoriu is False
for i in range(0, len(CLOSE)):
    if data_pd['Pokytis'][i] == 2:
        idx[i] = True
data_pd['Long'] =  idx

index = np.zeros([len(CLOSE)], dtype = bool)
for i in range(0, len(CLOSE)):
    if data_pd['Pokytis'][i] == -2:
        index[i] = True
data_pd['Short'] =  index


ax[0].scatter(data_pd.index[idx], CLOSE[idx], marker = 'x', color = 'red')
ax[0].scatter(data_pd.index[index],CLOSE[index], marker = '*', color = 'black')
ax[0].legend(['Close kaina','PC Upper','PC Lower','Pardavimai', 'Pirkimai'], loc=3) #uzdedam legenda

#Pelnas

data_pd['Pozicijos pasikeitimas'] = np.zeros([len(CLOSE)], dtype = bool)
for i in range (0, len(CLOSE)):
    if data_pd['Long'][i] != data_pd['Short'][i]:
        data_pd['Pozicijos pasikeitimas'][i]= True

data_pd['Pozicija'] = data_pd['Pozicija ateityje'].shift(1) #poziciju masyva paslenkame per viena diena zemyn ir priskiriam naujam stulpeliui, kad sekancia diena busime shorte, o ne siandien, pirma pozicija nezinoma
data_pd.iloc[0, data_pd.columns.get_loc('Pozicija')] = None

mokesciai = -0.05
data_pd['Mokesciai'] = data_pd['Pozicijos pasikeitimas'] * mokesciai #*2

data_pd['Kainos pokytis'] = data_pd['<CLOSE>'].diff(1) #dienos pokytis diff skaiciuoja skirtuma  ir idedame i df
data_pd.iloc[0, data_pd.columns.get_loc('Kainos pokytis')] = 0

data_pd['Pelnas is pozicijos'] = data_pd['Pozicija'] * data_pd['Kainos pokytis']
data_pd['Bendras pelnas'] = data_pd['Mokesciai'] + data_pd['Pelnas is pozicijos']

cs = np.cumsum(data_pd['Bendras pelnas'])
ax[1].set_title('Bendras pelnas')
ax[1].plot(cs)

# strategija kuri atidaro tik long pozicijas
#data_pd['Pozicija long'] = data_pd['Pozicija']
#data_pd.loc[data_pd['Pozicija'] < 0, ['Pozicija long']] = 0

#data_pd['Bendras pelnas long'] = data_pd['Pozicijos pasikeitimas'] * mokesciai * 1 + data_pd['Pozicija long'] * data_pd['Kainos pokytis'] #skaiciuojam dieninius pelna

#cs = np.cumsum(data_pd['Bendras pelnas long']) #suskaiciuoja visu dienu bendra pelna
#ax[1].plot(cs) #nupaisome

ax[1].legend(['Pelnas'])

#Take profit

data_pd['Long kaina'] = None
for i in range(0, len(CLOSE)):
    if data_pd['Long'][i] == True:
        data_pd['Long kaina'][i] = data_pd['<CLOSE>'][i]
data_pd['Long kaina'].fillna(method='ffill',inplace=True)
Long_kaina=data_pd['Long kaina'].values

data_pd['Short kaina'] = None
for i in range(0, len(CLOSE)):
    if data_pd['Short'][i] == True:
        data_pd['Short kaina'][i] = data_pd['<CLOSE>'][i]
data_pd['Short kaina'].fillna(method='ffill',inplace=True)
Short_kaina=data_pd['Short kaina'].values


data_pd['TP_pozicija'] = None

for i in range(0, len(CLOSE)):
    if CLOSE[i] >= 1.01 * data_pd['Long kaina'][i]:
        data_pd['TP_pozicija'][i] = 1 #parduodame

for i in range(0, len(CLOSE)):
    if CLOSE[i] <= 0.99 * data_pd['Long kaina'][i]:
        data_pd['TP_pozicija'][i] = - 1 #perkame

data_pd['TP_pozicija'].fillna(method='ffill',inplace=True) #uzpildo trukstamas reiksmes dubliuodamas
data_pd['TP_pokytis'] =  data_pd['TP_pozicija'].diff(1)

TP_pirkimas = np.zeros([len(CLOSE)], dtype = bool) #sukuria vektoriu is False
for i in range(0, len(CLOSE)):
    if data_pd['TP_pokytis'][i] == 2:
        TP_pirkimas[i] = True
data_pd['TP_pirkimas'] =  TP_pirkimas

TP_pardavimas = np.zeros([len(CLOSE)], dtype = bool)
for i in range(0, len(CLOSE)):
    if data_pd['TP_pokytis'][i] == -2:
        TP_pardavimas[i] = True
data_pd['TP_pardavimas'] = TP_pardavimas

plt.figure()
plt.gcf().autofmt_xdate()
plt.title('Take profit')
plt.plot(data_pd['<CLOSE>'],  color = 'g')
plt.plot(data_pd.index[N:],PC_UPPER[N:], color = 'b')
plt.plot(data_pd.index[N:],PC_LOWER[N:], color = 'b')
plt.scatter(data_pd.index[TP_pirkimas], CLOSE[TP_pirkimas], marker = '*', color = 'red')
plt.scatter(data_pd.index[TP_pardavimas], CLOSE[TP_pardavimas], marker = '^', color = 'black')
plt.plot(data_pd['Long kaina'], color = 'yellow')
#plt.plot(data_pd['Short kaina'], color = 'black')

plt.legend(['Close kaina','PC Upper','PC Lower','TP','Pirkimai', 'Pardavimai'], loc=1) #uzdedam legenda


#Optimizacija
def strategija_PC(df, N, mokesciai):

    PC_UPPER = PC_upper(data_pd['<HIGH>'].values, N)
    PC_LOWER = PC_lower(data_pd['<LOW>'].values, N)

    df['Pozicija ateityje'] = None  # sukurias tuscia stulpeli data frame

    for i in range(0, len(CLOSE) - 1):
        if (CLOSE[i + 1] >= PC_UPPER[i + 1]) and (PC_UPPER[i] > CLOSE[i]):  # Kai vakar kaina mazesne uz indikatoriu ir siandien kaina didesne uz indikatoriu tai esame longe
            df['Pozicija ateityje'].iloc[i + 1] = 1  # uzpildo 1, kai esame longe


    for i in range(0, len(CLOSE) - 1):
        if (CLOSE[i + 1] <= PC_LOWER[i + 1]) and (PC_LOWER[i] < CLOSE[i]):
            df['Pozicija ateityje'].iloc[i + 1] = -1  # uzpildo -1, kai esame shorte

    df['Pozicija ateityje'].fillna(method='ffill', inplace=True)  # uzpildo trukstamas reiksmes dubliuodamas

    df['Pokytis'] = df['Pozicija ateityje'].diff(1)

    df['Pozicijos pasikeitimas'] = np.zeros([len(CLOSE)], dtype=bool)
    for i in range(0, len(CLOSE)):
        if df['Long'][i] != df['Short'][i]:
            df['Pozicijos pasikeitimas'][i] = True

    df['Pozicija'] = df['Pozicija ateityje'].shift(1)
    df.iloc[0, df.columns.get_loc('Pozicija')] = None

    df['Mokesciai'] = df['Pozicijos pasikeitimas'] * mokesciai

    df['Kainos pokytis'] = df['<CLOSE>'].diff(1)
    df.iloc[0, df.columns.get_loc('Kainos pokytis')] = 0

    df['Pelnas is pozicijos'] = df['Pozicija'] * df['Kainos pokytis']
    df['Bendras pelnas'] = df['Mokesciai'] + df['Pelnas is pozicijos']

    return df['Bendras pelnas']


N=22
mokesciai = -0.05
df = data_pd[['<CLOSE>']].copy()
df['Long'] = data_pd[['Long']].copy()
df['Short'] = data_pd[['Short']].copy()
rez = strategija_PC(df, N, mokesciai)

def annualised_sharpe(returns, P=252):

    #Finansų srityje „Sharpe“ koeficientas išmatuoja investicijos rezultatą, palyginti su turtu, nerizikingu turtu,
    # po to, kai jis yra pritaikytas atsižvelgiant į jo riziką.
    # Jis apibrėžiamas kaip skirtumas tarp investicijos grąžos ir nerizikingos grąžos, padalytos iš standartinio investicijos nuokrypio.
    # Padeda investuotojams suprasti investicijos grąžą, palyginti su rizika.
    # Šis koeficientas yra vidutinė uždirbta grąža, išreikšta nerizikingos gražos norma per vienetą arba bendros rizikos norma.

    return np.sqrt(P) * returns.mean() / returns.std()

df_opt = pd.DataFrame(columns=['N', 'sharpe_ratio', 'rez']) #sukuriame lentelę iš 3 stulpelių ir priskiriame pavadinimus

for N in range(1,100,4):
    rez = strategija_PC(df, N, mokesciai) #sukame ciklą (išsikviečiame savo strategijos funkciją ir gauname jos reikės, kai kinta N)
    sharpe_ratio = annualised_sharpe(rez) #paskaičiuojame sharpą su visomis rez reikšmėmis
    df_opt = df_opt.append({'N': N, 'sharpe_ratio': sharpe_ratio, 'rez': rez.copy()}, ignore_index = True) # BUTINAI rez.copy() !!!!!! prijungiame prie lentelės
    idx_max = df_opt['sharpe_ratio'].idxmax() #randame maksimalią sharpe reikšmę
    print('Didziausias sarpo santykis ({}) yra su parametru N: {}.'.format(df_opt.loc[idx_max]['sharpe_ratio'],
                                                                                 df_opt.loc[idx_max]['N'],))

plt.figure()
plt.title('Pelno kitimo grafikas')
plt.plot(df_opt.loc[idx_max]['rez'].cumsum(), label='Optimizuotas pelnas')
plt.plot(df_opt.loc[22]['rez'].cumsum(), label='Pelnas')

plt.legend(['Optimizuotas pelnas', 'Pelnas'])

plt.show()
