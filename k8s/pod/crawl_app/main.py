import os
import json
import uvicorn

from fastapi import FastAPI, Response, status

from crawl import *

CODE_JSON_PATH = "./stock_code.json"
	
app = FastAPI()

'''
1. FastAPI app (backend API)
 - role : NLP task에 따른 알고리즘의 파라미터를 입력받고, crawling job과 kafka producer API 호출함 (kafka -> rabbitMQ)
 - 따라서 endpoint는 crawling + Task에 맞게 컨테이너 개발
 - crawling은 k8s가 관리하는 스파크 클러스터 내에서 동작 -> 결과를 json(?)으로 떨어뜨려준다
 - 이후 해당 json과 함께 Task에 대응하는 producer API를 호출

2. Producer API
 - role: NLP 알고리즘 컨테이너(core)에 job을 날려주는 API
 - 컨테이너로 감쌓은 FastAPI(uvicorn) app

3. NLP core 컨테이너
 - role: 토픽모델링, 감성분석, 예측 등의 알고리즘이 동작하는 서비스
 - consumer가 job을 받아서 동작한다
'''

@app.get("/test_api")
def crawl_naver_news(YY:str, MM:str, DD:str):
	date_param = f"{YY}-{MM}-{DD}"
	base_url = "https://finance.naver.com/news/mainnews.nhn" #naver stock main news url
    
	req_url = f"{base_url}?{date_param}"
	main_titles = test_crawl(req_url)
	
	return main_titles

@app.post("/update_code")
def update_stock_code(stock_name:str, stock_code:str):
	
	with open(CODE_JSON_PATH, encoding="UTF-8") as f:
		code_dict = json.load(f)
	
	code_dict[stock_name] = stock_code

	with open(CODE_JSON_PATH, "w", encoding="UTF-8") as outfile:
		json.dump(code_dict, outfile, ensure_ascii = False)

	return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/news_titles")
def crawl_naver_news(stock_name:str):
	
	base_url = "https://finance.naver.com/item/news.nhn"
    
	main_titles = get_news_title(base_url, stock_name)
	
	return main_titles