"""
Global setting of VN Trader.
"""

from logging import CRITICAL
from typing import Dict, Any
from tzlocal import get_localzone

from .utility import load_json

SETTINGS: Dict[str, Any] = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "rqdata.username": "+16692603794",
    "rqdata.password": "19911111DX",

    "iexdata.username": "+16692603794",
    "iexdata.token": "pk_ad0de14828b64af9a9f1f022953a39b3",

    "tiingo.token": "947d427079f7e6ee5163af80549c9b91afd8ad8f",



    "database.timezone": get_localzone().zone,
    "database.driver": "mysql",                # see database.Driver
    "database.database": "quant.xx",         # for sqlite, use this as filepath
    "database.host": "localhost",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "Einstein1991",
    "database.authentication_source": "admin",  # for mongodb

    "genus.parent_host": "",
    "genus.parent_port": "",
    "genus.parent_sender": "",
    "genus.parent_target": "",
    "genus.child_host": "",
    "genus.child_port": "",
    "genus.child_sender": "",
    "genus.child_target": "",
}

# Load global setting from json file.
SETTING_FILENAME: str = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))


def get_settings(prefix: str = "") -> Dict[str, Any]:
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}
