import random
import requests
from bs4 import BeautifulSoup

from src.sql_func import insert_to_table


def get_html(url, proxy=None):
    """
    function to get html code from the url
    :param url: url
    :param proxy: proxy ip
    :return: html code
    """
    resp = requests.get(url, proxies=proxy)
    return resp.text


def grab_all_info(link):
    """
    function grab all necessary info from link and put it in the table
    :param link: link
    :return: None
    """
    proxies = open('proxy.txt').read().split('\n')  # get proxy list from proxy.txt
    proxy = {'http': 'http://' + random.choice(proxies)}  # get proxy from proxy list

    html = get_html(link, proxy)
    parse_html = BeautifulSoup(html, 'html.parser')

    name = parse_html.find(class_='company-name').get_text()

    okpo = parse_html.find(id='clip_okpo')
    if okpo:
        okpo = int(okpo.get_text())
    else:
        okpo = 'NULL'

    ogrn = parse_html.find(id='clip_ogrn')
    if ogrn:
        ogrn = int(ogrn.get_text())
    else:
        ogrn = 'NULL'

    registration_date = parse_html.find(itemprop='foundingDate')
    if registration_date:
        registration_date = f"'{registration_date.get_text()}'"
    else:
        ogrn = 'NULL'

    capital_find = parse_html.find_all(class_='company-row')[1]
    capital_list = capital_find.find_all(class_='company-info__title')
    authorized_capital = 'NULL'
    for capital in capital_list:
        if capital.get_text() == 'Уставный капитал':
            authorized_capital = f"'{capital_find.select('span')[0].get_text()}'"

    status = parse_html.find(class_='attention-text')
    if status:
        status = status.get_text()
    else:
        status = 'Действующая'

    insert_to_table([name, ogrn, okpo, status, registration_date, authorized_capital])  # putting in the table
