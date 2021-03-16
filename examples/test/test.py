# from vnpy.trader.rqdata import RqdataClient
from datetime import datetime

from vnpy.trader.iexdata import iexdata_client as client

from vnpy.event import EventEngine
from vnpy.app.data_manager.engine import ManagerEngine
from vnpy.app.data_manager.ui.widget import DownloadDialog
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

import sys

# 2. Create an instance of QApplication
app = QApplication([])
# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

APP_NAME = "DataManager"
event_engine = EventEngine()

main_engine = MainEngine(event_engine)
dm = main_engine.add_engine(ManagerEngine)

DownloadDialog(dm).download()


# 4. Show your application's GUI
window = MainWindow(main_engine, event_engine)

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())



#
# start = datetime(2016, 1, 1)
# end = datetime(2019, 7, 30)
# # single_stock_history = client.getHistoricalPrices(['AAPL'])
# single_company_history = client.getCompanyInfo(['AAPL'])
# print(single_company_history)

