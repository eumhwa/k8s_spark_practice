import os
import json
import requests

from urllib import request, parse
from bs4 import BeautifulSoup

NEWS_BASE_URL = "https://finance.naver.com"
CODE_JSON_PATH = "./stock_code.json"

def get_code(stock_name:str):

    with open(CODE_JSON_PATH, encoding="UTF-8") as f:
        code_dict = json.load(f)
	
    try:
        stock_code = code_dict[stock_name]
        return stock_code
    except Except as e:
        print(e)
        return
    

def crawl_by_date(url:str):
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all("dd", "articleSubject")

    main_news_list = []
    for p in res:
        txt = p.text.replace('\n', '').replace(' ', '')
        main_news_list.append(txt)

    return main_news_list


def get_news_title(url:str, stock_name:str):
    
    code_param = {"code" : get_code(stock_name)}
    res = requests.get(url, params=code_param)
    
    soup = BeautifulSoup(res.text, "html.parser")
    iframe = soup.find("iframe", id="news_frame")
    
    res_iframe = request.urlopen(f"{NEWS_BASE_URL}{iframe.attrs['src']}")
    iframe_soup = BeautifulSoup(res_iframe)
    
    title_tags = iframe_soup.find_all("td", class_="title")
    title_lst = []
    for tag in title_tags:
        txt = tag.text.replace('\n', '').replace(' ', '')
        title_lst.append(txt)

    print(title_lst)
    
    return title_lst

    
    