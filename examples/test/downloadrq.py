# from vnpy.trader.rqdata import RqdataClient
from datetime import datetime
import csv
from datetime import datetime
from typing import List, Tuple, Optional



from vnpy.trader.constant import Interval, Exchange
from vnpy.trader.database import BarOverview, DB_TZ
from vnpy.trader.database import database_manager
from vnpy.trader.engine import BaseEngine, MainEngine, EventEngine
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.rqdata import rqdata_client
from vnpy.trader.iexdata import iexdata_client
from vnpy.trader.tiingodata import tiingo_client
from vnpy.trader.setting import SETTINGS
import sys
from vnpy.trader.rqdata import rqdata_client
username  = SETTINGS['rqdata.username']
password  = SETTINGS['rqdata.password']
rqdata_client.init(username, password)

req = HistoryRequest(
    symbol='TSLA',
    exchange=Exchange.NASDAQ,
    start=DB_TZ.localize(datetime.strptime('2020-01-01','%Y-%m-%d')),
    interval=Interval.DAILY,
    end=datetime.now(DB_TZ)
)
data = rqdata_client.query_history(req)
print(data)



#
# start = datetime(2016, 1, 1)
# end = datetime(2019, 7, 30)
# # single_stock_history = client.getHistoricalPrices(['AAPL'])
# single_company_history = client.getCompanyInfo(['AAPL'])
# print(single_company_history)

