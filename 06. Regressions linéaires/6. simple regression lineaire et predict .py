import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import linear_model

# On a nos valeurs datetimes en abscisse X
data_time = np.asarray(['2012-04-12 14:56:50','2012-04-12 14:56:50','2012-04-12 15:27:01','2012-04-12 15:42:06'])

# On a nos valeurs en kw/h en ordonnées y.
data_count = np.asarray([1.256400,1.430750,1.369910,1.359350]) 

df = pd.DataFrame({'time': data_time, 'count': data_count})
df.time = pd.to_datetime(df.time)

regr = linear_model.LinearRegression()

regr.fit(df.time.values.reshape(-1, 1), df['count'].values.reshape(-1, 1)) 

# Make predictions using the testing set
y_pred = regr.predict(df.time.values.astype(float).reshape(-1, 1))
df['pred'] = y_pred

ax = df.plot(x='time', y='count', color='black', style='.')
df.plot(x='time', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)
ax.set_title('My Title')
ax.set_xlabel('Date')
ax.set_ylabel('Metric')

plt.show()

# put the dates of which you want to predict kwh here (NOT WORKING)

""" X_new = np.array(['2012-04-13 05:55:30']).reshape(-1, 1)
print(regr.predict(X_new)) """

# Et si on essaye vaec seulement des dates, cela fonctionne aussi ;: 

data_time = np.asarray(['2017-05-24', '2017-05-25', '2017-05-26',
                        '2017-05-27', '2017-05-28', '2017-05-29',
                        '2017-05-30', '2017-05-31', '2017-06-01',
                        '2017-06-02', '2017-06-03', '2017-06-04',
                        '2017-06-05', '2017-06-06', '2017-06-07',
                        '2017-06-08', '2017-06-09', '2017-06-10',
                        '2017-06-11', '2017-06-12', '2017-06-13',
                        '2017-06-14', '2017-06-15', '2017-06-16',
                        '2017-06-17', '2017-06-18', '2017-06-19',
                        '2017-06-20', '2017-06-21'])
data_count = np.asarray([300.000, 301.000, 302.000, 303.000, 304.000,
                         305.000, 306.000, 307.000, 308.000, 309.000,
                         310.000, 311.000, 312.000, 230.367, 269.032,
                         258.867, 221.645, 222.323, 212.357, 198.516,
                         230.133, 243.903, 244.320, 207.451, 192.710,
                         212.033, 216.677, 222.333, 208.710])

df = pd.DataFrame({'time': data_time, 'count': data_count})
df.time = pd.to_datetime(df.time)

regr = linear_model.LinearRegression()
regr.fit(df.time.values.reshape(-1, 1), df['count'].values.reshape(-1, 1)) 

# Make predictions using the testing set
y_pred = regr.predict(df.time.values.astype(float).reshape(-1, 1))
df['pred'] = y_pred

ax = df.plot(x='time', y='count', color='black', style='.')
df.plot(x='time', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)
ax.set_title('My Title')
ax.set_xlabel('Date')
ax.set_ylabel('Metric')

plt.show()