import requests
import global_vars
import builtwith
import whois
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Evaluation:

    def __is_available_in_robots(self, web):
        is_available = True
        res = requests.get(web.get("web") + "robots.txt", headers=global_vars.HEADERS, verify=False)
        if res.status_code == 200 and web.get("contains") in res.text:
            is_available = False
        return is_available

    def __is_available_sitemap(self, web):
        is_available = True
        res = requests.get(web.get("web") + "sitemap.xml", headers=global_vars.HEADERS, verify=False)
        if res.status_code == 200 and web.get("contains") in res.text:
            is_available = False
        return is_available

    def __get_info_web(self, web):
        return builtwith.builtwith(web.get("web"))

    def __who_is(self, web):
        who_is = None
        try:
            who_is = whois.query(web.get("web"))
        except whois.exceptions.UnknownTld:
            pass
        return who_is

    def do(self):
        webs = [{"web": "http://www.duana.ad/", "contains": "canvis-monetaris"},
                     {"web": "https://www.bopa.ad/", "contains": "/bopa/"}]
        for web in webs:
            print("checking the page:", web)

            r = self.__is_available_in_robots(web)
            sleep(global_vars.SECOND_SLEEP)
            print("\trobots.txt is available", r)

            r = self.__is_available_sitemap(web)
            sleep(global_vars.SECOND_SLEEP)
            print("\tsitemap.xml", r)

            r = self.__get_info_web(web)
            print("\tInformation web:", r)
            sleep(global_vars.SECOND_SLEEP)

            r = self.__who_is(web)
            print("\twho is:", r)
            sleep(global_vars.SECOND_SLEEP*2)
