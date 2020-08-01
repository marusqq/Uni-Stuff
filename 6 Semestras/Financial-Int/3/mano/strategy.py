import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def sharpe(returns, P = 252):
    return np.sqrt(P) * returns.mean() / returns.std()

def macd(df, days = 13):
    '''calculates macd by taking close as argument'''
    
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    macd = pd.Series(exp1-exp2, name = 'MACD')
    ma = pd.Series(macd.rolling(days).mean(), name = 'MACD_Signal')
    macd_bar = pd.Series(macd - ma, name = 'MACD_bar')

    df = df.join(macd)
    df = df.join(ma)
    df = df.join(macd_bar)

    return df 

def trade(df, loss_secure = False):
    '''tries to trade stocks
        buys --> when signal line goes under macd
        sells --> when macd goes under signal line'''

    sell = False
    profit_calculation = 0
    tax = 0.03
    if loss_secure:
        stop_loss_rate = 0.1
    close_holding = None


    df['Close_yesterday'] = df['Close'].shift(1)
    df['MACD_yesterday'] = df['MACD'].shift(1)
    df['MACD_Signal_yesterday'] = df['MACD_Signal'].shift(1)

    buying = {
        "Date":[],
        "Buy_Price":[]
    }

    selling = {
        "Date":[],
        "Sell_Price":[]
    }

    profit = {
        "Date":[],
        "Money_Change":[]
    }

    if loss_secure:
        stop_loss = {
            "Date":[],
            "Loss_Sold_Price":[]
        }
        

    for date, data in df.iterrows():
        
        taxed = False

        profit['Date'].append(date)
        profit['Money_Change'].append(
            (data['Close'] - data['Close_yesterday']) * profit_calculation
        )

        #if i am buying
        if not sell:
            
            #when MACD >= MACD_Signal TODAY and was MACD < MACD_Signal YESTERDAY
            if data['MACD'] >= data['MACD_Signal'] and data['MACD_yesterday'] < data['MACD_Signal_yesterday']: 
                buying['Date'].append(date)
                buying['Buy_Price'].append(data['Close'])
                if loss_secure:
                    close_holding = data['Close']

                sell = True
                taxed = True

                profit_calculation = 1
                
        
        #if i am selling
        else:
            
            #when MACD < MACD_Signal TODAY and was MACD >= MACD_Signal YESTERDAY                                    
            if (data['MACD'] < data['MACD_Signal'] and data['MACD_yesterday'] >= data['MACD_Signal_yesterday']):
                selling['Date'].append(date)
                selling['Sell_Price'].append(data['Close'])
                
                sell = False
                taxed = True
                profit_calculation = -1
            
            #if loss_secure is enabled
            elif loss_secure:
                
                if (close_holding * (1 - stop_loss_rate) >= data['Close']):
                    stop_loss['Date'].append(date)
                    stop_loss['Loss_Sold_Price'].append(data['Close'])

                    sell = False
                    taxed = True
                    profit_calculation = -1

         # if we did a transaction
        if taxed:
            if profit['Money_Change'][-1] > 0:
                profit['Money_Change'][-1] = profit['Money_Change'][-1] * (1 - tax)

            elif profit['Money_Change'][-1] < 0:
                profit['Money_Change'][-1] = profit['Money_Change'][-1] * (1 + tax)


    df_buy = pd.DataFrame(buying)
    df_sell = pd.DataFrame(selling)
    df_profit = pd.DataFrame(profit)
    if loss_secure:
        df_stop_loss = pd.DataFrame(stop_loss)
    
    if loss_secure:
        return df, df_buy, df_sell, df_profit, df_stop_loss
    else:
        return df, df_buy, df_sell, df_profit

def read_stock(file_name):
    '''reads the stock and returns it in a DataFrame'''

    df = pd.read_csv(file_name, parse_dates=['Date'], index_col='Date')
    return df

def start(df, loss_secure = False, days = None, optimisation = False):
    '''calculates macd, then starts trading with or without loss secure
    returns 4 dataframes in list if loss_secure is False (df, df_buy, df_sell, df_profit),
    returns 5 dataframs in list if loss_secure is True (df, df_buy, df_sell, df_profit, df_stop_loss)'''

    #calculate MACD
    if days is None:
        df = macd(df)
    else:
        df = macd(df, days)

    #start trading
    if loss_secure:
        df, df_buy, df_sell, df_profit, df_stop_loss = trade(df, True)
        #if we are only optimising, df_profit is enough
        if optimisation:
            return df_profit
        return df, df_buy, df_sell, df_profit, df_stop_loss
    else:
        df, df_buy, df_sell, df_profit = trade(df, False)
        return df, df_buy, df_sell, df_profit

def plot_TSLA(suptitle_name, df, with_stop_loss, without_stop_loss):
    #two subplots
    fig, ax = plt.subplots(3, sharex = True)
    fig.set_size_inches(16, 5)
    fig.suptitle(suptitle_name)

    #list:
    # list[0] = df,             list[1] = df_buy,           list[2] = df_sell, 
    # list[3] = df_profit,      list[4] = df_stop_loss

    #1GRAPHIC
    #stock close
    ax[0].plot(df.Close, color = 'black')
    #buys and sells
    ax[0].plot(with_stop_loss[1]['Date'], with_stop_loss[1]['Buy_Price'], 'bx')
    ax[0].plot(with_stop_loss[2]['Date'], with_stop_loss[2]['Sell_Price'], 'rx')
    #stop loss
    ax[0].plot(with_stop_loss[4]['Date'], with_stop_loss[4]['Loss_Sold_Price'], 'yx')
    ax[0].legend(['TSLA Close', 'Buy', 'Sell', 'Trade Loss Sell'], loc = 'lower left')

    #2GRAPHIC
    #stock close
    ax[1].plot(df.Close, color = 'black')
    #buys and sells
    ax[1].plot(without_stop_loss[1]['Date'], without_stop_loss[1]['Buy_Price'], 'bx')
    ax[1].plot(without_stop_loss[2]['Date'], without_stop_loss[2]['Sell_Price'], 'rx')
    ax[1].legend(['TSLA Close', 'Buy', 'Sell'], loc = 'lower left')

    #3GRAPHIC
    #macd:
    ax[2].bar(with_stop_loss[0].index, with_stop_loss[0]['MACD_bar'], color = 'black')
    ax[2].plot(with_stop_loss[0]['MACD'], color = 'yellow')
    ax[2].plot(with_stop_loss[0]['MACD_Signal'], color = 'cyan')
    ax[2].legend(['MACD', 'MACD_Signal', 'MACD bars'], loc = 'lower left')
     
    # #profit:
    # ax[3].plot(df_profit['Date'], df_profit['Money_Change'].cumsum(), color = 'blue')
    
    # if df_stop_loss is not None:
    #     ax[2].legend(["Cash with 10% stop loss"])
    # else:
    #     ax[2].legend(['Cash'])
    # ax[3].legend(['SL:Profit without opti'], loc = 'lower left')

def plot_compare_profit(suptitle_name, df_profits, names):
    '''compares two profits and plots them'''
    fig, ax = plt.subplots(1)
    fig.set_size_inches(16, 5)
    fig.suptitle(suptitle_name)
    ax.plot(df_profits[0]['Date'], df_profits[0]['Money_Change'].cumsum(), color = 'red')
    ax.plot(df_profits[1]['Date'], df_profits[1]['Money_Change'].cumsum(), color = 'blue')
    ax.plot(df_profits[2]['Date'], df_profits[2]['Money_Change'].cumsum(), color = 'black')
    ax.legend(names)

def show_plot():
    plt.show()