import tushare as ts
import pandas as pd

root_path='/Users/thomas.yuan/Documents/private/stock_analysis/'
data_path=root_path + 'database/'

# pro = ts.pro_api('c6e4eed05abcf7901c7edd4a08dece608991d32324be5504a047cd50')
# df = pro.query('daily',ts_code='000001.SH', start_date='20190721', end_date='20190722')
# df = pro.daily(trade_date='20190722')

df = ts.get_hist_data('sh',start='2018-07-23',end='2019-07-23') 
df.to_csv(data_path+'sh.csv',index=True, header=True,mode='a')

# f = open(data_path+'sh.csv','w')
# f.write(df)
# f.close()

print('success!')