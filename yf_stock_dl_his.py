    # -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:36:33 2019
@author: Galileo
yfinance Download
"""
import yfinance as yf
import datetime
import pandas as pd

gDfStock = pd.read_csv('stock.csv')    
gTickers = list(gDfStock.loc[:, '股票代號']) 

gSDate = datetime.datetime.now() - datetime.timedelta(days=2920)
gEDate = datetime.date.today()

#yfinance Download
for i in gTickers:
    print(i)
    
    dfStock = yf.download(str(i) + ".TW", gSDate, gEDate)
    dfStock.to_csv(r'D:\python\stock\yf_his\\' + str(i) + '.TW.csv')

