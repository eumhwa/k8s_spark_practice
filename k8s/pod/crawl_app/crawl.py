import os
import json
import requests

from urllib import request, parse
from bs4 import BeautifulSoup

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
    

def test_crawl(url:str):
    soup = BeautifulSoup(request.urlopen(url).read(), 'html.parser')
    res = soup.find_all("dd", "articleSubject")

    main_news_list = []
    for p in res:
        txt = p.text.replace('\n', '').replace(' ', '')
        main_news_list.append(txt)

    return main_news_list


def get_news_title(url:str, stock_name:str):
    stock_code = get_code(stock_name)
    param = {"code":stock_code}

    req = requests.get(url, params=param)
    soup = BeautifulSoup(req.text, "html.parser")
    res = soup.find_all("div", "content")
    print(res)
    
        
    return 

    
    