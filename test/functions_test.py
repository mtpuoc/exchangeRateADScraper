import sys

sys.path.append("../src/exchangeRateADScraper/")

from functions import get_code_month

assert get_code_month(None) is None
assert get_code_month("") is None
assert get_code_month(" ") is None
assert get_code_month("Gener ") is None
assert get_code_month("Gener 2020") == "01"
assert get_code_month("Genecr 2020") is None
