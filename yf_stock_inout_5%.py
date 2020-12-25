# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:36:33 2019
@author: Galileo
In/out 5%
"""
import pandas as pd
import datetime
import time

#取得收盤價
def craw_close(stock_number):
    try:
        dfClean = pd.read_csv('yf_clean\\' + str(stock_number) + '.TW_CLEAN.csv')
        dfClean = dfClean.reset_index(drop = True)
        
        row = dfClean.shape[0]
        close = dfClean.at[row - 1, 'Close']

        return close
    
    except Exception:
        return 0

#取得最近一天交易量
for i in range(7):
    try:
        gdate = datetime.date.today() - datetime.timedelta(days = i)
        print(str(gdate))
        
        timeStruct = time.strptime(str(gdate), "%Y-%m-%d")
        strTime = time.strftime("%Y%m%d", timeStruct)
        gDfStock = pd.read_csv('inout\\' + strTime + '.csv', thousands = ',')    
        
        break
    
    except Exception:
        pass
    
#Craw Close, Amount
gDfStock['Close'] = 0
gDfStock['Amount'] = 0

rows = gDfStock.shape[0]

for j in range(rows):
    sid = gDfStock.at[j, '證券代號']
    
    #取得收盤價
    close = craw_close(sid)
    gDfStock['Close'][j] = close
    
    finout = gDfStock['外陸資買賣超股數(不含外資自營商)'][j]
    #finout = gDfStock['三大法人買賣超股數'][j]
    gDfStock['Amount'][j] = float(close) * float(finout)
    
gDfStock.to_csv(r'D:\python\stock\stock_finout_5%_ORI.csv')
gDfTemp = gDfStock[gDfStock['外陸資買賣超股數(不含外資自營商)'] >= 0]
#gDfTemp = gDfStock[gDfStock['三大法人買賣超股數'] >= 0]
gDfTemp = gDfTemp.sort_values(by='Amount',ascending=False)
gDfTemp.to_csv(r'D:\python\stock\stock_fin_5%.csv')

gDfTemp = gDfStock[gDfStock['外陸資買賣超股數(不含外資自營商)'] < 0]
#gDfTemp = gDfStock[gDfStock['三大法人買賣超股數'] < 0]
gDfTemp = gDfTemp.sort_values(by='Amount',ascending=True)
gDfTemp.to_csv(r'D:\python\stock\stock_fout_5%.csv')

