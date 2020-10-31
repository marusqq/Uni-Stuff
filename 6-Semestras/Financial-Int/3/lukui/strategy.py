import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def optimisation(data, max_sharpe):
  
  for index in range(1,100):
      calculated_data = normal_trading(data, optimised_days = index, take_profit = False)
      calculated_sharpe = sharpe(calculated_data[3]['Profit'])
      print('checking index:', index, 'sharpe:', calculated_sharpe)

      #print('calculate_sharpe = ' + str(calculated_sharpe) + ' - [index]' + str(index) + ' vs ' + 'max_sharpe = ' + str(max_sharpe) + ' - [index]' + str(index))
      if calculated_sharpe > max_sharpe:
          max_sharpe = calculated_sharpe
          best_sharpe_rating = index

  return best_sharpe_rating

def read_stock(path):
  '''csv file reader'''
  data = pd.read_csv(path, parse_dates = ['Date'])
  data = data.set_index('Date')

  return data

def taxation(money, tax_rate):
  if money > 0:
    return money * (1 - tax_rate)

  elif money < 0:
    return money * (1 + tax_rate)
  
  else:
    return money

def sharpe(returns, P = 252):
    return np.sqrt(P) * returns.mean() / returns.std()

def williams_range(data, lbp):
  '''calculate williams % range by taking arguments:
      high, low, close, lbp (14 by default)'''

  hh = data['High'].rolling(lbp, min_periods=0).max()  # highest high over lookback period lbp
  ll = data['Low'].rolling(lbp, min_periods=0).min()  # lowest low over lookback period lbp

  wr = -100 * (hh - data['Close']) / (hh - ll)

  wr_pd = pd.Series(wr, name = 'WR')
  data = data.join(wr_pd)
  
  return data

def plot_1(data, buy, sell, profits):

  #create fig
  fig, ax = plt.subplots(3, sharex=True, sharey=False)
  fig.suptitle('Defaults')
  #set size of plot
  fig.set_size_inches(20, 5)

  #labels
  ax[0].set(ylabel= 'Price EUR')
  ax[1].set(ylabel= '%')
  ax[2].set(ylabel= 'Price EUR')
  
  #grids
  ax[0].grid()
  ax[1].grid()
  ax[2].grid()


  #Close
  close, = ax[0].plot(data['Close'], color = 'black', label = 'NFLX Close')
  #plot what when we bought
  buy, = ax[0].plot(buy['Date'], buy['Price'], 'bx', label = 'Buy Symbols')
  #plot what when we sold
  sell, = ax[0].plot(sell['Date'], sell['Price'], 'rx', label = 'Sell Symbols')

  #WR
  wr, = ax[1].plot(data['WR'], color = 'green', label = 'Williams % Range')

  line20 = ax[1].axhline(y = -20, color = 'yellow', linestyle = '--', label = '-20%') 
  line80 = ax[1].axhline(y = -80, color = 'red', linestyle = '--', label = '-80%')

  #plot profits
  profits, = ax[2].plot(profits['Date'], profits['Profit'].cumsum(), color = 'black', label = 'Profits')

  #legends
  first_legend = ax[0].legend(handles=[close, buy, sell], loc='lower left')
  second_legend = ax[1].legend(handles=[wr, line20, line80], loc='lower left')
  third_legend = ax[2].legend(handles=[profits], loc='lower left')

  return 

def plot_2(data, buy, sell, profits, take_profit):

  #create fig
  fig, ax = plt.subplots(3, sharex=True, sharey=False)
  fig.suptitle('Optimised with take_profit')

  #set size of plot
  fig.set_size_inches(20, 5)


  #labels
  ax[0].set(ylabel= 'Price EUR')
  ax[1].set(ylabel= '%')
  ax[2].set(ylabel= 'Price EUR')
  
  #grids
  for x in ax:
      x.grid()
  

  #Close
  close, = ax[0].plot(data['Close'], color = 'black', label = 'NFLX Close')
  #plot what when we bought
  buy, = ax[0].plot(buy['Date'], buy['Price'], 'bx', label = 'Buy Symbols')
  #plot what when we sold
  sell, = ax[0].plot(sell['Date'], sell['Price'], 'rx', label = 'Sell Symbols')
  #take profit sells
  take_profit, = ax[0].plot(take_profit['Date'], take_profit['Price'], 'gx', label = 'Take Profit Symbols')

  #WR
  wr, = ax[1].plot(data['WR'], color = 'green', label = 'Williams % Range')

  line20 = ax[1].axhline(y = -20, color = 'yellow', linestyle = '--', label = '-20%') 
  line80 = ax[1].axhline(y = -80, color = 'red', linestyle = '--', label = '-80%')

  #plot profits
  profits, = ax[2].plot(profits['Date'], profits['Profit'].cumsum(), color = 'black', label = 'Profits')

  #legends
  first_legend = ax[0].legend(handles=[close, buy, sell, take_profit], loc='lower left')
  second_legend = ax[1].legend(handles=[wr, line20, line80], loc='lower left')
  third_legend = ax[2].legend(handles=[profits], loc='lower left')

  return 

