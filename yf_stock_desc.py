    # -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:36:33 2019
@author: Galileo
Clean、Desc
"""
import pandas as pd

class stock:
    def __init__(self, stock_number):
        self.stock_number = stock_number
    
    # 爬取每月股價並包裝成函式
    def craw_his(self):
        try:
            dfTmp = pd.read_csv('yf_his\\' + str(self.stock_number) + '.TW.csv', thousands = ',')
            
            return dfTmp
        
        except Exception:
            pass
    
gDfStock = pd.read_csv('stock.csv')       
gTickers = list(gDfStock.loc[:, '股票代號']) 

for i in gTickers:
    print(i)

    s = stock(i) 
    
    #Clean
    gDfHis = s.craw_his()
    
    gDfClean = gDfHis.loc[:, ['Date','Open','High','Low','Close','Adj Close','Volume']]
    #gDfClean = gDfClean[gDfClean['Open'] != '--']
    gDfClean.set_index("Date", inplace = True)
    gDfClean.to_csv(r'D:\python\stock\yf_clean\\' + str(i) + '.TW_CLEAN.csv')

    #DESC
    #gDfClean = pd.read_csv('yf_clean\\' + str(i) + '.TW_CLEAN.csv', thousands = ',')
    print(gDfClean.describe())
    gDfClean.describe().to_csv(r'D:\python\stock\yf_desc\\' + str(i) + '.TW_DESC.csv')
    #gDfClean.to_csv(r'D:\python\stock\yf_clean\\' + str(i) + '.TW_CLEAN.csv')
    