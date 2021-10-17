import sys

sys.path.append("../src/exchangeRateADScraper/")

from main import ExchangeRateADScraper

t = ExchangeRateADScraper()
expected = ["GBP", "LLIURA ESTERLINA", "0,7913"]

#assert t._ExchangeRateADScraper__get_monetary_value([], "2020")[0] == expected

#assert len(t._ExchangeRateADScraper__get_monetary_value([], "2020")) == 10


print(t._ExchangeRateADScraper__get_monetary_value({"link":"https://www.bopa.ad/bopa/027066/Pagines/GV20150923_14_58_00.aspx"}, "2014") )