def plot_3(defaults, optimised_defaults, default_take_profit, optimised_take_profit):

    #create fig
    fig, ax = plt.subplots(1, sharex=True, sharey=False)

    #set size of plot
    fig.set_size_inches(20, 5)

    fig.suptitle('Profit compare')

    #labels
    ax.set(ylabel= 'Profits in EUR')

    #plot profits
    profits1, = ax.plot(defaults['Date'], defaults['Profit'].cumsum(), color = 'black', label = 'Profits default')
    
    #plot profits
    profits2, = ax.plot(optimised_defaults['Date'], optimised_defaults['Profit'].cumsum(), color = 'yellow', label = 'Profits optimised without take profit')

    #plot profits
    profits3, = ax.plot(default_take_profit['Date'], default_take_profit['Profit'].cumsum(), color = 'red', label = 'Profits default with take profit')
    
    #plot profits
    profits4, = ax.plot(optimised_take_profit['Date'], optimised_take_profit['Profit'].cumsum(), color = 'blue', label = 'Profits optimised with take profit')
    
    #legends
    legend = ax.legend(handles=[profits1, profits2, profits3, profits4], loc='lower left')

    return

def normal_trading(data, optimised_days, take_profit = True):

  #Calculate WR
  data = williams_range(data, optimised_days)

  #start trading
  buying_trades = pd.DataFrame(columns=['Date', 'Price'])
  selling_trades = pd.DataFrame(columns=['Date', 'Price'])
  take_profit_sell_trades = pd.DataFrame(columns=['Date', 'Price'])
  profits = pd.DataFrame(columns=['Date', 'Profit'])

  tax_rate = 0.02
  buying_mult = 0
  take_profit_ratio = 0.3
  last_bought_stock_price = 0
  days_to_hold = 1

  data['Shifted_Close'] = data.Close.shift(-1)

  #start going through
  for index, row in data.iterrows():
    
    #wait for a day
    if days_to_hold > 0:
        days_to_hold = days_to_hold - 1

    todays_profit = (row['Close'] - row['Shifted_Close']) * buying_mult

    #buying
    if buying_mult != 1:
      if row['WR'] <= -90 and days_to_hold == 0:
        
        #selling after this buy
        buying_mult = 1

        #set last bought price
        last_bought_stock_price = row['Close']

        #add what you buy
        buying_trades = buying_trades.append({
            'Date' : index, 
            'Price' : row['Close']},
            ignore_index = True)

        #after you buy add a timer so we don't sell and buy again instantly
        days_to_hold = 20
        
        #taxation
        todays_profit = taxation(todays_profit, tax_rate) 
        
    
    #selling
    elif buying_mult != -1:
      
        #we take profit instantly if we can
        if last_bought_stock_price * (1 + take_profit_ratio) <= row['Close'] and take_profit:

            buying_mult = -1

            #add what you take profit sell
            take_profit_sell_trades = take_profit_sell_trades.append({
                'Date' : index, 
                'Price' : row['Close']},
                ignore_index = True)
            
            #taxation
            todays_profit = taxation(todays_profit, tax_rate) 

        #or just sell normally
        elif row['WR'] >= -10 and days_to_hold == 0:
            
            #buying after this sell
            buying_mult = -1

            #add what you sell
            selling_trades = selling_trades.append({
                'Date' : index, 
                'Price' : row['Close']},
                ignore_index = True)
            
            #taxation
            todays_profit = taxation(todays_profit, tax_rate) 

    profits = profits.append(
        { 'Date' : index, 'Profit' : todays_profit}, 
        ignore_index = True)         

  return data, buying_trades, selling_trades, profits, take_profit_sell_trades

data = read_stock('NFLX_Daily.csv')

#buying/selling
data1, buy1, sell1, profits1, take_profit1 = \
normal_trading(data, optimised_days = 14, take_profit = False)

data4, buy4, sell4, profits4, take_profit4 = \
normal_trading(data, optimised_days = 14, take_profit = True)

best_sharpe = optimisation(data, max_sharpe = -99)
#best_sharpe = 93

data2, buy2, sell2, profits2, take_profit2 = \
normal_trading(data, optimised_days = best_sharpe, take_profit = True)

data3, buy3, sell3, profits3, take_profit3 = \
normal_trading(data, optimised_days = best_sharpe, take_profit = False)

#plot1:
  #1. default stock + buy + sell
  #2. default indicator
  #3. profit
plot_1(data1, buy1, sell1, profits1)

#plot2:
  #1. default stock + buy + sell + take profit
  #2. optimised indicator
  #3. profit
plot_2(data2, buy2, sell2, profits2, take_profit2)

#plot3:
  #1. profit from default indicator (profits1)
  #2. profit from optimised indicator (profits3)
  #3. profit from default indicator + take profit (profits4)
  #4. profit from optimised indicator + take profit (profits2)
plot_3(profits1, profits3, profits4, profits2)

plt.show()
