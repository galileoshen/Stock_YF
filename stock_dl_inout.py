    # -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:36:33 2019
@author: Galileo
Download inout
"""
from urllib.request import urlopen
import datetime
import pandas as pd
import json
import time
    
def dl_inout():
    for i in range(7):
        try:
            gdate = datetime.date.today() - datetime.timedelta(days = i)
            print(str(gdate))
            
            timeStruct = time.strptime(str(gdate), "%Y-%m-%d")
            strTime = time.strftime("%Y%m%d", timeStruct)
            craw_inout(strTime)
            
        except Exception:
            pass

def craw_inout(date):
    url = (
        'http://www.tse.com.tw/fund/T86?response=json&date=' + date + '&selectType=ALLBUT0999'
    )
    
    data = json.loads(urlopen(url).read())
    
    dfInout = pd.DataFrame(data['data'], columns=data['fields'])
    dfInout.to_csv(r'D:\python\stock\inout\\' + date + '.csv')
    
    time.sleep(3000.0/1000.0);
    
dl_inout()