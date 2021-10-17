import sys

sys.path.append("../src/exchangeRateADScraper/")

import csvfile

c = csvfile.CsvFile()
c.PATH_DOC = "./"
c.FILE_NAME = "test_exchangeRateAdScraper.csv"

try:
    c.generate_file_csv([], "w")
    assert True
except:
    assert False
try:
    c.generate_file_csv([{}], "w")
    assert True
except:
    assert False

try:
    j = [{"year": "2020", "month": "01", "money": [["TEST", "money test", "33.6"], ["TEST", "money test", "33.6"]]}]
    c.generate_file_csv(j, "w")
    assert True
except:
    assert False

try:
    j = [{"year": "2020", "month": "01", "money": [["TEST", "money test", "33.6"], ["TEST", "money test", " "]]}]
    c.generate_file_csv(j, "w")
    assert True
except:
    assert False

