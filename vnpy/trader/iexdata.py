from datetime import timedelta
from typing import List, Optional
from pytz import timezone

from numpy import ndarray
from iexfinance.stocks import Stock, get_historical_data

# from iexdatac import init as iexdata_init
# from iexdatac.services.basic import all_instruments as iexdata_all_instruments
# from iexdatac.services.get_price import get_price as iexdata_get_price
# from iexdatac.share.errors import AuthenticationFailed

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

CHINA_TZ = timezone("Asia/Shanghai")


class IexdataClient:
    """
    Client for querying history data from RQData.
    """

    def __init__(self):
        """"""
        self.username: str = SETTINGS["iexdata.username"]
        self.token: str = SETTINGS["iexdata.token"]

        self.inited: bool = False
        self.symbols: ndarray = None
        # self.api = 'https://cloud.iexapis.com/'

    def getCompanyInfo(self, symbols):
        """
        getCompanyInfo
        @returns : a dictionary with the company symbol as a key and the info as the value
        """
        stock_batch = Stock(symbols,
                            token=self.token)
        company_info = stock_batch.get_company()
        return company_info

    # TODO could get a full history
    def getDailyHistoricalPrices(self, stock, start=None, end=None):
        token = self.token
        return get_historical_data(stock, start, end,
                                   output_format='pandas',
                                   token=token)


    # def query_history(self, req: HistoryRequest) -> Optional[List[BarData]]:
    #     """
    #     Query history bar data from RQData.
    #     """
    #     if self.symbols is None:
    #         return None
    #
    #     symbol = req.symbol
    #     exchange = req.exchange
    #     interval = req.interval
    #     start = req.start
    #     end = req.end
    #
    #     iex_symbol = self.to_iex_symbol(symbol, exchange)
    #     if iex_symbol not in self.symbols:
    #         return None
    #
    #     iex_interval = INTERVAL_VT2RQ.get(interval)
    #     if not iex_interval:
    #         return None
    #
    #     # For adjust timestamp from bar close point (RQData) to open point (VN Trader)
    #     adjustment = INTERVAL_ADJUSTMENT_MAP[interval]
    #
    #     # For querying night trading period data
    #     end += timedelta(1)
    #
    #     # Only query open interest for futures contract
    #     fields = ["open", "high", "low", "close", "volume"]
    #     if not symbol.isdigit():
    #         fields.append("open_interest")
    #
    #     df = iexdata_get_price(
    #         iex_symbol,
    #         frequency=iex_interval,
    #         fields=fields,
    #         start_date=start,
    #         end_date=end,
    #         adjust_type="none"
    #     )
    #
    #     data: List[BarData] = []
    #
    #     if df is not None:
    #         for ix, row in df.iterrows():
    #             dt = row.name.to_pydatetime() - adjustment
    #             dt = CHINA_TZ.localize(dt)
    #
    #             bar = BarData(
    #                 symbol=symbol,
    #                 exchange=exchange,
    #                 interval=interval,
    #                 datetime=dt,
    #                 open_price=row["open"],
    #                 high_price=row["high"],
    #                 low_price=row["low"],
    #                 close_price=row["close"],
    #                 volume=row["volume"],
    #                 open_interest=row.get("open_interest", 0),
    #                 gateway_name="RQ"
    #             )
    #
    #             data.append(bar)
    #
    #     return data
    #
    # def query_tick_history(self, req: HistoryRequest) -> Optional[List[TickData]]:
    #     """
    #     Query history bar data from RQData.
    #     """
    #     if self.symbols is None:
    #         return None
    #
    #     symbol = req.symbol
    #     exchange = req.exchange
    #     start = req.start
    #     end = req.end
    #
    #     iex_symbol = self.to_iex_symbol(symbol, exchange)
    #     if iex_symbol not in self.symbols:
    #         return None
    #
    #     # For querying night trading period data
    #     end += timedelta(1)
    #
    #     # Only query open interest for futures contract
    #     fields = [
    #         "open",
    #         "high",
    #         "low",
    #         "last",
    #         "prev_close",
    #         "volume",
    #         "limit_up",
    #         "limit_down",
    #         "b1",
    #         "b2",
    #         "b3",
    #         "b4",
    #         "b5",
    #         "a1",
    #         "a2",
    #         "a3",
    #         "a4",
    #         "a5",
    #         "b1_v",
    #         "b2_v",
    #         "b3_v",
    #         "b4_v",
    #         "b5_v",
    #         "a1_v",
    #         "a2_v",
    #         "a3_v",
    #         "a4_v",
    #         "a5_v",
    #     ]
    #     if not symbol.isdigit():
    #         fields.append("open_interest")
    #
    #     df = iexdata_get_price(
    #         iex_symbol,
    #         frequency="tick",
    #         fields=fields,
    #         start_date=start,
    #         end_date=end,
    #         adjust_type="none"
    #     )
    #
    #     data: List[TickData] = []
    #
    #     if df is not None:
    #         for ix, row in df.iterrows():
    #             dt = row.name.to_pydatetime()
    #             dt = CHINA_TZ.localize(dt)
    #
    #             tick = TickData(
    #                 symbol=symbol,
    #                 exchange=exchange,
    #                 datetime=dt,
    #                 open_price=row["open"],
    #                 high_price=row["high"],
    #                 low_price=row["low"],
    #                 pre_close=row["prev_close"],
    #                 last_price=row["last"],
    #                 volume=row["volume"],
    #                 open_interest=row.get("open_interest", 0),
    #                 limit_up=row["limit_up"],
    #                 limit_down=row["limit_down"],
    #                 bid_price_1=row["b1"],
    #                 bid_price_2=row["b2"],
    #                 bid_price_3=row["b3"],
    #                 bid_price_4=row["b4"],
    #                 bid_price_5=row["b5"],
    #                 ask_price_1=row["a1"],
    #                 ask_price_2=row["a2"],
    #                 ask_price_3=row["a3"],
    #                 ask_price_4=row["a4"],
    #                 ask_price_5=row["a5"],
    #                 bid_volume_1=row["b1_v"],
    #                 bid_volume_2=row["b2_v"],
    #                 bid_volume_3=row["b3_v"],
    #                 bid_volume_4=row["b4_v"],
    #                 bid_volume_5=row["b5_v"],
    #                 ask_volume_1=row["a1_v"],
    #                 ask_volume_2=row["a2_v"],
    #                 ask_volume_3=row["a3_v"],
    #                 ask_volume_4=row["a4_v"],
    #                 ask_volume_5=row["a5_v"],
    #                 gateway_name="RQ"
    #             )
    #
    #             data.append(tick)
    #
    #     return data
    #

iexdata_client = IexdataClient()
