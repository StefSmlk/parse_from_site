import urllib.request as url_request
from multiprocessing import Pool
from bs4 import BeautifulSoup

from src.parse_func import grab_all_info
from src.sql_func import create_database, create_table

lst = ['https://www.rusprofile.ru/codes/89220', 'https://www.rusprofile.ru/codes/429110']


def get_all_pages(pages):
    """
    this function creates list of pages, if the site is multi-page

    :param pages: list of site links
    :return: list of pages
    """
    pages_lst = []
    for page in pages:
        with url_request.urlopen(page) as response:
            pages_lst.append(page)
    return pages_lst


def get_html_from_pages(pages):
    """
    this function creates list of links, which are on the site pages

    :param pages: list of pages
    :return: list of links
    """
    links = []
    for page in pages:
        with url_request.urlopen(page) as response:
            html_from_page = response.read()
        parse_html_all = BeautifulSoup(html_from_page, 'html.parser')
        for company_info in parse_html_all.find_all(class_='company-item'):
            company_id = str(company_info.a.attrs.get('href')).split('/')[2]
            links.append(f'https://www.rusprofile.ru/id/{company_id}')
    return links


def main():
    all_links = get_html_from_pages(get_all_pages(lst))  # get a list of links
    create_database()  # get a database if it haven't already created
    create_table()  # create table if it haven't already created
    with Pool(5) as pool:
        pool.map(grab_all_info, all_links)  # get the necessary information and put it into the table


if __name__ == '__main__':
    main()
