import numpy as np
import matplotlib.pyplot as plt

a_data = np.random.randn(200)
a_data = a_data - np.mean(a_data)+0.1

b_data = np.random.randn(200)
b_data = b_data - np.mean(b_data)+0.1

c_data = np.random.randn(200)
c_data = c_data - np.mean(c_data)+0.1

d_data = np.random.randn(200)
d_data = d_data - np.mean(d_data)+0.1

sharpe_a = np.average(a_data) / np.std(a_data) * np.sqrt(252)
sharpe_b = np.average(b_data) / np.std(b_data) * np.sqrt(252)
sharpe_c = np.average(c_data) / np.std(c_data) * np.sqrt(252)
sharpe_d = np.average(d_data) / np.std(d_data) * np.sqrt(252)


bendras_data = (a_data + b_data + c_data + d_data) / 4
sharpe_all_data= np.average(bendras_data) / np.std(bendras_data) * np.sqrt(252)

print(sharpe_all_data)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(a_data.cumsum(), color = 'green')
ax[0, 0].set(title = 'Sharpe = ' + str(round(sharpe_a, 3)))
ax[0, 0].set(xlabel = 'Days', ylabel = 'Price')


ax[0, 1].plot(b_data.cumsum(), color = 'grey')
ax[0, 1].set(title = 'Sharpe = ' + str(round(sharpe_b, 3)))
ax[0, 1].set(xlabel = 'Days', ylabel = 'Price')

ax[1, 0].plot(c_data.cumsum(), color = 'yellow')
ax[1, 0].set(title = 'Sharpe = ' + str(round(sharpe_c, 3)))
ax[1, 0].set(xlabel = 'Days', ylabel = 'Price')

ax[1, 1].plot(d_data.cumsum(), color = 'purple')
ax[1, 1].set(title = 'Sharpe = ' + str(round(sharpe_d, 3)))
ax[1, 1].set(xlabel = 'Days', ylabel = 'Price')


plt.figure(2)
plt.plot(bendras_data.cumsum(), color = 'black')
plt.title('Sharpe = ' + str(round(sharpe_all_data, 3)))
plt.xlabel('Days')
plt.ylabel('Price')

plt.show()