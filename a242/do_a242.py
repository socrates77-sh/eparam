import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

plt.rc('figure', figsize=(12, 6))

raw_data = pd.read_csv('A6090722-NA-12-RT-170927-185341.csv', header=12)
cols = [x.strip() for x in raw_data.columns]

valid_data = raw_data.iloc[:, 5:]
valid_data.columns = valid_data.columns.str.strip()
basic_sta = valid_data.describe()

param = 'VREF3_H()'

valid_data[param].plot(grid=True)
plt.title('all value of %s' % param)
plt.savefig('%s_value.png' % param, dpi=400, bbox_inches='tight')
plt.show()

valid_data[param].hist(bins=100)
valid_data[param].plot(kind='kde', grid=True)
plt.title('hist & kde of %s' % param)
plt.savefig('%s_hist.png' % param, dpi=400, bbox_inches='tight')
plt.show()

scatter_matrix = ['OSC_32K(HZ)',
                  'OSC_455K(KHZ)',
                  'ERC_4M(KHZ)',
                  'VBG_3P0V()']
mat_value = valid_data[scatter_matrix]
pd.plotting.scatter_matrix(mat_value, diagonal='kde', color='k', alpha=0.3)
plt.show()

with pd.ExcelWriter('a242_data.xlsx') as writer:
    raw_data.to_excel(writer, sheet_name='raw_data')
    valid_data.to_excel(writer, sheet_name='useful_data')
    basic_sta.to_excel(writer, sheet_name='basic_sta')
