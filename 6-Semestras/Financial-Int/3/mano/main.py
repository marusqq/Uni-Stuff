import strategy as st

file = 'TSLA_Daily.csv'
df = st.read_stock(file)

max_sharpe = -9999999
for i in range(1, 100):
    test = st.start(df, loss_secure = True, days = i, optimisation=True)
    sharpe = st.sharpe(test['Money_Change'])
    if sharpe > max_sharpe:
        max_sharpe = sharpe
        best_sharpe_rating = i

#with loss_secure
a = st.start(df, loss_secure = True, days = best_sharpe_rating)

#without loss_secure
b = st.start(df, loss_secure = False, days = best_sharpe_rating)

#profits
profits_without_opti = st.start(df, loss_secure = True, optimisation = True)

#graphs with:
# TSLA close + buy + sell + (stop loss)
# MACD
# Cash
st.plot_TSLA('TSLA with and without Stop Loss', df, a, b)

#graphs both profits
st.plot_compare_profit(
    suptitle_name = 'Comparing profits', 
    df_profits = [a[3], b[3], profits_without_opti],
    names = ['With Stop Loss (+opti)', 
    'Without Stop Loss (+opti)', 
    'With Stop Loss (-opti)'])


#finish with this to show
st.show_plot()




