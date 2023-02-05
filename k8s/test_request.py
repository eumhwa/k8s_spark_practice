import requests
import time

req_url = "http://127.0.0.1:64629/news_titles?stock_name=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
N_ITER = 10

for _ in range(N_ITER):
    response = requests.get(req_url)
    print(response)
    print(response.json())
