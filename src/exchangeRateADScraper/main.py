# -*- coding: utf-8 -*-
import global_vars
import requests
import html_webs
import copy
import functions
import csvfile
import time
import argparse
import evaluation
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ExchangeRateADScraper:
    def __init__(self):
        html = None
        self.soup = None
        if global_vars.is_developing:
            html = html_webs.html
        else:
            try:
                res = requests.get(global_vars.URL_GOVERN_DUANA, headers=global_vars.HEADERS)
                if res.status_code == 200:
                    html = res.text
                else:
                    raise requests.exceptions.HTTPError("Cannot reach the page. Check the url. HTTP Error: " + str(res.status_code))
            except requests.exceptions.ConnectionError as err:
                print("Failed to establish a new connection. Try later...")
            except requests.exceptions.HTTPError as err:
                print(err)
        if html is not None:
            self.soup = BeautifulSoup(html, "html.parser")
            self.csv = csvfile.CsvFile()

    def __get_years_on_web(self):
        years = []
        h4 = self.soup.findAll("h4", {"class": "expanded"})
        for year in h4:
            if " " in year.text:
                y = year.text.split()
                years.append(y[1])
            else:
                print("Error to read the month: " + year.text)
        return years

    def __get_bopa_links(self, year):
        bopa_links_year = []
        tables = self.soup.findAll("table", {"class": "zebra"})
        # remove the first table because we need the bottom tables
        try:
            tables.pop(0)
        except IndexError:
            pass
        for table in tables:
            for link in table.findChildren("a"):
                if year in link.text:
                    bopa_links_year.append({"text": link.text, "link": link['href']})
        return bopa_links_year

    def __get_monetary_value(self, link):
        monetary_value = []

        if global_vars.is_developing:
            html = html_webs.bopa
        else:
            res = requests.get(link.get("link"), headers=global_vars.headers, verify=False)
            html = res.text
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.findAll("tr"):
            money = []
            for p in tr.findChildren("p"):
                money.append(p.text)
            monetary_value.append(copy.copy(money))
        return monetary_value

    def do(self):
        # Check if we have the html code
        if self.soup is None:
            exit(1)
        action_file = "w"
        years = self.__get_years_on_web()
        for year in years:
            print("year=", year)
            bopa_links = self.__get_bopa_links(year)
            print("bopa_links", len(bopa_links))
            json_year = []
            for bopa_link in bopa_links:
                json_csv = dict()
                json_csv["year"] = year
                json_csv["month"] = functions.get_code_month(bopa_link.get("text"))
                json_csv["money"] = self.__get_monetary_value(bopa_link)
                json_year.append(json_csv)
                time.sleep(global_vars.SECOND_SLEEP)
            self.csv.generate_file_csv(json_year, action_file)
            action_file = "a" if action_file == "w" else "a"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process to use web scraping')
    parser.add_argument('action', help='list active param', choices=[global_vars.SCRAPING, global_vars.ANALIZE])

    args = parser.parse_args()
    if args.action == global_vars.ANALIZE:
        a = evaluation.Evaluation()
        a.do()
    elif args.action == global_vars.SCRAPING:
        ex = ExchangeRateADScraper()
        ex.do()
