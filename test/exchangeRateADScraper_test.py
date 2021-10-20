import sys

sys.path.append("../src/exchangeRateADScraper/")

from main import ExchangeRateADScraper
import global_vars

global_vars.is_developing = True

t = ExchangeRateADScraper()
expected = ["GBP", "LLIURA ESTERLINA", "0,7913"]

assert t._ExchangeRateADScraper__get_monetary_value([], "2020", "01")[0] == expected

assert len(t._ExchangeRateADScraper__get_monetary_value([], "2020", "01")) == 10
