# -*- coding: utf-8 -*-
import csv

class CsvFile:
    def __init__(self):
        self.PATH_DOC = "../../docs/"
        self.FILE_NAME = "exchangeRateAdScraper.csv"

    def generate_file_csv(self, monetary_value, action_file):
        try:
            with open(self.PATH_DOC + self.FILE_NAME, action_file, newline='', encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
                if action_file == "w":
                    writer.writerow(["year", "month", "code", "description", "description", "price"])

                for money in monetary_value:
                    year = money.get("year")
                    month = money.get("month")
                    if money.get("money") is not None:
                        for m in money.get("money"):
                            if m[0].upper() != "EUR":
                                try:
                                    price = m[2].replace(",", ".")
                                    price = float(price)
                                except ValueError:
                                    price = None
                                writer.writerow([year, month, m[0].upper(), m[1], price])
        except FileNotFoundError:
            print("No such file or directory: {}".format(self.PATH_DOC + self.FILE_NAME))
