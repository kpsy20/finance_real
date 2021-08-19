from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='hello jinja')

# 네이버 금융 페이지 1~33페이지까지 보면서 종목 이름과 코드 리턴.
# 코스피!!


@app.route('/crawingAllKospi')
def crawingAllKospiNameAndCode():
    code_result = []
    name_result = []
    for page in range(1, 34):
        url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
        res = requests.get(url+str(page))
        html = res.text

        soup = bs(html, 'html.parser')
        title = soup.find_all('th')
        title = [x.text for x in title]

        summary = soup.find_all('tr')
        for i in range(7, len(summary)-1):
            a = summary[i].find_all('a')
            if(a != []):
                code = str(a[0]).index('code=')
                last = str(a[0])[code:].index('"')
                code_result.append(str(a[0])[code+5:code+last])
                name_result.append(a[0].text.replace(';', ''))  # .replace(
                # "-", "").replace("&", "").replace("(", "").replace(")", "").replace(" ", ""))
        print(page)

    return 'code_result, name_result'  # ([code_result], [name_result]) 형태로 리턴

# 네이버 금융 페이지 1~33페이지까지 보면서 종목 이름과 코드 리턴.
# 코스닥!!


@app.route('/crawingAllKosdaq')
def crawingAllKosdaqNameAndCode():
    code_result = []
    name_result = []
    for page in range(1, 32):
        url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
        res = requests.get(url+str(page))
        html = res.text

        soup = bs(html, 'html.parser')
        title = soup.find_all('th')
        title = [x.text for x in title]

        summary = soup.find_all('tr')
        for i in range(7, len(summary)-1):
            a = summary[i].find_all('a')
            if(a != []):
                code = str(a[0]).index('code=')
                last = str(a[0])[code:].index('"')
                code_result.append(str(a[0])[code+5:code+last])
                name_result.append(a[0].text.replace(';', ''))
                #  "-", "").replace("&", "").replace("(", "").replace(")", "").replace(" ", ""))
        print(page)
    return 'code_result, name_result'  # ([code_result], [name_result]) 형태로 리턴
