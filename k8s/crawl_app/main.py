import os
import json
import uvicorn

from fastapi import FastAPI, Response, status

from crawl import *

NEWS_MAIN_URL = "https://finance.naver.com/news/mainnews.nhn" #naver stock main news url
NEWS_URL = "https://finance.naver.com/item/news.nhn"

app = FastAPI()


@app.put("/code")
def update_stock_code(stock_name:str, stock_code:str):
	
	with open(CODE_JSON_PATH, encoding="UTF-8") as f:
		code_dict = json.load(f)
	
	code_dict[stock_name] = stock_code

	with open(CODE_JSON_PATH, "w", encoding="UTF-8") as outfile:
		json.dump(code_dict, outfile, ensure_ascii = False)

	return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/titles_by_date")
def crawl_naver_news(yyyy:str, mm:str, dd:str):
	date_param = f"{yyyy}-{mm}-{dd}"
	
	req_url = f"{NEWS_MAIN_URL}?{date_param}"
	return crawl_by_date(req_url)

@app.get("/news_titles")
def crawl_naver_news(stock_name:str):
	return get_news_title(NEWS_URL, stock_name)
