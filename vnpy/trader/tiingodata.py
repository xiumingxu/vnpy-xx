from datetime import timedelta
from typing import List, Optional
from pytz import timezone

from numpy import ndarray
from iexfinance.stocks import Stock, get_historical_data

# from iexdatac import init as iexdata_init
# from iexdatac.services.basic import all_instruments as iexdata_all_instruments
# from iexdatac.services.get_price import get_price as iexdata_get_price
# from iexdatac.share.errors import AuthenticationFailed
from tiingo import TiingoClient

from .setting import SETTINGS
from .constant import Exchange, Interval
from .object import BarData, TickData, HistoryRequest


INTERVAL_VT2RQ = {
    Interval.MINUTE: "1m",
    Interval.HOUR: "60m",
    Interval.DAILY: "1d",
}

INTERVAL_ADJUSTMENT_MAP = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta()         # no need to adjust for daily bar
}


config = {}

# To reuse the same HTTP Session across API calls (and have better performance), include a session key.
config['session'] = True

# If you don't have your API key as an environment variable,
# pass it in via a configuration dictionary.
config['api_key'] = SETTINGS['tiingo.token']

# Initialize
tiingo_client = TiingoClient(config)

